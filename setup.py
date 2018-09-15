#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:28:28 2018

@author: Khaled Nakhleh
"""

from setuptools import setup

__version__ = "1.0.0"
__author__ = "Khaled Nakhleh"

description = "generates and combine sinusoidal functions"
requirements = [
 "numpy==1.11.3",
 "matplotlib==2.1.2"]

setup(
      name = "SignalSlice",
      description = description,
      install_requires = requirements,
      version = __version__,
      author = __author__,
      author_email="khaled.jamal.nakhleh@gmail.com",
      url="https://github.com/KhaledNakhleh/SignalSlice"    
      )
