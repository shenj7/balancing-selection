COUNT=1000 # number of scripts we want to generate
dir="test_batch_one"
sd="test_batch_one_stats"
seed=0
ml=0.0000001 # 10-6 to 10-8
mr=0.0000002 
cl=0.001 # 10-2 10-4
cr=0.002
rl=0.0000001 # same as mutation rate
rr=0.0000002
pl=1000 # 1e3 5e3 1e4
pr=2000
sz=10




for d in "${h[@]}"
do
    python3 full_pipeline_script/full_pipeline.py \
    -d $dir -n $COUNT -s $seed -sd $sd -sz $sz\
    -cl $cl -cr $cr -ml $ml -mr $mr -rl $rl -rr $rr -pl $pl -pr $pr

done
