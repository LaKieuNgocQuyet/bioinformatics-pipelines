import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description="None")
parser.add_argument("-I", "--input",required=True, type=str, help="None")
parser.add_argument("-R", "--reference", required=True, type=str, help="None")
parser.add_argument("-O", "--outdir", required=False, type=str, help="None")
args = parser.parse_args()

RECAL_BAM = args.input
REFERENCE = args.reference
OUTDIR = args.outdir

filename = os.path.basename(RECAL_BAM)
file_root, file_extension = os.path.splitext(filename)
RAW_VCF = f"{file_root}.raw.vcf"

variant_calling = f"""
    /usr/bin/time -v \
        gatk HaplotypeCaller \
            --native-pair-hmm-threads 8 \
            -I {RECAL_BAM} \
            -R {REFERENCE} \
            -O {OUTDIR}/{RAW_VCF} \
            -L /home/lknq/hg19/S07604624_Regions.bed \
    2>> {OUTDIR}/monitoring.log
"""

subprocess.run(variant_calling, shell=True, check=True)
