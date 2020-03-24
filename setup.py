#!/usr/bin/env python
# GlueMP4 is a script to trim, crop and concatenate MP4 fragments with ffmpeg.
# Copyright (C) 2019 Toon Verstraelen
#
# This file is part of GlueMP4.
#
# GlueMP4 is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# GlueMP4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
"""Installation script for GlueMP4."""


from setuptools import setup


setup(
    name="gluemp4",
    version="0.0.0",
    description="Simple driver for ffmpeg to stitch together MP4 video files.",
    url="https://github.com/tovrstra/gluemp4",
    package_dir={"gluemp4": "gluemp4"},
    packages=["gluemp4"],
    entry_points={"console_scripts": ["gluemp4 = gluemp4.__main__:main"]},
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["pyyaml"],
)
