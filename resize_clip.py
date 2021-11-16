import subprocess


def change_resolution(name, w, h):
    subprocess.getstatusoutput(
        "ffmpeg -i test.mp4 -vf scale=" + str(w) + ":" + str(
            h) + " -preset slow -crf 18 " + name + ".mp4")
