import subprocess
import argparse

parser = argparse.ArgumentParser(description="None")
parser.add_argument("-I", "--input",required=True, nargs="+", type=str, help="None")
parser.add_argument("-R", "--reference", required=True, type=str, help="None")
parser.add_argument("-O", "--outdir", required=False, type=str, help="None")
args = parser.parse_args()