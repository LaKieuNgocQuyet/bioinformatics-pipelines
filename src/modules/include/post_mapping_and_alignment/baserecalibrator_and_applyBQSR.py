import subprocess

def baserecalibrator(MARKED_BAM_FILE, KNOWN_SITES, REFERENCE, SAMPLE_OUTDIR, OUTDIR):
    command = f"""
    /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
        gatk BaseRecalibrator \
            -I {SAMPLE_OUTDIR}/{MARKED_BAM_FILE} \
            -R {REFERENCE} \
            {KNOWN_SITES} \
            -O {SAMPLE_OUTDIR}/recal_data.table \
    2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

def applyBQSR ( MARKED_BAM_FILE, REFERENCE, SAMPLE_OUTDIR, OUTDIR, RECAL_BAM_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            gatk ApplyBQSR \
                -I {SAMPLE_OUTDIR}/{MARKED_BAM_FILE} \
                -R {REFERENCE} \
                --bqsr-recal-file {SAMPLE_OUTDIR}/recal_data.table \
                -O {SAMPLE_OUTDIR}/{RECAL_BAM_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)