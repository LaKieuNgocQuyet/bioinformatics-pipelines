import subprocess
def convert_and_sort(SAM_FILE, OUTDIR, SORTED_BAM):
    command = f"""
        /usr/bin/time -v -o ${OUTDIR}/runtime.log\
            samtools view -@ 8 -Sb {SAM_FILE} | \
            samtools sort -@ 8 -o {OUTDIR}/{SORTED_BAM} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)