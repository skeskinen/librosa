#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utility functions - stripped for smart-media-cutter."""

from .exceptions import LibrosaError, ParameterError

from .utils import (
    fix_length,
    frame,
    pad_center,
    valid_audio,
    valid_int,
    is_positive_int,
    normalize,
    tiny,
    MAX_MEM_BLOCK,
)

from .decorators import deprecated

__all__ = [
    "LibrosaError",
    "ParameterError",
    "fix_length",
    "frame",
    "pad_center",
    "valid_audio",
    "valid_int",
    "is_positive_int",
    "normalize",
    "tiny",
    "MAX_MEM_BLOCK",
    "deprecated",
]
