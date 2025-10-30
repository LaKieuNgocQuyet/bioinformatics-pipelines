import subprocess

def mapping_and_alignment_Minimap2(SAMPLE_ID, PLATFORM, FORWARD, REVERSE, REFERENCE, OUTDIR, SAMPLE_OUTDIR, SAM_FILE):
    command = f"""
        /usr/bin/time -v -o {OUTDIR}/runtime.log \
            minimap2 -x -a \
                {REFERENCE}.mmi \
                -R "@RG\\tID:{SAMPLE_ID}\\tLB:lib1\\tPL:{PLATFORM}\\tPU:unit1\\tSM:{SAMPLE_ID}" \
                {FORWARD} \
                {REVERSE} \
                > {SAMPLE_OUTDIR}/{SAM_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)