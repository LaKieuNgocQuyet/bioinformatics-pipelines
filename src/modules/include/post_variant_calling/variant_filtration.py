import subprocess

def hard_filtration(RAW_VCF_FILE, REFERENCE, SAMPLE_OUTDIR, OUTDIR, FILTERED_VCF_FILE):
    command = f"""
        /usr/bin/time -v -o {OUTDIR}/runtime.log \
            gatk VariantFiltration \
                -R {REFERENCE} \
                -V {SAMPLE_OUTDIR}/{RAW_VCF_FILE} \
                --filter-expression "vc.isSNP() && (QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0 || SOR > 3.0)" \
                --filter-name "MG_SNP_Filter" \
                --filter-expression "vc.isIndel() && (QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0)" \
                --filter-name "MG_INDEL_Filter" \
                -O {SAMPLE_OUTDIR}/{FILTERED_VCF_FILE} \
        2>> {OUTDIR}/monitoring.log
    """
    subprocess.run(command, shell=True, check=True)

