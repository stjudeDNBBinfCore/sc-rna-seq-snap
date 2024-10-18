#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author:
	Name: 			Cody Alexander Ramirez
	Email: 			cody.ramirez@stjude.org
	Affiliation: 	St. Jude Children's Research Hospital, Memphis, TN
	Date: 			June 27th, 2023
"""


import os, sys, argparse, glob, numpy, pandas


def dir_path(string):
	if os.path.isdir(string):
		return string
	else:
		raise NotADirectoryError(string)

#Beginning the argparse module to extract command-line arguments
parser = argparse.ArgumentParser(description="This is a script that will summarize cellranger count results from at least one cellranger output and create a summary within the 4_reports directory of the project. It accepts a data directory that contains at least one cellranger count results.")
#Creating the following optional arguments; some have default values
parser.add_argument('--dir', type=dir_path, help='Data directory path that contains individually named cellranger count results for samples', required=True)
parser.add_argument('--outdir', type=dir_path, help='Create all output files in the specified output directory. Please note that this directory must exist as the program will not create it.', required=True)
parser.add_argument('--genome', type=str, help='Only specify the genome you want to recover data from a multiple genome alignment', required=False)

#Converts argument strings to objects and assigns them as attributes of the namespace; e.g. --id -> args.id
args = parser.parse_args()


MasterDF = pandas.DataFrame()

for filename in glob.glob(os.path.join(args.dir, "*", "outs", "metrics_summary.csv")):
    # print(filename)
    
    df = pandas.read_csv(filename)
    df = df.replace(",", "", regex=True)
    df = df.replace("%", "", regex=True)
    df = df.astype('float')
    
    SampleID = filename.split("/outs")[0].split("/")[-1]
#     print(SampleID)
    df["Sample ID"] = SampleID
    
    
    Warnings = ""
    MajorWarnings = ""
    TotalWarnings = 0
    
    if args.genome == None:
        if df.iloc[0]["Estimated Number of Cells"] < 500:
            Warnings = Warnings + "Estimated Number of Cells < 500, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Estimated Number of Cell Partitions"] < 500:
            Warnings = Warnings + "GRCh38 Estimated Number of Cell Partitions < 500, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Estimated Number of Cell Partitions"] < 500:
            Warnings = Warnings + "mm10 Estimated Number of Cell Partitions < 500, "
            TotalWarnings += 1

    
    if args.genome == None:
        if df.iloc[0]["Estimated Number of Cells"] < 100:
            MajorWarnings = MajorWarnings + "Estimated Number of Cells < 100, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Estimated Number of Cell Partitions"] < 100:
            MajorWarnings = MajorWarnings + "GRCh38 Estimated Number of Cell Partitions < 100, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Estimated Number of Cell Partitions"] < 100:
            MajorWarnings = MajorWarnings + "mm10 Estimated Number of Cell Partitions < 100, "
            TotalWarnings += 1
    

    if df.iloc[0]["Mean Reads per Cell"] < 20000:
        MajorWarnings = MajorWarnings + "Mean Reads per Cell < 20000, "
        TotalWarnings += 1
    

    if args.genome == None:
        if df.iloc[0]["Median Genes per Cell"] < 1000:
            MajorWarnings = MajorWarnings + "Median Genes per Cell < 1000, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Median Genes per Cell"] < 1000:
            MajorWarnings = MajorWarnings + "GRCh38 Median Genes per Cell < 1000, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Median Genes per Cell"] < 1000:
            MajorWarnings = MajorWarnings + "mm10 Median Genes per Cell < 1000, "
            TotalWarnings += 1
    

    if df.iloc[0]["Valid Barcodes"] < 75:
        Warnings = Warnings + "Valid Barcodes < 75%, "
        TotalWarnings += 1
        
    if df.iloc[0]["Q30 Bases in Barcode"] < 85:
        Warnings = Warnings + "Q30 Bases in Barcode < 85%, "
        TotalWarnings += 1
    
    if df.iloc[0]["Q30 Bases in RNA Read"] < 85:
        Warnings = Warnings + "Q30 Bases in RNA Read < 85%, "
        TotalWarnings += 1
        
    if df.iloc[0]["Q30 Bases in UMI"] < 85:
        Warnings = Warnings + "Q30 Bases in UMI < 85%, "
        TotalWarnings += 1
    

    if args.genome == None:
        if df.iloc[0]["Reads Mapped to Genome"] < 85:
            Warnings = Warnings + "Reads Mapped to Genome < 85%, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Reads Mapped to Genome"] < 85:
            Warnings = Warnings + "GRCh38 Reads Mapped to Genome < 85%, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm19 Reads Mapped to Genome"] < 85:
            Warnings = Warnings + "mm10 Reads Mapped to Genome < 85%, "
            TotalWarnings += 1
    

    if args.genome == None:
        if df.iloc[0]["Reads Mapped Confidently to Genome"] < 80:
            MajorWarnings = MajorWarnings + "Reads Mapped Confidently to Genome < 80%, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Reads Mapped Confidently to Genome"] < 80:
            MajorWarnings = MajorWarnings + "GRCh38 Reads Mapped Confidently to Genome < 80%, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Reads Mapped Confidently to Genome"] < 80:
            MajorWarnings = MajorWarnings + "mm10 Reads Mapped Confidently to Genome < 80%, "
            TotalWarnings += 1
    

    if args.genome == None:
        if df.iloc[0]["Reads Mapped Confidently to Intergenic Regions"] > 10:
            Warnings = Warnings + "Reads Mapped Confidently to Intergenic Regions > 10%, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Reads Mapped Confidently to Intergenic Regions"] > 10:
            Warnings = Warnings + "GRCh38 Reads Mapped Confidently to Intergenic Regions > 10%, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Reads Mapped Confidently to Intergenic Regions"] > 10:
            Warnings = Warnings + "mm10 Reads Mapped Confidently to Intergenic Regions > 10%, "
            TotalWarnings += 1
    

    if args.genome == None:
        if df.iloc[0]["Reads Mapped Confidently to Intronic Regions"] > 30:
            Warnings = Warnings + "Reads Mapped Confidently to Intronic Regions > 30%, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Reads Mapped Confidently to Intronic Regions"] > 30:
            Warnings = Warnings + "GRCh38 Reads Mapped Confidently to Intronic Regions > 30%, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Reads Mapped Confidently to Intronic Regions"] > 30:
            Warnings = Warnings + "mm10 Reads Mapped Confidently to Intronic Regions > 30%, "
            TotalWarnings += 1
    

    if args.genome == None:
        if df.iloc[0]["Reads Mapped Confidently to Exonic Regions"] < 30:
            MajorWarnings = MajorWarnings + "Reads Mapped Confidently to Exonic Regions < 30%, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Reads Mapped Confidently to Exonic Regions"] < 30:
            MajorWarnings = MajorWarnings + "GRCh38 Reads Mapped Confidently to Exonic Regions < 30%, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Reads Mapped Confidently to Exonic Regions"] < 30:
            MajorWarnings = MajorWarnings + "mm10 Reads Mapped Confidently to Exonic Regions < 30%, "
            TotalWarnings += 1

    
    if args.genome == None:
        if df.iloc[0]["Reads Mapped Confidently to Transcriptome"] < 30:
            MajorWarnings = MajorWarnings + "Reads Mapped Confidently to Transcriptome < 30%, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Reads Mapped Confidently to Transcriptome"] < 30:
            MajorWarnings = MajorWarnings + "GRCh38 Reads Mapped Confidently to Transcriptome < 30%, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Reads Mapped Confidently to Transcriptome"] < 30:
            MajorWarnings = MajorWarnings + "mm10 Reads Mapped Confidently to Transcriptome < 30%, "
            TotalWarnings += 1
    

    if df.iloc[0]["Reads Mapped Antisense to Gene"] > 10:
        Warnings = Warnings + "Reads Mapped Antisense to Gene > 10%, "
        TotalWarnings += 1
    

    if args.genome == None:
        if df.iloc[0]["Fraction Reads in Cells"] < 70:
            MajorWarnings = MajorWarnings + "Fraction Reads in Cells < 70%, "
            TotalWarnings += 1
    elif args.genome == "GRCh38":
        if df.iloc[0]["GRCh38 Fraction Reads in Cells"] < 70:
            MajorWarnings = MajorWarnings + "GRCh38 Fraction Reads in Cells < 70%, "
            TotalWarnings += 1
    elif args.genome == "mm10":
        if df.iloc[0]["mm10 Fraction Reads in Cells"] < 70:
            MajorWarnings = MajorWarnings + "mm10 Fraction Reads in Cells < 70%, "
            TotalWarnings += 1
    
    
    df["Warnings"] = Warnings
    df["MajorWarnings"] = MajorWarnings
    df["Total Warnings"] = TotalWarnings
        
    MasterDF = pandas.concat([MasterDF, df])

MasterDF.to_csv( args.outdir + "QC_Summary_CellRanger_Report.tsv", sep = "\t", index = False)
