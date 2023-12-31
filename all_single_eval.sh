!/bin/bash

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

# sbatch -J fbbki10 -o fbbki10.out -e fbbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 10
# sbatch -J fbbki20 -o fbbki20.out -e fbbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 20
# sbatch -J fbbki40 -o fbbki40.out -e fbbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 40
# sbatch -J fbbki80 -o fbbki80.out -e fbbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 80
# sbatch -J fbbki12 -o fbbki12.out -e fbbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 120

# sbatch -J rndbki10 -o rndbki10.out -e rndbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 10
# sbatch -J rndbki20 -o rndbki20.out -e rndbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 20
# sbatch -J rndbki40 -o rndbki40.out -e rndbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 40
# sbatch -J rndbki80 -o rndbki80.out -e rndbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 80
# sbatch -J rndbki12 -o rndbki12.out -e rndbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 120

# sbatch -J rdsbki10 -o rdsbki10.out -e rdsbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 10
# sbatch -J rdsbki20 -o rdsbki20.out -e rdsbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 20
# sbatch -J rdsbki40 -o rdsbki40.out -e rdsbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 40
# sbatch -J rdsbki80 -o rdsbki80.out -e rdsbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 80
# sbatch -J rdsbki12 -o rdsbki12.out -e rdsbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 120

# sbatch -J eyebki10 -o eyebki10.out -e eyebki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 10
# sbatch -J eyebki20 -o eyebki20.out -e eyebki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 20
# sbatch -J eyebki40 -o eyebki40.out -e eyebki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 40
# sbatch -J eyebki80 -o eyebki80.out -e eyebki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 80
# sbatch -J eyebki12 -o eyebki12.out -e eyebki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 120

# sbatch -J rxvbki10 -o rxvbki10.out -e rxvbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 10
# sbatch -J rxvbki20 -o rxvbki20.out -e rxvbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 20
# sbatch -J rxvbki40 -o rxvbki40.out -e rxvbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 40
# sbatch -J rxvbki80 -o rxvbki80.out -e rxvbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 80
# sbatch -J rxvbki12 -o rxvbki12.out -e rxvbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh arxiv bki_adp_Q 5 120

# sbatch -J w10bki10 -o w10bki10.out -e w10bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_10 bki_adp_Q 5 10
# sbatch -J w10bki20 -o w10bki20.out -e w10bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_10 bki_adp_Q 5 20
# sbatch -J w10bki40 -o w10bki40.out -e w10bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_10 bki_adp_Q 5 40
# sbatch -J w10bki80 -o w10bki80.out -e w10bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_10 bki_adp_Q 5 80
# sbatch -J w10bki12 -o w10bki12.out -e w10bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_10 bki_adp_Q 5 120

# sbatch -J w10bki10 -o w20bki10.out -e w20bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_20 bki_adp_Q 5 10
# sbatch -J w10bki20 -o w20bki20.out -e w20bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_20 bki_adp_Q 5 20
# sbatch -J w10bki40 -o w20bki40.out -e w20bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_20 bki_adp_Q 5 40
# sbatch -J w10bki80 -o w20bki80.out -e w20bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_20 bki_adp_Q 5 80
# sbatch -J w10bki12 -o w20bki12.out -e w20bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_20 bki_adp_Q 5 120

# sbatch -J w10bki10 -o w40bki10.out -e w40bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_40 bki_adp_Q 5 10
# sbatch -J w10bki20 -o w40bki20.out -e w40bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_40 bki_adp_Q 5 20
# sbatch -J w10bki40 -o w40bki40.out -e w40bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_40 bki_adp_Q 5 40
# sbatch -J w10bki80 -o w40bki80.out -e w40bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_40 bki_adp_Q 5 80
# sbatch -J w10bki12 -o w40bki12.out -e w40bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_40 bki_adp_Q 5 120

# sbatch -J w80bki10 -o w80bki10.out -e w80bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_80 bki_adp_Q 5 10
# sbatch -J w80bki20 -o w80bki20.out -e w80bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_80 bki_adp_Q 5 20
# sbatch -J w80bki40 -o w80bki40.out -e w80bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_80 bki_adp_Q 5 40
# sbatch -J w80bki80 -o w80bki80.out -e w80bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_80 bki_adp_Q 5 80
# sbatch -J w80bki12 -o w80bki12.out -e w80bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_80 bki_adp_Q 5 120

