#!/usr/bin/env python3
"""
Jinja Macro for the documentation
"""

import os

FILE_DIR = os.path.abspath(os.path.dirname(__file__))

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """
