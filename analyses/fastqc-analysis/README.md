# Pipeline for FastQC quality control tool for high throughput sequence data analysis

## Usage

`run-fastqc-analysis` is designed to be run as if it was called from this module directory even when called from outside of this directory.

Parameters according to the project and analysis strategy will need to be specified in the following scripts:
- `run-fastqc-analysis.sh`: define path to input data with `*R2*.fastq.gz` files.

### Run module on an interactive session on HPC

To run the script in this module from the command line sequentially, use:

```
bash run-fastqc-analysis.sh
```

### Run module by using lsf on HPC

There is also the option to run a lsf job on the HPC cluster by using the following command on an HPC node:

```
bsub < lsf-script.txt
```


## Folder content
This folder contains a script tasked to run FastQC quality control tool for all libraries across the project.
Each libary directory contains the following files:
- I1 is the 8 bp sample barcode, 
- R1 is the 16bp feature barcode + 10 bp UMI, and 
- R2 is the reads mapped to the transcriptome.
We only need to run FastQC on the single cell R2 files. Conducting read sequence QC on I1 or R1 wouldn't really tell us much other than do we trust our library indexing and barcode identification.

For more information, please:
- Type from the command line: fastqc --help, or
- See: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ 

## Folder structure 

The structure of this folder is as follows:

```
├── lsf-script.txt
├── README.md
├── results
|   ├── 01-fastqc-reports
|   ├── 02-multiqc-reports
|   └──multiqc_report.html
└── run-fastqc-analysis.sh
```