# sbatch -J w100bki10 -o w100bki10.out -e w100bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 bki_adp_Q 5 10
# sbatch -J w100bki20 -o w100bki20.out -e w100bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 bki_adp_Q 5 20
# sbatch -J w100bki40 -o w100bki40.out -e w100bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 bki_adp_Q 5 40
# sbatch -J w100bki80 -o w100bki80.out -e w100bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 bki_adp_Q 5 80
# sbatch -J w100bki12 -o w100bki12.out -e w100bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 bki_adp_Q 5 120

# sbatch -J w200bki10 -o w200bki10.out -e w200bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 bki_adp_Q 5 10
# sbatch -J w200bki20 -o w200bki20.out -e w200bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 bki_adp_Q 5 20
# sbatch -J w200bki40 -o w200bki40.out -e w200bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 bki_adp_Q 5 40
# sbatch -J w200bki80 -o w200bki80.out -e w200bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 bki_adp_Q 5 80
# sbatch -J w200bki12 -o w200bki12.out -e w200bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 bki_adp_Q 5 120

# sbatch -J w500bki10 -o w500bki10.out -e w500bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 bki_adp_Q 5 10
# sbatch -J w500bki20 -o w500bki20.out -e w500bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 bki_adp_Q 5 20
# sbatch -J w500bki40 -o w500bki40.out -e w500bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 bki_adp_Q 5 40
# sbatch -J w500bki80 -o w500bki80.out -e w500bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 bki_adp_Q 5 80
# sbatch -J w500bki12 -o w500bki12.out -e w500bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 bki_adp_Q 5 120

# sbatch -J w1000bki10 -o w1000bki10.out -e w1000bki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 bki_adp_Q 5 10
# sbatch -J w1000bki20 -o w1000bki20.out -e w1000bki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 bki_adp_Q 5 20
# sbatch -J w1000bki40 -o w1000bki40.out -e w1000bki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 bki_adp_Q 5 40
# sbatch -J w1000bki80 -o w1000bki80.out -e w1000bki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 bki_adp_Q 5 80
# sbatch -J w1000bki12 -o w1000bki12.out -e w1000bki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 bki_adp_Q 5 120

# sbatch -J eblbki10 -o eblbki10.out -e eblbki10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block bki_adp_Q 5 10
# sbatch -J eblbki20 -o eblbki20.out -e eblbki20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block bki_adp_Q 5 20
# sbatch -J eblbki40 -o eblbki40.out -e eblbki40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block bki_adp_Q 5 40
# sbatch -J eblbki80 -o eblbki80.out -e eblbki80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block bki_adp_Q 5 80
# sbatch -J eblbki12 -o eblbki12.out -e eblbki12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block bki_adp_Q 5 120

# sbatch -J eble310 -o eble310.out -e eble310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block e3 5 10
# sbatch -J eble320 -o eble320.out -e eble320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block e3 5 20
# sbatch -J eble340 -o eble340.out -e eble340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block e3 5 40
# sbatch -J eble380 -o eble380.out -e eble380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block e3 5 80
# sbatch -J eble312 -o eble312.out -e eble312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block e3 5 120

# sbatch -J fboadp -o fboadp.out -e fboadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook oth_adp 5
# sbatch -J rmoadp -o rmoadp.out -e rmoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random oth_adp 5
# sbatch -J rsoadp -o rsoadp.out -e rsoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos oth_adp 5
# sbatch -J eyoadp -o eyoadp.out -e eyoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye oth_adp 5
# sbatch -J rxoadp -o rxoadp.out -e rxoadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv oth_adp 5
# sbatch -J w1oadp -o w1oadp.out -e w1oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_10 oth_adp 5
# sbatch -J w2oadp -o w2oadp.out -e w2oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_20 oth_adp 5
# sbatch -J w4oadp -o w4oadp.out -e w4oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_40 oth_adp 5
# sbatch -J w8oadp -o w8oadp.out -e w8oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_80 oth_adp 5
# sbatch -J eboadp -o eboadp.out -e eboadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye_block oth_adp 5
# sbatch -J w10oadp -o w10oadp.out -e w10oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_100 oth_adp 5
# sbatch -J w20oadp -o w20oadp.out -e w20oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_200 oth_adp 5
# sbatch -J w50oadp -o w50oadp.out -e w50oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_500 oth_adp 5
# sbatch -J w100oadp -o w100oadp.out -e w100oadp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_1000 oth_adp 5

