import subprocess

def SNPs_and_Indels_GATK(RECAL_BAM, REFERENCE, OUTDIR, SAMPLE_NAME):
    command = f"""
        /usr/bin/time -v -o {OUTDIR}/runtime.log \
            gatk HaplotypeCaller \
                --native-pair-hmm-threads 8 \
                -I {RECAL_BAM} \
                -R {REFERENCE} \
                -O {OUTDIR}/{SAMPLE_NAME}.raw.vcf \
                -ERC GVCF
                -L /home/lknq/hg19/S07604624_Regions.bed \                
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)