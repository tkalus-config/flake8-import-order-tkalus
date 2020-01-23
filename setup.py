"""setup.py for flake8-import-order-tkalus."""

from setuptools import setup


__title__ = "flake8-import-order-tkalus"
__author__ = "Turtle Kalus"
__email__ = "turtle" "@" "kalus.us"
__version__ = "2.0"
__copyright__ = "Copyright (C) 2019 tkalus"
__license__ = "MIT License"

install_requires = ["flake8-import-order >= 0.18"]


setup(
    name=__title__,
    version=__version__,
    description="tkalus' custom import order plugin",
    long_description="",
    url="https://github.com/tkalus-config/flake8-import-order-tkalus",
    author=__author__,
    author_email=__email__,
    license=__license__,
    install_requires=install_requires,
    py_modules=["flake8_import_order_tkalus"],
    python_requires=">=3.5",
    entry_points={
        "flake8_import_order.styles": ["tkalus = flake8_import_order_tkalus:Tkalus"]
    },
    keyword="flake8 import imports ordering",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License (Expat)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
