import subprocess


def mono_codec(name, codec):
    subprocess.getstatusoutput("ffmpeg -i test.mp4 -ac 1 " + str(name) + str(codec) + "")