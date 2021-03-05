# Scritp to find repeats
## The workflow :
```bash
  #1step
#name option is the name given to the database that will be created in the folder data
#dir is the durectory containing fasta sequence to use to creat the database
mkdir data

perl /usr/local/RepeatModeler-open-1.0.11/BuildDatabase -name data/foam13  foa_M13_clean.fasta


#2steps
#this steps aims to build repeat models using the created database and using the ncbi search engine

perl /usr/local/RepeatModeler-open-1.0.11/RepeatModeler -database data/foam13 -pa 54
#this step will create two file families.fa nd families.stk in the data dir



#3step
# in this step we will run the masking of the genome using our custom library created in the step before s means sensitive dir is the output dir
mkdir out
perl /usr/local/RepeatMasker/RepeatMasker -pa 50 -s -lib data/foam13-families.fa -dir out/ foa_M13_clean.fasta
