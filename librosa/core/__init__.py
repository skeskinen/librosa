#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Core IO and DSP functions - stripped for smart-media-cutter."""

# Audio loading and resampling (resample is main function we need)
from .audio import (
    resample,
    to_mono,
    load,
    stream,
    get_duration,
    get_samplerate,
)

# Spectrum functions (needed for time_stretch via phase_vocoder)
from .spectrum import (
    stft,
    istft,
    phase_vocoder,
)

# FFT backend
from .fft import get_fftlib, set_fftlib

# Time/sample conversion utilities
from .convert import (
    frames_to_samples,
    frames_to_time,
    samples_to_frames,
    samples_to_time,
    time_to_samples,
    time_to_frames,
)

__all__ = [
    "resample",
    "to_mono",
    "load",
    "stream",
    "get_duration",
    "get_samplerate",
    "stft",
    "istft",
    "phase_vocoder",
    "get_fftlib",
    "set_fftlib",
    "frames_to_samples",
    "frames_to_time",
    "samples_to_frames",
    "samples_to_time",
    "time_to_samples",
    "time_to_frames",
]
