import pandas as pd
from cyvcf2 import VCF

vcf_file = VCF("/home/lknq/KVM148/KVM148S1.final.vcf")

data = []

columns = [
    #General
    "CHROM","POS","REF","ALT","DP","AD","QUAL","MQ","Zygosity","FILTER","Effect",
    "Putative_Impact","Gene_Name","Feature_Type","Feature_ID","Transcript_BioType",
    "Rank/Total","HGVS.c","HGVS.p","REF_AA","ALT_AA","cDNA_pos","cDNA_length","CDS_pos",
    "CDS_length","AA_pos","AA_length","Distance",
    #dbSNP138 annotation
    "dbSNP138_ID","dbSNP156_ID",
    #1000 genomes phase 3 annotation
    "p3_1000G_AF","p3_1000G_AFR_AF","p3_1000G_AMR_AF","p3_1000G_EAS_AF","p3_1000G_EUR_AF","p3_1000G_SAS_AF",
    #EVS annotation
    "ESP6500_MAF_EA","ESP6500_MAF_AA","ESP6500_MAF_ALL",
    #Clinvar annotation
    "CLINVAR_CLNSIG","CLINVAR_CLNDISDB","CLINVAR_CLNDN","CLINVAR_CLNREVSTAT",

    "ACMG_SF_v3.2","REF_AA_dbnsfp","ALT_AA_dbnsfp","hg38_chr","hg38_pos(1-based)","cds_strand","refcodon","codonpos",
    "codon_degeneracy","SIFT_score","SIFT_converted_rankscore","SIFT_pred","LRT_score",
    "LRT_converted_rankscore","LRT_pred","LRT_Omega","MutationTaster_score",
    "MutationTaster_converted_rankscore","MutationTaster_pred","MutationTaster_model",
    "MutationTaster_AAE","MutationAssessor_score","MutationAssessor_rankscore",
    "MutationAssessor_pred","FATHMM_score","FATHMM_converted_rankscore","FATHMM_pred",
    "PROVEAN_score","PROVEAN_converted_rankscore","PROVEAN_pred","MetaSVM_score",
    "MetaSVM_rankscore","MetaSVM_pred","MetaLR_score","MetaLR_rankscore","MetaLR_pred",
    "Reliability_index","M-CAP_score","M-CAP_rankscore","M-CAP_pred","MutPred_score",
    "MutPred_rankscore","MutPred_protID","MutPred_AAchange","MutPred_Top5features",
    "fathmm-MKL_coding_score","fathmm-MKL_coding_rankscore","fathmm-MKL_coding_pred",
    "fathmm-MKL_coding_group","Eigen-raw_coding","Eigen-phred_coding",
    "Eigen-PC-raw_coding","Eigen-PC-phred_coding","Eigen-PC-raw_coding_rankscore",
    "integrated_fitCons_score","integrated_fitCons_rankscore","integrated_confidence_value",
    "GERP++_NR","GERP++_RS","GERP++_RS_rankscore","gnomAD_exomes_AC","gnomAD_exomes_AN",
    "gnomAD_exomes_AF","gnomAD_exomes_AFR_AC","gnomAD_exomes_AFR_AN","gnomAD_exomes_AFR_AF",
    "gnomAD_exomes_AMR_AC","gnomAD_exomes_AMR_AN","gnomAD_exomes_AMR_AF",
    "gnomAD_exomes_ASJ_AC","gnomAD_exomes_ASJ_AN","gnomAD_exomes_ASJ_AF",
    "gnomAD_exomes_EAS_AC","gnomAD_exomes_EAS_AN","gnomAD_exomes_EAS_AF",
    "gnomAD_exomes_FIN_AC","gnomAD_exomes_FIN_AN","gnomAD_exomes_FIN_AF",
    "gnomAD_exomes_NFE_AC","gnomAD_exomes_NFE_AN","gnomAD_exomes_NFE_AF",
    "gnomAD_exomes_SAS_AC","gnomAD_exomes_SAS_AN","gnomAD_exomes_SAS_AF",
    "gnomAD_genomes_AC","gnomAD_genomes_AN","gnomAD_genomes_AF","gnomAD_genomes_AFR_AC",
    "gnomAD_genomes_AFR_AN","gnomAD_genomes_AFR_AF","gnomAD_genomes_AMR_AC",
    "gnomAD_genomes_AMR_AN","gnomAD_genomes_AMR_AF","gnomAD_genomes_ASJ_AC",
    "gnomAD_genomes_ASJ_AN","gnomAD_genomes_ASJ_AF","gnomAD_genomes_EAS_AC",
    "gnomAD_genomes_EAS_AN","gnomAD_genomes_EAS_AF","gnomAD_genomes_FIN_AC",
    "gnomAD_genomes_FIN_AN","gnomAD_genomes_FIN_AF","gnomAD_genomes_NFE_AC",
    "gnomAD_genomes_NFE_AN","gnomAD_genomes_NFE_AF","Interpro_domain","GTEx_V8_gene",
    "GTEx_V8_tissue","MIM_id","Gene_old_names","Gene_full_name","Pathway(Uniprot)",
    "Pathway(BioCarta)_short","Pathway(BioCarta)_full","Pathway(ConsensusPathDB)",
    "Pathway(KEGG)_id","Pathway(KEGG)_full","Function_description","Disease_description",
    "MIM_phenotype_id","MIM_disease","Trait_association(GWAS)","GO_biological_process",
    "GO_cellular_component","GO_molecular_function","Tissue_specificity(Uniprot)",
    "Expression(egenetics)","Expression(GNF/Atlas)","Interactions(IntAct)",
    "Interactions(BioGRID)","Interactions(ConsensusPathDB)","P(HI)","P(rec)",
    "Known_rec_info","RVIS_EVS","RVIS_percentile_EVS","LoF-FDR_ExAC","RVIS_ExAC",
    "RVIS_percentile_ExAC","GHIS","GDI","GDI-Phred",
    "Gene_damage_prediction(all_disease-causing_genes)",
    "Gene_damage_prediction(all_Mendelian_disease-causing_genes)",
    "Gene_damage_prediction(Mendelian_AD_disease-causing_genes)",
    "Gene_damage_prediction(Mendelian_AR_disease-causing_genes)",
    "Gene_damage_prediction(all_PID_disease-causing_genes)",
    "Gene_damage_prediction(PID_AD_disease-causing_genes)",
    "Gene_damage_prediction(PID_AR_disease-causing_genes)",
    "Gene_damage_prediction(all_cancer_disease-causing_genes)",
    "Gene_damage_prediction(cancer_recessive_disease-causing_genes)",
    "Gene_damage_prediction(cancer_dominant_disease-causing_genes)"
]