# sbatch -J fbswna -o fbswna.out -e fbswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook sw_nonadp 5
# sbatch -J rmswna -o rmswna.out -e rmswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random sw_nonadp 5
# sbatch -J rsswna -o rsswna.out -e rsswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos sw_nonadp 5
# sbatch -J eyswna -o eyswna.out -e eyswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye sw_nonadp 5
# sbatch -J rxswna -o rxswna.out -e rxswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv sw_nonadp 5
# sbatch -J w1swna -o w1swna.out -e w1swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_10 sw_nonadp 5
# sbatch -J w2swna -o w2swna.out -e w2swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_20 sw_nonadp 5
# sbatch -J w4swna -o w4swna.out -e w4swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_40 sw_nonadp 5
# sbatch -J w8swna -o w8swna.out -e w8swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_80 sw_nonadp 5
# sbatch -J ebswna -o ebswna.out -e ebswna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye_block sw_nonadp 5
# sbatch -J w10swna -o w10swna.out -e w10swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_100 sw_nonadp 5
# sbatch -J w20swna -o w20swna.out -e w20swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_200 sw_nonadp 5
# sbatch -J w50swna -o w50swna.out -e w50swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_500 sw_nonadp 5
# sbatch -J w100swna -o w100swna.out -e w100swna.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_1000 sw_nonadp 5

# sbatch -J fbondp -o fbondp.out -e fbondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook oth_nonadp 5
# sbatch -J rmondp -o rmondp.out -e rmondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random oth_nonadp 5
# sbatch -J rsondp -o rsondp.out -e rsondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos oth_nonadp 5
# sbatch -J eyondp -o eyondp.out -e eyondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye oth_nonadp 5
# sbatch -J rxondp -o rxondp.out -e rxondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv oth_nonadp 5
# sbatch -J w1ondp -o w1ondp.out -e w1ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_10 oth_nonadp 5
# sbatch -J w2ondp -o w2ondp.out -e w2ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_20 oth_nonadp 5
# sbatch -J w4ondp -o w4ondp.out -e w4ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_40 oth_nonadp 5
# sbatch -J w8ondp -o w8ondp.out -e w8ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_80 oth_nonadp 5
# sbatch -J ebondp -o ebondp.out -e ebondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye_block oth_nonadp 5

sbatch -J fbsegun -o fbsegun.out -e fbsegun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook segun 5
sbatch -J rmsegun -o rmsegun.out -e rmsegun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random segun 5
sbatch -J rssegun -o rssegun.out -e rssegun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos segun 5
sbatch -J eysegun -o eysegun.out -e eysegun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye segun 5
sbatch -J rxsegun -o rxsegun.out -e rxsegun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv segun 5
sbatch -J w1segun -o w1segun.out -e w1segun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_10 segun 5
sbatch -J w2segun -o w2segun.out -e w2segun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_20 segun 5
sbatch -J w4segun -o w4segun.out -e w4segun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_40 segun 5
sbatch -J w8segun -o w8segun.out -e w8segun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_80 segun 5
sbatch -J ebsegun -o ebsegun.out -e ebsegun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye_block segun 5

# sbatch -J fbsegfun -o fbsegfun.out -e fbsegfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook segfun 5
# sbatch -J rmsegfun -o rmsegfun.out -e rmsegfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random segfun 5
# sbatch -J rssegfun -o rssegfun.out -e rssegfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos segfun 5
# sbatch -J eysegfun -o eysegfun.out -e eysegfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye segfun 5
# sbatch -J rxsegfun -o rxsegfun.out -e rxsegfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv segfun 5
# sbatch -J w1segfun -o w1segfun.out -e w1segfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_10 segfun 5
# sbatch -J w2segfun -o w2segfun.out -e w2segfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_20 segfun 5
# sbatch -J w4segfun -o w4segfun.out -e w4segfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_40 segfun 5
# sbatch -J w8segfun -o w8segfun.out -e w8segfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_80 segfun 5
# sbatch -J ebsegfun -o ebsegfun.out -e ebsegfun.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye_block segfun 5

