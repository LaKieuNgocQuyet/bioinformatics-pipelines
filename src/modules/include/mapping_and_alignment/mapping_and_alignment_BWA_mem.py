import subprocess

def mapping_and_alignment_BWA_mem(SAMPLE_ID, PLATFORM, FORWARD, REVERSE, REFERENCE, OUTDIR, SAMPLE_OUTDIR, SAM_FILE):

    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            bwa mem -t 8 \
                -R "@RG\\tID:{SAMPLE_ID}\\tLB:lib1\\tPL:{PLATFORM}\\tPU:unit1\\tSM:{SAMPLE_ID}" \
                {REFERENCE} \
                {FORWARD} \
                {REVERSE} \
            > {SAMPLE_OUTDIR}/{SAM_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)