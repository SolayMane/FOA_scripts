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



### To continue in preparing the dataset for PanGenome analysis, we should create a new anvi'o contig database assigning for each genome its gene model

````bash
mkdir anvioDB

for file in anvioFiles/*contigs.fa

do 
  projectName=$(basename ${file%%-*})

  anvi-gen-contigs-database -f $file -n $projectName -T 36 -o anvioDB/${projectName}.db --external-gene-calls anvioFiles/${projectName}-external-gene-calls.txt --ignore-internal-stop-codons --skip-predict-frame
  
done
````
###



### Create a new anvi'o anvi-gen-genomes-storage 
#### --external-genomes FILE_PATH preparation 
````bash
echo -e 'name\tbin_id\tcollection_id\tprofile_db_path\tcontigs_db_path' > external_genomes.txt
bin=0
ls anvioFiles/*contigs.fa | while read file
  do
    name=$(basename ${file%%-*})
    bin=`expr $bin + 1`
    
    
    echo -e "$name\tBin_id_$bin\tCollection_A\t/disk1/FOA/anvio/$file" >> external_genomes.txt
 done
````
#### --internal-genomes FILE_PATH preparation
````bash
cp external_genomes.txt internal_genomes.txt

cat internal_genomes.txt

name    bin_id  collection_id   profile_db_path contigs_db_path
FOA_foa44       Bin_id_1        Collection_A    /disk1/FOA/anvio/anvioFiles/FOA_foa44-contigs.fa
GCA_000149955   Bin_id_2        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000149955-contigs.fa
GCA_000259975   Bin_id_3        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000259975-contigs.fa
GCA_000260075   Bin_id_4        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000260075-contigs.fa
GCA_000260155   Bin_id_5        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000260155-contigs.fa
GCA_000260175   Bin_id_6        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000260175-contigs.fa
GCA_000260195   Bin_id_7        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000260195-contigs.fa
GCA_000260215   Bin_id_8        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000260215-contigs.fa
GCA_000260235   Bin_id_9        Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000260235-contigs.fa
GCA_000260495   Bin_id_10       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000260495-contigs.fa
GCA_000350345   Bin_id_11       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000350345-contigs.fa
GCA_000350365   Bin_id_12       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_000350365-contigs.fa
GCA_001702695   Bin_id_13       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_001702695-contigs.fa
GCA_003615075   Bin_id_14       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_003615075-contigs.fa
GCA_003615085   Bin_id_15       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_003615085-contigs.fa
GCA_003615095   Bin_id_16       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_003615095-contigs.fa
GCA_004141715   Bin_id_17       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_004141715-contigs.fa
GCA_005930515   Bin_id_18       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_005930515-contigs.fa
GCA_007994515   Bin_id_19       Collection_A    /disk1/FOA/anvio/anvioFiles/GCA_007994515-contigs.fa

sed -i 's/anvioFiles/anvioDB/g' internal_genomes.txt # to modify the file path by replacing the folders
sed -i 's/-contigs.fa/.db/g' internal_genomes.txt # to modify the extension of the database files from -contigs.fa to .db

````
####Generating an anvi’o genomes storage
