import subprocess
import argparse


parser = argparse.ArgumentParser(description="None")
parser.add_argument("-I", "--input",required=True, nargs="+", type=str, help="None")
parser.add_argument("-R", "--reference", required=True, type=str, help="None")
parser.add_argument("-N", "--name", required=False, type=str, help="None")
args = parser.parse_args()


INPUT = args.input
REFERENCE = args.reference
NAME = args.name

FORWARD = INPUT[0]
REVERSE = INPUT[1] 
SAM_FILE = f"{NAME}.sam"
BAM_FILE = f"{NAME}.bam"
SORTED_BAM = f"{NAME}.sorted.bam"

long_read= f"""
	/usr/bin/time -v \
		minimap2 -x -a \
		{REFERENCE}.mmi \
		-R "@RG\tID:group1\tLB:lib1\tPL:illumina\tPU:unit1\tSM:sample1" \
		{FORWARD} \
		{REVERSE} \
		> {SAM_FILE} \
	2>> "$LOG
"""

short_read = f"""
	/usr/bin/time -v \
		bwa mem -t 8 -R "@RG\tID:group1\tLB:lib1\tPL:illumina\tPU:unit1\tSM:sample1" \
		{REFERENCE} \
		{FORWARD} \
		{REVERSE} \
		> {SAM_FILE} \
	2>> /home/lknq/KVM216_analysis/time.log
"""

def check_average_read_length(fastq):
    command = f'seqtk seq -A "{fastq}" | awk \'{{if(NR%2==0){{sum+=length($0);n++}}}} END{{if(n>0) print sum/n; else print 0}}\''
    average_length = subprocess.run(command, shell=True, capture_output=True, text=True)
    return float(average_length.stdout.strip() or 0)

FORWARD_AVERAGE_LENGTH = check_average_read_length(FORWARD)
REVERSE_AVERAGE_LENGTH = check_average_read_length(REVERSE)
AVERAGE_LENGTH = (FORWARD_AVERAGE_LENGTH + REVERSE_AVERAGE_LENGTH) / 2


if AVERAGE_LENGTH >= 250:
    subprocess.run(long_read, shell=True, check=True)
else:
    subprocess.run(short_read, shell=True, check=True)




