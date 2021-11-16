from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# https://www.py4u.net/discuss/146227


def cut_fragment(file, start_time, end_time):
    ffmpeg_extract_subclip(file, start_time, end_time, targetname="test.mp4")