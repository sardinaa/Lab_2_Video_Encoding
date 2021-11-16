import subprocess
from subprocess import call


def histogram(file):
    subprocess.getstatusoutput(
        "ffplay " + file + " -vf ""split=2[a][b],[b]histogram,"
                           "format=yuva444p[hh],[a][hh]overlay""")
