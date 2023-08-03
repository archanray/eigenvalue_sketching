#!/bin/bash

sbatch -J rdmQ -o rdmQ.out -e rdmQ.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh random_random bki_Q 5

sbatch -J rdmZ -o rdmZ.out -e rdmZ.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh random_random bki_Z 5

sbatch -J rdmE -o rdmE.out -e rdmE.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh random_random eg_unldd 5

sbatch -J FBQ -o FBQ.out -e FBQ.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh facebook bki_Q 5

sbatch -J FBZ -o FBZ.out -e FBZ.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh facebook bki_Z 5

sbatch -J FBE -o FBE.out -e FBE.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh facebook eg_unldd 5

sbatch -J rdsQ -o rdsQ.out -e rdsQ.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh erdos bki_Q 5

sbatch -J rdsZ -o rdsZ.out -e rdsZ.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh erdos bki_Z 5

sbatch -J rdsE -o rdsE.out -e rdsE.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm_single_func.sh erdos eg_unldd 5