#!/bin/bash

sbatch -J FB -o FB.out -e FB.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm.sh facebook 10 full

#sbatch -J rxv -o rxv.out -e rxv.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm.sh arxiv 10 full

sbatch -J rds -o rds.out -e rds.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm.sh erdos 10 full

sbatch -J rnd -o rnd.out -e rnd.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm.sh random_random 10 full

#sbatch -J kht -o kht.out -e kht.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm.sh kong_ht 10 full

#sbatch -J ktps -o ktps.out -e ktps.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 run_swarm.sh kong_tps 10 full