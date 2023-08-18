#!/bin/bash

# sbatch -J fbed10 -o fbed10.out -e fbed10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_deflate 5 10
# sbatch -J fbed20 -o fbed20.out -e fbed20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_deflate 5 20
# sbatch -J fbed40 -o fbed40.out -e fbed40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_deflate 5 40
# sbatch -J fbed80 -o fbed80.out -e fbed80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_deflate 5 80
# sbatch -J fbed12 -o fbed12.out -e fbed12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_deflate 5 120
# sbatch -J fbef10 -o fbef10.out -e fbef10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_flip 5 10
# sbatch -J fbef20 -o fbef20.out -e fbef20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_flip 5 20
# sbatch -J fbef40 -o fbef40.out -e fbef40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_flip 5 40
# sbatch -J fbef80 -o fbef80.out -e fbef80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_flip 5 80
# sbatch -J fbef12 -o fbef12.out -e fbef12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook eigengame_flip 5 120
# sbatch -J fbbki10 -o fbbki10.out -e fbbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook bki_adp_Q 5 10
# sbatch -J fbbki20 -o fbbki20.out -e fbbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook bki_adp_Q 5 20
# sbatch -J fbbki40 -o fbbki40.out -e fbbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook bki_adp_Q 5 40
# sbatch -J fbbki80 -o fbbki80.out -e fbbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook bki_adp_Q 5 80
# sbatch -J fbbki12 -o fbbki12.out -e fbbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook bki_adp_Q 5 120
# sbatch -J fboad -o fboad.out -e fboad.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook oth_adp 5 full
# sbatch -J fbona -o fbona.out -e fbona.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook oth_nonadp 5 full
# sbatch -J fbsna -o fbsna.out -e fbsna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh facebook sw_nonadp 5 full

# sbatch -J rnded10 -o rnded10.out -e rnded10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_deflate 5 10
# sbatch -J rnded20 -o rnded20.out -e rnded20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_deflate 5 20
# sbatch -J rnded40 -o rnded40.out -e rnded40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_deflate 5 40
# sbatch -J rnded80 -o rnded80.out -e rnded80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_deflate 5 80
# sbatch -J rnded12 -o rnded12.out -e rnded12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_deflate 5 120
# sbatch -J rndef10 -o rndef10.out -e rndef10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_flip 5 10
# sbatch -J rndef20 -o rndef20.out -e rndef20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_flip 5 20
# sbatch -J rndef40 -o rndef40.out -e rndef40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_flip 5 40
# sbatch -J rndef80 -o rndef80.out -e rndef80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_flip 5 80
# sbatch -J rndef12 -o rndef12.out -e rndef12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random eigengame_flip 5 120
# sbatch -J rndbki10 -o rndbki10.out -e rndbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random bki_adp_Q 5 10
# sbatch -J rndbki20 -o rndbki20.out -e rndbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random bki_adp_Q 5 20
# sbatch -J rndbki40 -o rndbki40.out -e rndbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random bki_adp_Q 5 40
# sbatch -J rndbki80 -o rndbki80.out -e rndbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random bki_adp_Q 5 80
# sbatch -J rndbki12 -o rndbki12.out -e rndbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random bki_adp_Q 5 120
# sbatch -J rndoad -o rndoad.out -e rndoad.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random oth_adp 5 full
# sbatch -J rndona -o rndona.out -e rndona.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random oth_nonadp 5 full
# sbatch -J rndsna -o rndsna.out -e rndsna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh random sw_nonadp 5 full

