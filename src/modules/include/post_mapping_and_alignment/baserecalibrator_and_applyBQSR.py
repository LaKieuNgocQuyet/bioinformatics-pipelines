import subprocess

def baserecalibrator(known_sites_string, MARKED_BAM, REFERENCE, OUTDIR):
    command = f"""
    /usr/bin/time -v -o {OUTDIR}/runtime.log\
        gatk BaseRecalibrator \
            -I {OUTDIR}/{MARKED_BAM} \
            -R {REFERENCE} \
            {known_sites_string} \
            -O {OUTDIR}/recal_data.table \
    2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

def applyBQSR ( MARKED_BAM, REFERENCE, OUTDIR, RECAL_BAM):
    command = f"""
        /usr/bin/time -v -o {OUTDIR}/runtime.log\
            gatk ApplyBQSR \
                -I {OUTDIR}/{MARKED_BAM} \
                -R {REFERENCE} \
                --bqsr-recal-file {OUTDIR}/recal_data.table \
                -O {OUTDIR}/{RECAL_BAM} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)