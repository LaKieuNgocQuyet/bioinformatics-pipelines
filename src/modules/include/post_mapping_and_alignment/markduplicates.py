import subprocess

def markduplicates(SORTED_BAM, OUTDIR, MARKED_BAM):
    command = f"""
        /usr/bin/time -v \
            gatk MarkDuplicates \
                -I {OUTDIR}/{SORTED_BAM} \
                -O {OUTDIR}/{MARKED_BAM} \
                -M {OUTDIR}/output.metrics.txt \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)