# sbatch -J rdsed10 -o rdsed10.out -e rdsed10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_deflate 5 10
# sbatch -J rdsed20 -o rdsed20.out -e rdsed20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_deflate 5 20
# sbatch -J rdsed40 -o rdsed40.out -e rdsed40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_deflate 5 40
# sbatch -J rdsed80 -o rdsed80.out -e rdsed80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_deflate 5 80
# sbatch -J rdsed12 -o rdsed12.out -e rdsed12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_deflate 5 120
# sbatch -J rdsef10 -o rdsef10.out -e rdsef10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_flip 5 10
# sbatch -J rdsef20 -o rdsef20.out -e rdsef20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_flip 5 20
# sbatch -J rdsef40 -o rdsef40.out -e rdsef40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_flip 5 40
# sbatch -J rdsef80 -o rdsef80.out -e rdsef80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_flip 5 80
# sbatch -J rdsef12 -o rdsef12.out -e rdsef12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos eigengame_flip 5 120
# sbatch -J rdsbki10 -o rdsbki10.out -e rdsbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos bki_adp_Q 5 10
# sbatch -J rdsbki20 -o rdsbki20.out -e rdsbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos bki_adp_Q 5 20
# sbatch -J rdsbki40 -o rdsbki40.out -e rdsbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos bki_adp_Q 5 40
# sbatch -J rdsbki80 -o rdsbki80.out -e rdsbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos bki_adp_Q 5 80
# sbatch -J rdsbki12 -o rdsbki12.out -e rdsbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos bki_adp_Q 5 120
# sbatch -J rdsoad -o rdsoad.out -e rdsoad.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos oth_adp 5 full
# sbatch -J rdsona -o rdsona.out -e rdsona.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos oth_nonadp 5 full
# sbatch -J rdssna -o rdssna.out -e rdssna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_eval.sh erdos sw_nonadp 5 full

sbatch -J fbbki10 -o fbbki10.out -e fbbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 10
sbatch -J fbbki20 -o fbbki20.out -e fbbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 20
sbatch -J fbbki40 -o fbbki40.out -e fbbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 40
sbatch -J fbbki80 -o fbbki80.out -e fbbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 80
sbatch -J fbbki12 -o fbbki12.out -e fbbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 120

sbatch -J rndbki10 -o rndbki10.out -e rndbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 10
sbatch -J rndbki20 -o rndbki20.out -e rndbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 20
sbatch -J rndbki40 -o rndbki40.out -e rndbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 40
sbatch -J rndbki80 -o rndbki80.out -e rndbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 80
sbatch -J rndbki12 -o rndbki12.out -e rndbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 120

sbatch -J rdsbki10 -o rdsbki10.out -e rdsbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 10
sbatch -J rdsbki20 -o rdsbki20.out -e rdsbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 20
sbatch -J rdsbki40 -o rdsbki40.out -e rdsbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 40
sbatch -J rdsbki80 -o rdsbki80.out -e rdsbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 80
sbatch -J rdsbki12 -o rdsbki12.out -e rdsbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 120

sbatch -J eyebki10 -o eyebki10.out -e eyebki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 10
sbatch -J eyebki20 -o eyebki20.out -e eyebki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 20
sbatch -J eyebki40 -o eyebki40.out -e eyebki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 40
sbatch -J eyebki80 -o eyebki80.out -e eyebki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 80
sbatch -J eyebki12 -o eyebki12.out -e eyebki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 120

# sbatch -J fboadp -o fboadp.out -e fboadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook oth_adp 5
# sbatch -J rmoadp -o rmoadp.out -e rmoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random oth_adp 5
# sbatch -J rsoadp -o rsoadp.out -e rsoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos oth_adp 5
# sbatch -J eyoadp -o eyoadp.out -e eyoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye oth_adp 5
# sbatch -J rxoadp -o rxoadp.out -e rxoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv oth_adp 5

# sbatch -J fbswna -o fbswna.out -e fbswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook sw_nonadp 5
# sbatch -J rmswna -o rmswna.out -e rmswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random sw_nonadp 5
# sbatch -J rsswna -o rsswna.out -e rsswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos sw_nonadp 5
# sbatch -J eyswna -o eyswna.out -e eyswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye sw_nonadp 5
# sbatch -J rxswna -o rxswna.out -e rxswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv sw_nonadp 5

# sbatch -J fbondp -o fbondp.out -e fbondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook oth_nonadp 5
# sbatch -J rmondp -o rmondp.out -e rmondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random oth_nonadp 5
# sbatch -J rsondp -o rsondp.out -e rsondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos oth_nonadp 5
# sbatch -J eyondp -o eyondp.out -e eyondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye oth_nonadp 5
# sbatch -J rxondp -o rxondp.out -e rxondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv oth_nonadp 5

sbatch -J rxvbki10 -o rxvbki10.out -e rxvbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 10
sbatch -J rxvbki20 -o rxvbki20.out -e rxvbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 20
sbatch -J rxvbki40 -o rxvbki40.out -e rxvbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 40
sbatch -J rxvbki80 -o rxvbki80.out -e rxvbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 80
sbatch -J rxvbki12 -o rxvbki12.out -e rxvbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 120