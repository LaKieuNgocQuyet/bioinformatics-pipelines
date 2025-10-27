import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description="None")
parser.add_argument("-I", "--input",required=True, nargs="+", type=str, help="None")
parser.add_argument("-R", "--reference", required=True, type=str, help="None")
parser.add_argument("--known-sites", required=False, nargs="+", type=str, help="None")
parser.add_argument("-O", "--outdir", required=False, type=str, help="None")
args = parser.parse_args()

SAM_FILE = args.input
REFERENCE = args.reference
KNOWN_SITES = args.known_sites
OUTDIR = args.outdir

filename = os.path.basename(SAM_FILE)
file_root, file_extension = os.path.splitext(filename)
BAM_FILE = f"{file_root}.bam"
SORTED_BAM = f"{file_root}.sorted.bam"
MARKED_BAM = f"{file_root}.sorted.marked.bam"
RECAL_BAM = f"{file_root}.sorted.marked.recal.bam"

known_sites_string = ""
if KNOWN_SITES:
    for site in KNOWN_SITES:
        known_sites_string += f"--known-sites {site} "


convert_and_sort = f"""
    /usr/bin/time -v \
        samtools view -@ 8 -Sb {SAM_FILE} | \
        samtools sort -@ 8 -o {OUTDIR}/{SORTED_BAM} \
    2>> /home/lknq/KVM216_analysis/time.log
"""

markduplicates = f"""
    /usr/bin/time -v \
        gatk MarkDuplicates \
            -I {OUTDIR}/{SORTED_BAM} \
            -O {OUTDIR}/{MARKED_BAM} \
            -M {OUTDIR}/output.metrics.txt \
    2>> /home/lknq/KVM216_analysis/time.log
"""

baserecalibrator = f"""
    /usr/bin/time -v \
        gatk BaseRecalibrator \
            -I {OUTDIR}/{MARKED_BAM} \
            -R {REFERENCE} \
            {known_sites_string} \
            -O {OUTDIR}/recal_data.table \
    2>> /home/lknq/KVM216_analysis/time.log
"""
applyBQSR = f"""
    /usr/bin/time -v \
        gatk ApplyBQSR \
            -I {OUTDIR}/{MARKED_BAM} \
            -R {REFERENCE} \
            --bqsr-recal-file {OUTDIR}/recal_data.table \
            -O {OUTDIR}/{RECAL_BAM} \
    2>> /home/lknq/KVM216_analysis/time.log
"""

subprocess.run(convert_and_sort, shell=True, check=True)
subprocess.run(markduplicates, shell=True, check=True)
subprocess.run(baserecalibrator, shell=True, check=True)
subprocess.run(applyBQSR, shell=True, check=True)