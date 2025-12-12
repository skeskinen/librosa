#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Librosa - stripped down for smart-media-cutter.

Only exports the functions actually needed:
- resample (from core.audio)
- time_stretch (from effects)
- fix_length (from util)
"""

from .version import version as __version__

# Import submodules
from . import core
from . import effects
from . import util

# Re-export commonly used functions at package level
from .core.audio import resample

# Exception classes
from .util.exceptions import (
    LibrosaError,
    ParameterError,
)

__all__ = [
    "core",
    "effects",
    "util",
    "resample",
    "LibrosaError",
    "ParameterError",
]
