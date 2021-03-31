
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

* [busco_phylogenomics.py](https://www.python.org/)




genome="$1"
#ORG="$2"
outname=$(basename ${genome%.*})

busco \
  -o ${outname} \
  -i ${genome} \
  -l /sanhome2/data/BUSCO/sordariomycetes_odb10 \
  -m ${MODE} \
  -c 16 \
  -f


##############
###RENAMING###
##############


#this script is aiming to rename predicetd genes by busco using the target species

# to find folders with predicted genes in every busco run



for dir in $(find . -type d -name "single_copy_busco_sequences")

do
        sppname=$(basename "${dir%/run_*}")

        for gene in $dir/*.faa
        do
        #       chr=$(cat $gene | grep "^>" | awk -F" " '{ print $1 }' | sed 's/>//g')
#               echo $chr
                cat $gene | awk -F":" '/^>/ { print "ZZZZ" } /[^>]/ { print $0}' | sed '/^>/d' | sed 's/ZZZZ/>'$sppname'/g' > ${gene%.*}.fan
        done
done


#######################################################
###IDENTIFYING IDs OF SHARED GENES WITHIN 17 GENOMES###
#######################################################
#seletc all complete busco ids
for file in $(find . -type f -name "full_table.tsv")
do
        grep -v "^#" ${file} | awk '$2=="Complete" {print $1}' >> complete_busco_ids.tsv
done

# sort and count ids
cat complete_busco_ids.tsv | sort | uniq -c > complete_buscoID_count.txt


#select only busco id shared by the 69 species
awk '$1 > 12 {print $2}' complete_buscoID_count.txt > final_busco.txt

##########################
###COPYING SHARED GENES###
##########################

# this script aims to copy each shared gene from all busco run and make multifasta for
 each gene

mkdir sharedfaa
rm sharedfaa/*
# this for loop is to ietrate around gene ids

for gene in $(cat final_busco.txt)
do

#this for loop aims to iterate around run busco directories for the gene id select in
precedente loop and to store the sequences in one file
        for dir in $(find . -type d -name "single_copy_busco_sequences")
        do
                cat $dir/${gene}.fan >> sharedfaa/${gene}.fa
        done
done

