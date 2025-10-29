import subprocess

def markduplicates(SORTED_BAM_FILE, SAMPLE_OUTDIR, OUTDIR, MARKED_BAM_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            gatk MarkDuplicates \
                -I {SAMPLE_OUTDIR}/{SORTED_BAM_FILE} \
                -O {SAMPLE_OUTDIR}/{MARKED_BAM_FILE} \
                -M {SAMPLE_OUTDIR}/output.metrics.txt \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)