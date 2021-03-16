## Phibase screen
# Build phibase db using makeblastdb
````bash
#Remove any/all non-ascii chars
cat phi-base_current.fas | perl -ne 's/[^\x00-\x7F]+/ /g; print;' > tmp.fasta
# creat blast database 
makeblastdb -in tmp.fasta -dbtype prot -out db/phibase

# blast proteins vs the database 
blastp -query proteins.fa -db db/phibase -max_target_seqs 1 -evalue 0.00001\
-num_threads 36 -outfmt '6 delim=@ qaccver saccver pident length qlen slen evalue qcovs ' > Foa44_vs_phibase_blastp
