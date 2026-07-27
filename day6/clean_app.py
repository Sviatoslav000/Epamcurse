import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()

shutil.unpack_archive(args.name,'.')