for record in vcf_file:

    ANN_values = record.INFO.get("ANN")
    if not ANN_values:
        continue
    if isinstance(ANN_values, str):
        ANN_values_first = ANN_values.split(",")[0]
    else:
        ANN_values_first = ANN_values[0]
    ANN_field_value =  ANN_values_first.split("|")    

    row = {}
    # =============================================== #
    #                  General fields
    # =============================================== #
    row["CHROM"] = record.CHROM
    row["POS"] = record.POS
    row["REF"] = record.REF
    row["ALT"] = record.ALT[0] if record.ALT else None
    dp_array = record.format("DP", None)
    row["DP"] = int(dp_array[0][0]) if dp_array is not None else None
    ad_array = record.format("AD")
    row["AD"] = int(ad_array[0][1]) if ad_array is not None and len(ad_array[0]) > 1 else None
    row["QUAL"] = round(record.QUAL,2) 
    row["MQ"] = round(record.INFO.get("MQ", None),2) 
    gt = record.genotypes[0] 
    if gt[0] == gt[1]:
        row["Zygosity"] = "HOM" if gt[0] != 0 else "Ref"
    else:
        row["Zygosity"] = "HET"
    row["FILTER"] = record.FILTER if record.FILTER else "PASS"
    row["Effect"] = ANN_field_value[1] if len(ANN_field_value) > 1 else None
    row["Putative_Impact"] = ANN_field_value[2] if len(ANN_field_value) > 2 else None
    row["Gene_Name"] = ANN_field_value[3] if len(ANN_field_value) > 3 else None
    row["Feature_Type"] = ANN_field_value[5] if len(ANN_field_value) > 5 else None
    row["Feature_ID"] = ANN_field_value[6] if len(ANN_field_value) > 6 else None
    row["Transcript_BioType"] = ANN_field_value[7] if len(ANN_field_value) > 7 else None
    row["Rank/Total"] = ANN_field_value[8] if len(ANN_field_value) > 8 else None
    row["HGVS.c"] = ANN_field_value[9] if len(ANN_field_value) > 9 else None
    row["HGVS.p"] = ANN_field_value[10] if len(ANN_field_value) > 10 else None
    if len(ANN_field_value) > 11:
        cDNA = ANN_field_value[11].split("/") if "/" in ANN_field_value[11] else [ANN_field_value[11], None]
        row["cDNA_pos"] = cDNA[0]
        row["cDNA_length"] = cDNA[1]
    if len(ANN_field_value) > 12:
        CDS = ANN_field_value[12].split("/") if "/" in ANN_field_value[12] else [ANN_field_value[12], None]
        row["CDS_pos"] = CDS[0]
        row["CDS_length"] = CDS[1]
    if len(ANN_field_value) > 13:
        AA = ANN_field_value[13].split("/") if "/" in ANN_field_value[13] else [ANN_field_value[13], None]
        row["AA_pos"] = AA[0]
        row["AA_length"] = AA[1]
    row["Distance"] = ANN_field_value[14] if len(ANN_field_value) > 14 else None
    # =============================================== #
    #                dbSNP138 annotation
    # =============================================== #
    row["dbSNP138_ID"] = record.ID
    # =============================================== #
    #          1000 genomes phase 3 annotation
    # =============================================== #
    row["p3_1000G_AF"] = record.INFO.get("p3_1000G_AF", None)
    row["p3_1000G_AFR_AF"] = record.INFO.get("p3_1000G_AFR_AF", None)
    row["p3_1000G_AMR_AF"] = record.INFO.get("p3_1000G_AMR_AF", None)
    row["p3_1000G_EAS_AF"] = record.INFO.get("p3_1000G_EAS_AF", None)
    row["p3_1000G_EUR_AF"] = record.INFO.get("p3_1000G_EUR_AF", None)
    row["p3_1000G_SAS_AF"] = record.INFO.get("p3_1000G_SAS_AF", None)
    # =============================================== #
    #                 EVS annotation
    # =============================================== #
    ESP6500_MAF_str = record.INFO.get("ESP6500_MAF", None)
    if ESP6500_MAF_str:
        ESP6500_MAF_array = ESP6500_MAF_str.split(",")
        EA = float(ESP6500_MAF_array[0]) / 100 if ESP6500_MAF_array[0] not in (".", "") else None
        AA = float(ESP6500_MAF_array[1]) / 100 if ESP6500_MAF_array[1] not in (".", "") else None
        ALL = float(ESP6500_MAF_array[2]) / 100 if ESP6500_MAF_array[2] not in (".", "") else None
    else:
        EA = AA = ALL = None
    row["ESP6500_MAF_EA"] = EA
    row["ESP6500_MAF_AA"] = AA
    row["ESP6500_MAF_ALL"] = ALL
    # =============================================== #
    #                Clinvar annotation
    # =============================================== #
    row["CLINVAR_CLNSIG"] = record.INFO.get("CLINVAR_CLNSIG", None)
    row["CLINVAR_CLNDISDB"] = record.INFO.get("CLINVAR_CLNDISDB", None)
    row["CLINVAR_CLNDN"] = record.INFO.get("CLINVAR_CLNDN", None)
    row["CLINVAR_CLNREVSTAT"] = record.INFO.get("CLINVAR_CLNREVSTAT", None)


    # row[""]
    # row[""]
    # row[""]
    data.append(row)


df = pd.DataFrame(data, columns=columns)

with pd.ExcelWriter("new_template.xlsx", engine="xlsxwriter") as writer:
    df_filled = df.fillna(".")
    df_filled.to_excel(writer, index=False, sheet_name="Sheet 1")
    workbook = writer.book
    worksheet = writer.sheets["Sheet 1"]

    header_format = workbook.add_format({
        'bold': True,
        'font_color': 'black',
        'font_size': 9,  
        'bg_color': "#ADCAE6",
        'border': 1,
        'font_name': 'Arial',
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
    })
    data_format = workbook.add_format({
        'font_name': 'Arial',
        'font_color': 'black',
        'font_size': 9,  
        'bold': False,
        'text_wrap': False, 
        'align': 'general' 
    })
    # Tô màu header
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

    # Bật filter
    worksheet.autofilter(0, 0, 0, len(df.columns)-1)

    row_height = 7 * 15
    worksheet.set_row(0, row_height)

    for row_num in range(1, len(df_filled) + 1):
        worksheet.set_row(row_num, None, data_format)
    

