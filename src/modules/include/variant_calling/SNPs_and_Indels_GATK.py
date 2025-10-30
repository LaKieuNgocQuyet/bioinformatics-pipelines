import subprocess

def SNPs_and_Indels_GATK(RECAL_BAM_FILE, REFERENCE, SAMPLE_OUTDIR, OUTDIR, RAW_GVCF_FILE):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            gatk HaplotypeCaller \
                --native-pair-hmm-threads 8 \
                -I {SAMPLE_OUTDIR}/{RECAL_BAM_FILE} \
                -R {REFERENCE} \
                -O {SAMPLE_OUTDIR}/{RAW_GVCF_FILE} \
                -ERC GVCF \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

def combine_gvcfs(GVCF_FILE_LIST, REFERENCE, OUTDIR):
    command = f"""
        /usr/bin/time -v -a -o {OUTDIR}/runtime.log \
            gatk CombineGVCFs \
                -R {REFERENCE} \
                {GVCF_FILE_LIST} \
                -O {OUTDIR}/variant_combined.g.vcf \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)