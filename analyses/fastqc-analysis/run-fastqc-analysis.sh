#!/bin/bash

set -e
set -o pipefail

# Set up modules
module load fastqc/0.11.5
module load multiqc/1.0dev

# set up running directory
cd "$(dirname "${BASH_SOURCE[0]}")" 

# Create results dir
mkdir results
mkdir results/01-fastqc-reports

################################################################################################################
# Run FastQC per library

fastqc -o results/01-fastqc-reports /research/dept/hart/PI_data_distribution/zakhagrp/GSF/zakhagrp_321555_10XsNucRNAseq-1/*/*R2*.fastq.gz

################################################################################################################
# Run multiqc for all samples in the `results` dir
# to summarize results
 
cd results/01-fastqc-reports
multiqc . 

# rename folder
mv multiqc_data 02-multiqc-reports

# move the files related to multiqc in the main `results` dir
mv 02-multiqc-reports ../
mv multiqc_report.html ../
