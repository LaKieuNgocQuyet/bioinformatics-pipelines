import yaml
import argparse
import sys
import subprocess
import os
import logging
import time
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

known_sites_string = ""
if KNOWN_SITES:
    for site in KNOWN_SITES:
        known_sites_string += f"--known-sites {site} "

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(f"{OUTDIR}/runtime.log", mode="a", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

# Classification and define sample information
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

    SAMPLE_OUTDIR = os.path.join(OUTDIR, ID)
    os.makedirs(SAMPLE_OUTDIR, exist_ok=True)

    SAMPLE_LIST[ID] = {
        "read1": R1,
        "read2": R2,
        "sample_outdir": SAMPLE_OUTDIR,
        "platform": "illumina",
        "read_length_type": READ_TYPE,
        "average_length": AVERAGE_LENGTH,
        "sam_file": f"{ID}.sam",
        "bam_file": f"{ID}.bam",
        "sorted_bam_file": f"{ID}.sorted.bam",
        "marked_bam_file": f"{ID}.sorted.marked.bam",
        "recal_bam_file": f"{ID}.sorted.marked.recal.bam",
        "raw_gvcf_file": f"{ID}.raw.g.vcf",
        "raw_vcf_file": f"{ID}.raw.vcf",
        "filtered_vcf_file": f"{ID}.filtered.vcf",
        "final_vcf_file": f"{ID}.final.vcf"
    }
logging.info(f"Sample information:\n{yaml.dump(SAMPLE_LIST, sort_keys=False, default_flow_style=False)}")
# ================================================== #
#             Main pipeline execution                #
# ================================================== #

# +----------------------------------------------------------------------------------------------------+ #
# |                                        Mapping and Alignment                                       | #
# +----------------------------------------------------------------------------------------------------+ #
for sample_id, info in SAMPLE_LIST.items():
    start_time = time.time()
    logging.info(f"Mapping and alignment sample: {sample_id}")
    if info["read_length_type"] == "short":
        mapping_and_alignment_BWA_mem(
            SAMPLE_ID=sample_id,
            PLATFORM=info["platform"],
            FORWARD=info["read1"],
            REVERSE=info["read2"],
            REFERENCE=REFERENCE,
            OUTDIR=OUTDIR,
            SAMPLE_OUTDIR=info["sample_outdir"],
            SAM_FILE=info["sam_file"]
        )
    else:
        mapping_and_alignment_Minimap2(
            SAMPLE_ID=sample_id,
            PLATFORM=info["platform"],
            FORWARD=info["read1"],
            REVERSE=info["read2"],
            REFERENCE=REFERENCE,
            OUTDIR=OUTDIR,
            SAMPLE_OUTDIR=info["sample_outdir"],
            SAM_FILE=info["sam_file"]
        )
    end_time = time.time()
    duration = (end_time - start_time) / 60  
    logging.info(f"{sample_id} finished mapping and alignment in {duration:.2f} minutes")
logging.info("All samples finished mapping and alignment step.")
# +----------------------------------------------------------------------------------------------------+ #
# |                                      Post-mapping and Alignment                                    | #
# +----------------------------------------------------------------------------------------------------+ #
for sample_id, info in SAMPLE_LIST.items():
    start_time = time.time()
    logging.info(f"Post-mapping and alignment sample: {sample_id}")
    convert_and_sort(
        SAMPLE_OUTDIR=info["sample_outdir"],
        SAM_FILE=info["sam_file"],
        SORTED_BAM_FILE=info["sorted_bam_file"],
        OUTDIR=OUTDIR
    )
    markduplicates(
        SORTED_BAM_FILE=info["sorted_bam_file"],
        SAMPLE_OUTDIR=info["sample_outdir"],
        OUTDIR=OUTDIR,
        MARKED_BAM_FILE=info["marked_bam_file"],
    )
    baserecalibrator(
        MARKED_BAM_FILE=info["marked_bam_file"],
        SAMPLE_OUTDIR=info["sample_outdir"],
        KNOWN_SITES=known_sites_string,
        REFERENCE=REFERENCE,
        OUTDIR=OUTDIR
    )
    applyBQSR(
        MARKED_BAM_FILE=info["marked_bam_file"],
        REFERENCE=REFERENCE,
        SAMPLE_OUTDIR=info["sample_outdir"],
        OUTDIR=OUTDIR,
        RECAL_BAM_FILE=info["recal_bam_file"],
    )  
    end_time = time.time()
    duration = (end_time - start_time) / 60  
    logging.info(f"{sample_id} finished post-mapping and alignment in {duration:.2f} minutes")
logging.info("All samples finished post-mapping and alignment step.")    
# +----------------------------------------------------------------------------------------------------+ #
# |                                           Variant Calling                                          | #
# +----------------------------------------------------------------------------------------------------+ #
for sample_id, info in SAMPLE_LIST.items():
    start_time = time.time()
    logging.info(f"Variant calling sample: {sample_id}")
    SNPs_and_Indels_GATK(
        RECAL_BAM_FILE=info["recal_bam_file"],
        REFERENCE=REFERENCE,
        SAMPLE_OUTDIR=info["sample_outdir"],
        OUTDIR=OUTDIR,
        RAW_GVCF_FILE=info["raw_gvcf_file"],
    )
    end_time = time.time()
    duration = (end_time - start_time) / 60  
    logging.info(f"{sample_id} finished variant calling in {duration:.2f} minutes")
GVCF_FILE_LIST = ""
for sample_id, info in SAMPLE_LIST.items():
    GVCF_FILE_LIST += f" -V {info['sample_outdir']}/{info['raw_gvcf_file']} "    
combine_gvcfs(
    GVCF_FILE_LIST=GVCF_FILE_LIST,
    REFERENCE=REFERENCE,
    OUTDIR=OUTDIR
)


