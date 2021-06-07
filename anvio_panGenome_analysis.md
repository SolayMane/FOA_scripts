## Workflow used to perform PanGenome analysis using anvio pipeline

### parse gbk files using this python script gb2tabAnvio
````bash    
for file in gbk/*.gbk
do python2.7 gb2tabAnvio.py -i $file -o ${file%%.*}.txt
done 

In the file gbk/FOA_foa44.gbk, we found 51 contig/scaffold with 20416 genes
In the file gbk/GCA_000149955.2_ASM14995v2_genomic.gbk, we found 88 contig/scaffold with 27347 genes
In the file gbk/GCA_000259975.2_FO_MN25_V1_genomic.gbk, we found 388 contig/scaffold with 24733 genes
In the file gbk/GCA_000260075.2_FO_HDV247_V1_genomic.gbk, we found 472 contig/scaffold with 26378 genes
In the file gbk/GCA_000260155.3_FO_CL57_V1_genomic.gbk, we found 418 contig/scaffold with 24739 genes
In the file gbk/GCA_000260175.2_FO_Cotton_V1_genomic.gbk, we found 985 contig/scaffold with 25216 genes
In the file gbk/GCA_000260195.2_FO_II5_V1_genomic.gbk, we found 418 contig/scaffold with 22487 genes
In the file gbk/GCA_000260215.2_FO_PHW808_V1_genomic.gbk, we found 2552 contig/scaffold with 26246 genes
In the file gbk/GCA_000260235.2_FO_PHW815_V1_genomic.gbk, we found 1218 contig/scaffold with 25666 genes
In the file gbk/GCA_000260495.2_FO_melonis_V1_genomic.gbk, we found 1146 contig/scaffold with 26719 genes
In the file gbk/GCA_000350345.1_Foc1_1.0_genomic.gbk, we found 1341 contig/scaffold with 15438 genes
In the file gbk/GCA_000350365.1_Foc4_1.0_genomic.gbk, we found 840 contig/scaffold with 14459 genes
In the file gbk/GCA_001702695.2_ASM170269v2_genomic.gbk, we found 33 contig/scaffold with 17168 genes
In the file gbk/GCA_003615075.1_FoC_A23_v1_genomic.gbk, we found 1997 contig/scaffold with 18530 genes
In the file gbk/GCA_003615085.1_FoC_Fus2_v1_genomic.gbk, we found 34 contig/scaffold with 19342 genes
In the file gbk/GCA_003615095.1_FoC_125_v1_genomic.gbk, we found 2119 contig/scaffold with 18720 genes
In the file gbk/GCA_004141715.1_FoN_N139_v1_genomic.gbk, we found 4349 contig/scaffold with 20668 genes
In the file gbk/GCA_005930515.1_ASM593051v1_genomic.gbk, we found 12 contig/scaffold with 16784 genes
In the file gbk/GCA_007994515.1_ASM799451v1_genomic.gbk, we found 15 contig/scaffold with 17022 genes

mv gbk/*.txt anvioFiles # mv all external-gene-call txt files to the folder anvioFile that contains the contigs
````
### Generate a new anvi'o contigs database for each genome

````bash
mkdir anvioDB

for file in anvioFiles/*.txt

do 
  string=$(basename ${file%%.*})
  anvi-gen-contigs-database  \
  -f ${file%%.*}-contigs.fa \
  -T 36 \
  -o anvioDB/${string}.db \
  -n FOPan \
  --external-gene-calls $file \
  --ignore-internal-stop-codons \
  --skip-predict-frame
done
````


### Create a new anvi'o anvi-gen-genomes-storage 
#### --external-genomes FILE_PATH preparation 

````bash
echo -e 'name\tcontigs_db_path' > external_genomes.txt

ls anvioDB/| while read file
  do
    name=$(basename ${file%%.*})
    
    echo -e "$name\t$(pwd)/anvioDB/$file" >> external_genomes.txt
 done
```` 
#### Generating an anvi’o genomes storage
```bash
anvi-gen-genomes-storage -e external_genomes.txt -o FO-GENOMES.db
````
### Run pangenome pipeline
````bash

anvi-pan-genome \
-g FO-GENOMES.db \
-n FOPanGenome \
--num-threads 36 \
--use-ncbi-blast \
--mcl-inflation 10 \
--minbit 0.5 \
--output-dir FO_pangenomics
````
