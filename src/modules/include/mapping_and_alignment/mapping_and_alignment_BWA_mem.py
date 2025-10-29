import subprocess

def mapping_and_alignment_BWA_mem(FORWARD, REVERSE, REFERENCE, OUTDIR, SAM_FILE):

    short_read = f"""
        /usr/bin/time -v \
            bwa mem -t 8 -R "@RG\\tID:group1\\tLB:lib1\\tPL:illumina\\tPU:unit1\\tSM:sample1" \
            {REFERENCE} \
            {FORWARD} \
            {REVERSE} \
            > {OUTDIR}/{SAM_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(short_read, shell=True, check=True)