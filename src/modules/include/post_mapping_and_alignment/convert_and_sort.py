import subprocess
def convert_and_sort(SAM_FILE, SAMPLE_OUTDIR, OUTDIR, SORTED_BAM_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log bash -c '\
            samtools view -@ 8 -Sb {SAMPLE_OUTDIR}/{SAM_FILE} | \
            samtools sort -@ 8 -o {SAMPLE_OUTDIR}/{SORTED_BAM_FILE}' \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)