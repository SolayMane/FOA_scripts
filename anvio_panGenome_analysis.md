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
