#!/usr/bin/env bash
now=$(date +"%h_%d_%H:%M:%S")
local_home="/Users/chandansingh/drive/asdf/research/stochastic-simulations/thresh_model/"
remote_home="~/stochastic-simulations/thresh_model"
target_folder="${local_home}data/titrate/$now"
mkdir $target_folder
scp "cs3hq@interactive.hpc.virginia.edu:${remote_home}/data/titrate/*" $target_folder
echo $target_folder