## Workflow used to perform PanGenome analysis using anvio pipeline
### From gbk folder, run anvi-script-process-genbank to generate files for anvi-gen-genome-storage
```` bash
mkdir anvioFiles
for file in gbk/*.gbk

do 
  string=$(basename ${file%%.*})
  echo $string
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

### To continue in preparing the dataset for PanGenome analysis, we should create a new anvi'o contig database givig for each genome its gene model

````bash
mkdir anvioDB

for file in anvioFiles/*contigs.fa

do 
  projectName=$(basename ${file%%-*})

  anvi-gen-contigs-database -f $file -n $projectName -T 36 -o anvioDB/${projectName}.db --external-gene-calls anvioFiles/${projectName}-external-gene-calls.txt --ignore-internal-stop-codons --skip-predict-frame
  
done




### Create a new anvi'o anvi-gen-genomes-storage 
````bash
echo -e 'name\tbin_id\tcollection_id\tprofile_db_path\tcontigs_db_path' > external_genomes.txt
bin=0
ls anvioFiles/*contigs.fa | while read file
  do
    name=$(basename ${file%%-*})
    bin=`expr $bin + 1`
    
    
    echo -e "$name\tBin_id_$bin\tCollection_A\t/disk1/FOA/anvio/$file" >> external_genomes.txt
 done


