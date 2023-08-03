#!/bin/bash

sbatch -J rdmE -o rdmE.out -e rdmE.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 GS_EGU.sh random_random 5

sbatch -J fbE -o fbE.out -e fbE.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 GS_EGU.sh facebook 5

sbatch -J rdsE -o rdsE.out -e rdsE.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 GS_EGU.sh erdos 5