# sbatch -J fbsegqr -o fbsegqr.out -e fbsegqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook segqr 5
# sbatch -J rmsegqr -o rmsegqr.out -e rmsegqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random segqr 5
# sbatch -J rssegqr -o rssegqr.out -e rssegqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos segqr 5
# sbatch -J eysegqr -o eysegqr.out -e eysegqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye segqr 5
# sbatch -J rxsegqr -o rxsegqr.out -e rxsegqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv segqr 5
# sbatch -J w1segqr -o w1segqr.out -e w1segqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_10 segqr 5
# sbatch -J w2segqr -o w2segqr.out -e w2segqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_20 segqr 5
# sbatch -J w4segqr -o w4segqr.out -e w4segqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_40 segqr 5
# sbatch -J w8segqr -o w8segqr.out -e w8segqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_80 segqr 5
# sbatch -J ebsegqr -o ebsegqr.out -e ebsegqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye_block segqr 5

# sbatch -J fbsegfqr -o fbsegfqr.out -e fbsegfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh facebook segfqr 5
# sbatch -J rmsegfqr -o rmsegfqr.out -e rmsegfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh random segfqr 5
# sbatch -J rssegfqr -o rssegfqr.out -e rssegfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh erdos segfqr 5
# sbatch -J eysegfqr -o eysegfqr.out -e eysegfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye segfqr 5
# sbatch -J rxsegfqr -o rxsegfqr.out -e rxsegfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh arxiv segfqr 5
# sbatch -J w1segfqr -o w1segfqr.out -e w1segfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_10 segfqr 5
# sbatch -J w2segfqr -o w2segfqr.out -e w2segfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_20 segfqr 5
# sbatch -J w4segfqr -o w4segfqr.out -e w4segfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_40 segfqr 5
# sbatch -J w8segfqr -o w8segfqr.out -e w8segfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_80 segfqr 5
# sbatch -J ebsegfqr -o ebsegfqr.out -e ebsegfqr.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh eye_block segfqr 5

# sbatch -J w10ondp -o w10ondp.out -e w10ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_100 oth_nonadp 5
# sbatch -J w20ondp -o w20ondp.out -e w20ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_200 oth_nonadp 5
# sbatch -J w50ondp -o w50ondp.out -e w50ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_500 oth_nonadp 5
# sbatch -J w100ondp -o w100ondp.out -e w100ondp.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals.sh wishart_1000 oth_nonadp 5


# sbatch -J fbe310 -o fbe310.out -e fbe310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e3 5 10
# sbatch -J fbe320 -o fbe320.out -e fbe320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e3 5 20
# sbatch -J fbe340 -o fbe340.out -e fbe340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e3 5 40
# sbatch -J fbe380 -o fbe380.out -e fbe380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e3 5 80
# sbatch -J fbe312 -o fbe312.out -e fbe312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e3 5 120

# sbatch -J fbe410 -o fbe410.out -e fbe410.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e4 5 10
# sbatch -J fbe420 -o fbe420.out -e fbe420.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e4 5 20
# sbatch -J fbe440 -o fbe440.out -e fbe440.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e4 5 40
# sbatch -J fbe480 -o fbe480.out -e fbe480.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e4 5 80
# sbatch -J fbe412 -o fbe412.out -e fbe412.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook e4 5 120

# sbatch -J fbegun10 -o fbegun10.out -e fbegun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egun 5 10
# sbatch -J fbegun20 -o fbegun20.out -e fbegun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egun 5 20
# sbatch -J fbegun40 -o fbegun40.out -e fbegun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egun 5 40
# sbatch -J fbegun80 -o fbegun80.out -e fbegun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egun 5 80
# sbatch -J fbegun12 -o fbegun12.out -e fbegun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egun 5 120

