# flake8-import-order-tkalus

Package used as plugin for flake8-import-order

Based on base-[Style] and departs from there by:
 * Enforces combining third-party and app imports.
 * Module order ignores case
 * Name order is lexigraphical (case sensitive)
 * Relative module levels are reversed; ".." (level 2) is before "." (level 1)

See [demo_file](demo/complete_tkalus.py) for examples

## Status

Actively used.

## Usage

### Requirements

 * python 3.5+
 * flake8
 * flake8-import-order 0.18+

### Installation

```
pip install git+https://github.com/tkalus-config/flake8-import-order-tkalus@v2.0#egg=flake8-import-order-tkalus
```

### Running

Add this to your setup.cfg or .flake8

```
import-order-style=tkalus
```

## Roadmap

### Changelog

The changelog can be found in the [CHANGELOG.md](CHANGELOG.md) file.

### In progress

 * Maintaining

### Future

 * Tests

## License

flake8-import-order-tkalus is made available under the MIT license. See the [LICENSE file](LICENSE) for more info.
