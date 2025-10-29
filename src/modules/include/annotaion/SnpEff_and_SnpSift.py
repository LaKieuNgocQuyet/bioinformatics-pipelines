import subprocess

def snpEff_annotation(VCF_INPUT, OUTDIR):
    command = f"""
        /usr/bin/time -v -o {OUTDIR}/runtime.log \
            snpEff -lof GRCh37.p13 {VCF_INPUT} > {OUTDIR}/{vcf_output} \
        2>> {OUTDIR}/monitoring.log
    """