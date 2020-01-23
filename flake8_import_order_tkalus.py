"""Custom flake8-import-order."""


from flake8_import_order import ImportType
from flake8_import_order.styles import Style


class Tkalus(Style):
    """Custom import order... probably aligning with code [TKalus] works on the most."""

    @staticmethod
    def import_key(import_):
        """
        Set the full ordering.

        import [module]
        from [module] import [name]
        from .. import Name, anothername
        from . import Thirdname, secondname

        Module order ignores case
        Name order is lexigraphical (case sensitive)
        Relative module levels are reversed; ".." (level 2) is before "." (level 1)
        """
        modules = [module.lower() for module in import_.modules]
        level = import_.level
        if import_.type in {ImportType.APPLICATION_RELATIVE}:
            level *= -1
        return (import_.type, import_.is_from, level, modules, import_.names)

    @staticmethod
    def same_section(previous, current):
        """
        Ordering of sections, allowing for grouping

        Make sure we're classing APPLICATION and THIRD_PARTY types _together_.
        """
        same_type = current.type == previous.type
        both_first = {previous.type, current.type} <= {
            ImportType.APPLICATION,
            ImportType.THIRD_PARTY,
        }
        return same_type or both_first
