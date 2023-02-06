N=4
(
for file in "./"/*; do
   ((i=i%N)); ((i++==0)) && wait
    /work/williarj/2223_balancing_selection/slimexe "$file" &
done
)