# sbatch -J fbegfun10 -o fbegfun10.out -e fbegfun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfun 5 10
# sbatch -J fbegfun20 -o fbegfun20.out -e fbegfun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfun 5 20
# sbatch -J fbegfun40 -o fbegfun40.out -e fbegfun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfun 5 40
# sbatch -J fbegfun80 -o fbegfun80.out -e fbegfun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfun 5 80
# sbatch -J fbegfun12 -o fbegfun12.out -e fbegfun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfun 5 120

# sbatch -J fbegqr10 -o fbegqr10.out -e fbegqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egqr 5 10
# sbatch -J fbegqr20 -o fbegqr20.out -e fbegqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egqr 5 20
# sbatch -J fbegqr40 -o fbegqr40.out -e fbegqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egqr 5 40
# sbatch -J fbegqr80 -o fbegqr80.out -e fbegqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egqr 5 80
# sbatch -J fbegqr12 -o fbegqr12.out -e fbegqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egqr 5 120

# sbatch -J fbegfqr10 -o fbegfqr10.out -e fbegfqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfqr 5 10
# sbatch -J fbegfqr20 -o fbegfqr20.out -e fbegfqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfqr 5 20
# sbatch -J fbegfqr40 -o fbegfqr40.out -e fbegfqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfqr 5 40
# sbatch -J fbegfqr80 -o fbegfqr80.out -e fbegfqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfqr 5 80
# sbatch -J fbegfqr12 -o fbegfqr12.out -e fbegfqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook egfqr 5 120

# sbatch -J rde310 -o rde310.out -e rde310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e3 5 10
# sbatch -J rde320 -o rde320.out -e rde320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e3 5 20
# sbatch -J rde340 -o rde340.out -e rde340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e3 5 40
# sbatch -J rde380 -o rde380.out -e rde380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e3 5 80
# sbatch -J rde312 -o rde312.out -e rde312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e3 5 120

# sbatch -J rde410 -o rde410.out -e rde410.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e4 5 10
# sbatch -J rde420 -o rde420.out -e rde420.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e4 5 20
# sbatch -J rde440 -o rde440.out -e rde440.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e4 5 40
# sbatch -J rde480 -o rde480.out -e rde480.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e4 5 80
# sbatch -J rde412 -o rde412.out -e rde412.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos e4 5 120

# sbatch -J rdegun10 -o rdegun10.out -e rdegun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egun 5 10
# sbatch -J rdegun20 -o rdegun20.out -e rdegun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egun 5 20
# sbatch -J rdegun40 -o rdegun40.out -e rdegun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egun 5 40
# sbatch -J rdegun80 -o rdegun80.out -e rdegun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egun 5 80
# sbatch -J rdegun12 -o rdegun12.out -e rdegun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egun 5 120

# sbatch -J rdegfun10 -o rdegfun10.out -e rdegfun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfun 5 10
# sbatch -J rdegfun20 -o rdegfun20.out -e rdegfun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfun 5 20
# sbatch -J rdegfun40 -o rdegfun40.out -e rdegfun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfun 5 40
# sbatch -J rdegfun80 -o rdegfun80.out -e rdegfun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfun 5 80
# sbatch -J rdegfun12 -o rdegfun12.out -e rdegfun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfun 5 120

# sbatch -J rdegqr10 -o rdegqr10.out -e rdegqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egqr 5 10
# sbatch -J rdegqr20 -o rdegqr20.out -e rdegqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egqr 5 20
# sbatch -J rdegqr40 -o rdegqr40.out -e rdegqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egqr 5 40
# sbatch -J rdegqr80 -o rdegqr80.out -e rdegqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egqr 5 80
# sbatch -J rdegqr12 -o rdegqr12.out -e rdegqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egqr 5 120

# sbatch -J rdegfqr10 -o rdegfqr10.out -e rdegfqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfqr 5 10
# sbatch -J rdegfqr20 -o rdegfqr20.out -e rdegfqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfqr 5 20
# sbatch -J rdegfqr40 -o rdegfqr40.out -e rdegfqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfqr 5 40
# sbatch -J rdegfqr80 -o rdegfqr80.out -e rdegfqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfqr 5 80
# sbatch -J rdegfqr12 -o rdegfqr12.out -e rdegfqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos egfqr 5 120

