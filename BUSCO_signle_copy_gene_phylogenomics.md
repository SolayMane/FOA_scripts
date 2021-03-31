
## Prepare your genomes to include in the analysis
````bash
mkdir data
cp *.fasta data/



## Run busco on every genome sequence

#!/bin/bash

for file in data/*.fasta
do
        output=$(basename ${file%%.*})


        busco -i $file -l sordariomycetes_odb10 -o $output -m genome --out_path out --cpu 36

done

### now we need to copy all the busc runs into a new directory "inputD"

mkdir inputD

find out/ -type d -name "run_*" | while read path
do
        new_name=$(basename ${path%/*})
        cp -r $path inputD/run_${new_name}
done


# now, we will run a python script that retriece all the single copy busco sahred genes and perform signle genes alignement, trimming concatenation and phylogenetic treee inference


<a href="https://github.com/jamiemcg/BUSCO_phylogenomics/blob/master/BUSCO_phylogenomics.py">BUSCO_phylogenomics.py</a> 


