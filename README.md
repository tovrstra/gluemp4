# GlueMP4

GlueMP4 is a simple driver script for ffmpeg to trim, crop and concatenate MP4
video fragments. It was developed to combine fragments of a lecture, recorded by
screencasting on a tablet, into a single video clip.

## Installation

```bash
pip install git+https://github.com/tovrstra/gluemp4.git@master
```

You also need to install ffmpeg separately:

- On Fedora Linux, first activate [RPM Fusion](https://rpmfusion.org/Configuration#Command_Line_Setup_using_rpm).
  Then run the following install command:

  ```bash
  sudo dnf install ffmpeg --allowerasing
  ```

## Usage

Make a YAML config file `config.yaml` describing the fragments going into the video clip:

```yaml
fragments:
- ["some_file1.mp4", "width:height:xleft:ytop", start, stop or null]
- ["some_file2.mp4", "width:height:xleft:ytop", start, stop or null]
- ...
output: final_output.mp4
```

Then run `gluemp4 config.yaml`.

## How to determine the cropping region?

Take a single snapshot from your video, e.g. with ffmpeg at second 3 of the video:

```bash
ffmpeg -i input.mp4 -ss 3.0 -f image2 -vframes 1 snapshot.jpeg
```

Then open the image `snapshot.jpeg` in teh Gimp and draw a rectangle with the
cropping tool, e.g. one that fits neatly your slide. Do not crop yet, just read
the parameters of the cropping window and copy them to the config file.
