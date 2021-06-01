## Workflow used to perform PanGenome analysis using anvio pipeline

### parse gbk files using this pythoin code 
````python
#!/usr/bin/env python

import sys, argparse
import pandas as pd
from Bio import SeqIO
tabout = open("tabbedout", 'w')
tabout.write("GeneID\tType\tScaffold\tStart\tEnd\tStrand\tProduct\taa_sequence\n")

gb_file = "FOA_foa44.gbk"
for record in SeqIO.parse(open(gb_file,"r"), "genbank") :
    for f in record.features:
        if f.type == 'CDS':
                                                                chr = record.id
                                                                ID = f.qualifiers['locus_tag'][0]
                                                                try:
                                                                        product = f.qualifiers['product'][0]
                                                                except KeyError:
                                                                        product = "hypothetical protein"
                                                                start = f.location.nofuzzy_start + 1
                                                                end = f.location.nofuzzy_end
                                                                strand = f.location.strand
                                                                if strand == 1:
                                                                        strand = '+'
                                                                elif strand == -1:
                                                                        strand = '-'
                                                                aa_seq = f.qualifiers ['translation'][0]
                                                                tabout.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (ID, 'CDS', chr, str(start), str(end), strand, product, aa_seq))
````

                                                                
                                                                

### From gbk folder, run anvi-script-process-genbank to generate files for anvi-gen-genome-storage
```` bash
mkdir anvioFiles
for file in gbk/*.gbk

do 
  string=$(basename ${file%%.*})
  anvi-script-process-genbank -i $file -O anvioFiles/$string
done

FOA_foa44
Num GenBank entries processed ................: 51
Num gene records found .......................: 20,416
Num genes reported ...........................: 6,325
Num genes with functions .....................: 97

FASTA file path ..............................: anvioFiles/FOA_foa44-contigs.fa
External gene calls file .....................: anvioFiles/FOA_foa44-external-gene-calls.txt
TAB-delimited functions ......................: anvioFiles/FOA_foa44-external-functions.txt

* Mmmmm ☘

GCA_000149955
Num GenBank entries processed ................: 88
Num gene records found .......................: 27,347
Num genes reported ...........................: 7,445
Num genes with functions .....................: 631

FASTA file path ..............................: anvioFiles/GCA_000149955-contigs.fa
External gene calls file .....................: anvioFiles/GCA_000149955-external-gene-calls.txt
TAB-delimited functions ......................: anvioFiles/GCA_000149955-external-functions.txt

* Mmmmm ☘

GCA_000259975
Num GenBank entries processed ................: 388
Num gene records found .......................: 24,733
Num genes reported ...........................: 6,465
Num genes with functions .....................: 591

FASTA file path ..............................: anvioFiles/GCA_000259975-contigs.fa
External gene calls file .....................: anvioFiles/GCA_000259975-external-gene-calls.txt
TAB-delimited functions ......................: anvioFiles/GCA_000259975-external-functions.txt

* Mmmmm ☘

GCA_000260075
Num GenBank entries processed ................: 472
Num gene records found .......................: 26,378
Num genes reported ...........................: 6,817
Num genes with functions .....................: 633

FASTA file path ..............................: anvioFiles/GCA_000260075-contigs.fa
External gene calls file .....................: anvioFiles/GCA_000260075-external-gene-calls.txt
TAB-delimited functions ......................: anvioFiles/GCA_000260075-external-functions.txt

* Mmmmm ☘
.
.
.
````

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
