import subprocess

def snpEff_and_snpSift_annotation(FILTERED_VCF_FILE, SAMPLE_OUTDIR, OUTDIR, FINAL_VCF_FILE):
    command = f"""
        /usr/bin/time -v -o {OUTDIR}/runtime.log \
            snpEff -lof GRCh37.p13 {FILTERED_VCF_FILE} \
            | snpsift varType \
            | snpsift annotate -noId -name CLINVAR_ /home/lknq/anotation/clinvar/clinvar_20240716.vcf.gz \
            | snpsift annotate -noId -name p3_1000G_ /home/lknq/hg19_known-sites/1000G_phase1.indels.hg19.sites.vcf \
            | snpsift annotate -noId -info dbSNP138_ID /home/lknq/anotation/dbsnp/All_20180423.vcf.gz \
            | snpsift annotate -noId -info dbSNPBuildID /home/lknq/anotation/dbsnp/All_20180423.vcf.gz \
            | snpsift annotate -id /home/lknq/anotation/dbsnp/All_20180423.vcf.gz \
            | snpsift dbnsfp -v -db /home/lknq/anotation/dbNSFP/dbNSFP4.1a.txt.gz \
            > {SAMPLE_OUTDIR}/{FINAL_VCF_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

