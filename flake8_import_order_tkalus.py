"""
Custom flake8-import-order, derived from smarkets style.

Key difference here is that third-party and application modules are combined.
"""


from flake8_import_order import ImportType
from flake8_import_order.styles import Smarkets


class Tkalus(Smarkets):
    """
    Custom import order.

    We use Smarkets as a base with the addition that third party and application
    imports should be in the same section.
    """

    @staticmethod
    def same_section(previous, current):
        """Make sure we're classing the types together."""
        same_type = current.type == previous.type
        both_first = {previous.type, current.type} <= {
            ImportType.APPLICATION,
            ImportType.THIRD_PARTY,
        }
        return same_type or both_first