# sbatch -J rne310 -o rne310.out -e rne310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e3 5 10
# sbatch -J rne320 -o rne320.out -e rne320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e3 5 20
# sbatch -J rne340 -o rne340.out -e rne340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e3 5 40
# sbatch -J rne380 -o rne380.out -e rne380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e3 5 80
# sbatch -J rne312 -o rne312.out -e rne312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e3 5 120

# sbatch -J rne410 -o rne410.out -e rne410.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e4 5 10
# sbatch -J rne420 -o rne420.out -e rne420.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e4 5 20
# sbatch -J rne440 -o rne440.out -e rne440.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e4 5 40
# sbatch -J rne480 -o rne480.out -e rne480.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e4 5 80
# sbatch -J rne412 -o rne412.out -e rne412.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random e4 5 120

# sbatch -J rnegun10 -o rnegun10.out -e rnegun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egun 5 10
# sbatch -J rnegun20 -o rnegun20.out -e rnegun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egun 5 20
# sbatch -J rnegun40 -o rnegun40.out -e rnegun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egun 5 40
# sbatch -J rnegun80 -o rnegun80.out -e rnegun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egun 5 80
# sbatch -J rnegun12 -o rnegun12.out -e rnegun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egun 5 120

# sbatch -J rnegfun10 -o rnegfun10.out -e rnegfun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfun 5 10
# sbatch -J rnegfun20 -o rnegfun20.out -e rnegfun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfun 5 20
# sbatch -J rnegfun40 -o rnegfun40.out -e rnegfun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfun 5 40
# sbatch -J rnegfun80 -o rnegfun80.out -e rnegfun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfun 5 80
# sbatch -J rnegfun12 -o rnegfun12.out -e rnegfun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfun 5 120

# sbatch -J rnegqr10 -o rnegqr10.out -e rnegqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egqr 5 10
# sbatch -J rnegqr20 -o rnegqr20.out -e rnegqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egqr 5 20
# sbatch -J rnegqr40 -o rnegqr40.out -e rnegqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egqr 5 40
# sbatch -J rnegqr80 -o rnegqr80.out -e rnegqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egqr 5 80
# sbatch -J rnegqr12 -o rnegqr12.out -e rnegqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egqr 5 120

# sbatch -J rnegfqr10 -o rnegfqr10.out -e rnegfqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfqr 5 10
# sbatch -J rnegfqr20 -o rnegfqr20.out -e rnegfqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfqr 5 20
# sbatch -J rnegfqr40 -o rnegfqr40.out -e rnegfqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfqr 5 40
# sbatch -J rnegfqr80 -o rnegfqr80.out -e rnegfqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfqr 5 80
# sbatch -J rnegfqr12 -o rnegfqr12.out -e rnegfqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random egfqr 5 120

# sbatch -J eye310 -o eye310.out -e eye310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e3 5 10
# sbatch -J eye320 -o eye320.out -e eye320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e3 5 20
# sbatch -J eye340 -o eye340.out -e eye340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e3 5 40
# sbatch -J eye380 -o eye380.out -e eye380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e3 5 80
# sbatch -J eye312 -o eye312.out -e eye312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e3 5 120

# sbatch -J eye410 -o eye410.out -e eye410.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e4 5 10
# sbatch -J eye420 -o eye420.out -e eye420.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e4 5 20
# sbatch -J eye440 -o eye440.out -e eye440.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e4 5 40
# sbatch -J eye480 -o eye480.out -e eye480.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e4 5 80
# sbatch -J eye412 -o eye412.out -e eye412.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye e4 5 120

# sbatch -J eyegun10 -o eyegun10.out -e eyegun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egun 5 10
# sbatch -J eyegun20 -o eyegun20.out -e eyegun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egun 5 20
# sbatch -J eyegun40 -o eyegun40.out -e eyegun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egun 5 40
# sbatch -J eyegun80 -o eyegun80.out -e eyegun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egun 5 80
# sbatch -J eyegun12 -o eyegun12.out -e eyegun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egun 5 120

