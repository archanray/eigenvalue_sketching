#!/bin/bash
# sbatch -J dataset_name -o dataset_name.out -e dataset_name.err --nodes 6 --cpus-per-task 12 -p longq --mem 32000 run_swarm.sh dataset_name trials

#python single_function_tester.py 
python main_single_eval.py -d $1 -m $2 -t $3 -b $4
