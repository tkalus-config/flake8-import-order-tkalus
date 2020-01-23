from __future__ import absolute_import

import ast
import os
import StringIO
import sys
from functools import *
from os import path

import flake8_import_order
import localpackage
import X
import y
import Z
from flake8_import_order import *
from X import *
from X import A, B, C, b, d
from y import *
from y import A, B, C, D, e
from Z import A
from Z.a import Q, a
from Z.A.A import A
from Z.B import B

from .. import A, B
from ..A import A
from ..B import B
from . import A, B
from .A import A
from .B import B
