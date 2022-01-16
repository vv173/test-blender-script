#!/usr/bin/env python3
# File name: test-blender-script.py
# Description: Python script thats executes test for blender by using pytest.
#               Run this script by using this command:
#               blender --background --python run.py -noaudio --python-use-system-env
# Author: Viktor Vodnev
# Date: 15-01-2022


import pytest
import logging


cmd = [
        'tests/',
        '--maxfail=2',
        '--tb=long',
        '--showlocals',
        '--log-format="%(asctime)s %(levelname)s %(message)s"',
        '--log-date-format="%Y-%m-%d %H:%M:%S"',
        '--log-file=./blender_test.log'
    ]


def bledner_check():
    try:
        import bpy
        logging.info("Successfully import blender pip module")
    except ImportError:
        logging.exception("Failed to install bpy, please run the script by using blender context")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='bpy_test.log',
                        format='%(asctime)s %(levelname)s:%(message)s')
    bledner_check()
    pytest.main(cmd)
