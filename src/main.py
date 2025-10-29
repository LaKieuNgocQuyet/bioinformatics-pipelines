import yaml
import argparse
import sys
sys.dont_write_bytecode = True
from modules import header

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

for sample in SAMPLES:
    ID = sample["id"]
    R1 = sample["read1"]
    R2 = sample["read2"]

    SAMPLE_LIST[ID] = {
        "read1": R1,
        "read2": R2
    }


