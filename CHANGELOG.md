# Changelog

## Archived

* Module EOL'd.

## Release v2.0

* Major release - major changes
* (Still) enforces combining third-party and app imports.
* Module order ignores case (E.G. `str.lower()`)
* Name order is case-sensitive (I.E. lexigraphical)
* Relative module levels are reversed from default
  * "import ..B" (level 2) is before "import .A" (level 1)
* No longer deriving from Smarkets; using base Style class instead.
* Added demo .flake8 and python file

## Release v1.1

* Python 3.5 minimum.
 * Fix from Python 3.6 minimum in v1.0; 3.5 not yet EOL.
 * Deprecate Python 2.7

## Release v1.0

* Initial release
* Derived from Smarkets style from flake8-import-order
* Enforces combining third-party and app imports.
