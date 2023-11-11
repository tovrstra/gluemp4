# GlueMP4 is a script to trim, crop and concatenate MP4 fragments with ffmpeg.
# Copyright (C) 2023 Toon Verstraelen
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
"""Generate initial config files based on Toony's filename conventions.

Existing files are not overwritten.
"""

import os
from glob import glob


def main():
    groups = {}
    for fn_raw in glob("*_raw*.mp4"):
        prefix = fn_raw[: fn_raw.find("_raw")]
        groups.setdefault(prefix, []).append(fn_raw)
    for prefix, fns_raw in groups.items():
        fn_config = f"{prefix}.yaml"
        if os.path.exists(fn_config):
            continue
        fn_output = f"{prefix}_cut.mp4"
        with open(fn_config, "w") as f:
            f.write("fragments:\n")
            for fn_raw in sorted(fns_raw):
                f.write(f'- ["{fn_raw}", "1664:1248:128:164", 0.0, null]\n')
            f.write(f"output: {fn_output}\n")


if __name__ == "__main__":
    main()
