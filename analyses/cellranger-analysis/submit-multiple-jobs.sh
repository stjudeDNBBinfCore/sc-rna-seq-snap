#!/bin/bash

#BSUB -P run_cellranger
#BSUB -J submitter
#BSUB -q standard
#BSUB -n 1
#BSUB -R "rusage[mem=2500]"
#BSUB -o submitter.out
#BSUB -e submitter.err
#BSUB -cwd "/research/dept/dnb/core_operations/Bioinformatics/achroni/GitHub/sc-rna-seq-snap/analyses/cellranger-analysis"

########################################################################
# Set up running directory
prefix="/research/dept/dnb/core_operations/Bioinformatics/achroni/GitHub/sc-rna-seq-snap/analyses/cellranger-analysis"
cd "$(dirname "${BASH_SOURCE[0]}")" 
########################################################################
# Create directories to save output files to
mkdir -p ${prefix}/input
mkdir -p ${prefix}/results
mkdir -p ${prefix}/results/01_logs
mkdir -p ${prefix}/results/02_cellranger_count
mkdir -p ${prefix}/results/02_cellranger_count/DefaultParameters

########################################################################
# File in which we store the output text to verify the job execution order.
# As the jobs will run on the cluster, we pass in a path to the directory from
# which this launch script was run so everyone writes to the same file.
output_file="output.txt"

# Prints a simple LSF job file to standard output
function print_job {
    outfile=${1}
    delay_seconds=${2}

    # Preamble
    echo "#!/bin/bash"

    # Variables
    echo "time=\`date\`"
    echo "name=\${LSB_JOBNAME}"

    # Describe job when it comes online, delay, then write completion text
    echo "echo \"Online: name=\${name} time=\${time}\" >> ${outfile}"
    echo "sleep ${delay_seconds}"
    echo "echo \"Done: name=\${name}\" >> ${outfile}"
}

# Generate the LSF job files
for ((i=1; i<=2; i++)); do
    jobname="j${i}"
    print_job "${output_file}" 10 > "${prefix}/${jobname}.bsub"
    echo "bash ${prefix}/${jobname}.sh" >> "${prefix}/${jobname}.bsub"
done

# Submit job 1 - note no dependencies!
bsub -P run_CellRanger -q standard -n 1 -R "rusage[mem=2GB]" -R "span[hosts=1]" -J j1 -o j1.out -e j1.err "bash ${prefix}/j1.bsub"

# Job 2 depend on the successful completion of job 1

sleep 60
bsub < ${prefix}/waiter.sh