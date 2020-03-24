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
"""Trim, crop and concatenate MP4 fragments with ffmpeg."""

import argparse
import os
import tempfile

import yaml


def run_verbose(command):
    """Print and execute a command."""
    print(command)
    os.system(command)


def main():
    """Main program."""
    args = parse_args()

    with open(args.fn_config) as f:
        config = yaml.safe_load(f)

    if args.tmpdir is None:
        # Default procedure: work in a temporary directory, which gets cleaned
        # up afterwards
        with tempfile.TemporaryDirectory() as tmpdir:
            work(config, tmpdir)
    else:
        # Alternative: create a user-specified working directory, which is not
        # cleaned up. This may be useful for debugging.
        tmpdir = os.path.abspath(args.tmpdir)
        if os.path.exists(tmpdir):
            print("Already exists:", tmpdir)
            return
        os.mkdir(tmpdir)
        work(config, tmpdir)


def parse_args():
    """Parse the command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Trim, crop and concatenate MP4 fragments with ffmpeg."
    )
    parser.add_argument("fn_config", help="The YAML config file.")
    parser.add_argument(
        "-t",
        "--tmpdir",
        default=None,
        help="The temporary directory to use. It should not exist yet and "
        "it will not be deleted afterwards.",
    )
    return parser.parse_args()


def work(config, tmpdir):
    """Perform the actual task using the given temporary directory."""
    fn_fragments = os.path.join(tmpdir, "fragments.txt")
    print(fn_fragments)
    with open(fn_fragments, "w") as f:
        for fn, crop, start, stop in config["fragments"]:
            fn_out = os.path.join(tmpdir, fn)
            f.write(f"file '{fn_out}'\n")
            options = [
                f"-i {fn}",
                f"-ss {start:.3f}",
                "-r 30",
                f'-filter:v "crop={crop}"',
                "-acodec copy",
                "-c:v libx264",
                fn_out,
            ]
            if stop is not None:
                options.insert(2, f"-to {stop:.3f}")
            run_verbose("ffmpeg {}".format(" ".join(options)))
    run_verbose(
        "ffmpeg -f concat -safe 0 -i {} -c copy {}".format(
            fn_fragments, config["output"]
        )
    )
