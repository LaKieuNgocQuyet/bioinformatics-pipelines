import yaml
import argparse
import sys
import subprocess
sys.dont_write_bytecode = True

from modules.header import *

parser = argparse.ArgumentParser(description="None")
parser.add_argument("-I", "--input",required=True, type=str, help="None")
args = parser.parse_args()

INPUT_YAML = args.input

SAMPLE_LIST = {}
# Load input YAML file
with open(f"{INPUT_YAML}", "r") as f:
    input = yaml.safe_load(f)
    SAMPLES = input["sample"]
    REFERENCE = input["reference"]["genome"]
    KNOWN_SITES = input["reference"]["known_site"]
    OUTDIR = input["output"]["directory"]
# Group samples
for sample in SAMPLES:
    ID = sample["id"]
    R1 = sample["read1"]
    R2 = sample["read2"]

    FORWARD_AVERAGE_LENGTH = check_average_read_length(R1)
    REVERSE_AVERAGE_LENGTH = check_average_read_length(R2)
    AVERAGE_LENGTH = (FORWARD_AVERAGE_LENGTH + REVERSE_AVERAGE_LENGTH) / 2
    
    if AVERAGE_LENGTH >= 250:
        READ_TYPE = "long"
    else:
        READ_TYPE = "short"

    SAMPLE_LIST[ID] = {
        "read1": R1,
        "read2": R2,
        "read_type": READ_TYPE
    }
print(SAMPLE_LIST)


