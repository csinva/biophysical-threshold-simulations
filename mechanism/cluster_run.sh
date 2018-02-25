#!/usr/bin/env bash
#SBATCH --ntasks=1
#SBATCH --job-name=arrayJob
#SBATCH --partition=economy
filename="mosinit.hoc"
nrniv -Py_NoSiteFlag -nogui -c "cmd_trial_num=${SLURM_ARRAY_TASK_ID}" $filename