# sbatch -J eyegfun10 -o eyegfun10.out -e eyegfun10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfun 5 10
# sbatch -J eyegfun20 -o eyegfun20.out -e eyegfun20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfun 5 20
# sbatch -J eyegfun40 -o eyegfun40.out -e eyegfun40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfun 5 40
# sbatch -J eyegfun80 -o eyegfun80.out -e eyegfun80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfun 5 80
# sbatch -J eyegfun12 -o eyegfun12.out -e eyegfun12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfun 5 120

# sbatch -J eyegqr10 -o eyegqr10.out -e eyegqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egqr 5 10
# sbatch -J eyegqr20 -o eyegqr20.out -e eyegqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egqr 5 20
# sbatch -J eyegqr40 -o eyegqr40.out -e eyegqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egqr 5 40
# sbatch -J eyegqr80 -o eyegqr80.out -e eyegqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egqr 5 80
# sbatch -J eyegqr12 -o eyegqr12.out -e eyegqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egqr 5 120

# sbatch -J eyegfqr10 -o eyegfqr10.out -e eyegfqr10.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfqr 5 10
# sbatch -J eyegfqr20 -o eyegfqr20.out -e eyegfqr20.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfqr 5 20
# sbatch -J eyegfqr40 -o eyegfqr40.out -e eyegfqr40.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfqr 5 40
# sbatch -J eyegfqr80 -o eyegfqr80.out -e eyegfqr80.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfqr 5 80
# sbatch -J eyegfqr12 -o eyegfqr12.out -e eyegfqr12.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye egfqr 5 120

# sbatch -J eybe310 -o eybe310.out -e eybe310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block e3 5 10
# sbatch -J eybe320 -o eybe320.out -e eybe320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block e3 5 20

# sbatch -J w1e310 -o w1e310.out -e w1e310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 e3 5 10
# sbatch -J w1e320 -o w1e320.out -e w1e320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 e3 5 20
# sbatch -J w1e340 -o w1e340.out -e w1e340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 e3 5 40
# sbatch -J w1e380 -o w1e380.out -e w1e380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 e3 5 80
# sbatch -J w1e312 -o w1e312.out -e w1e312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 e3 5 120

# sbatch -J w2e310 -o w2e310.out -e w2e310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 e3 5 10
# sbatch -J w2e320 -o w2e320.out -e w2e320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 e3 5 20
# sbatch -J w2e340 -o w2e340.out -e w2e340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 e3 5 40
# sbatch -J w2e380 -o w2e380.out -e w2e380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 e3 5 80
# sbatch -J w2e312 -o w2e312.out -e w2e312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 e3 5 120

# sbatch -J w5e310 -o w5e310.out -e w1e310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 e3 5 10
# sbatch -J w5e320 -o w5e320.out -e w1e320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 e3 5 20
# sbatch -J w5e340 -o w5e340.out -e w1e340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 e3 5 40
# sbatch -J w5e380 -o w5e380.out -e w1e380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 e3 5 80
# sbatch -J w5e312 -o w5e312.out -e w1e312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 e3 5 120

# sbatch -J wCe310 -o wCe310.out -e wCe310.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 e3 5 10
# sbatch -J wCe320 -o wCe320.out -e wCe320.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 e3 5 20
# sbatch -J wCe340 -o wCe340.out -e wCe340.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 e3 5 40
# sbatch -J wCe380 -o wCe380.out -e wCe380.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 e3 5 80
# sbatch -J wCe312 -o wCe312.out -e wCe312.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 e3 5 120

# sbatch -J fbbki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh facebook bki_adp_Q 5 1
# sbatch -J erbki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh erdos bki_adp_Q 5 1
# sbatch -J rnbki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh random bki_adp_Q 5 1
# sbatch -J w1bki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_100 bki_adp_Q 5 1
# sbatch -J w2bki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_200 bki_adp_Q 5 1
# sbatch -J w5bki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_500 bki_adp_Q 5 1
# sbatch -J wcbki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh wishart_1000 bki_adp_Q 5 1
# sbatch -J eybki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye bki_adp_Q 5 1
# sbatch -J ebbki1 -o fbbki1.out -e fbbki1.err --nodes 2 --cpus-per-task 12 -p longq --mem 32000 --time 07-07:00:00 single_evals_3.sh eye_block bki_adp_Q 5 1

