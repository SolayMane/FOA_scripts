# Gene & Repeat densities
## This script describehow to analyse the gene/repetas density within Foa genome sequence

```bash
#we need to have the genome indexed bwa index, using makewwindows in bdetools we will creat the winodows throuhg the genome

samtools faidx genome.fa

bedtools makewindows -g /sanhome2/data/annotation/m13annotation2/annotate_results/genome.fa.fai -w 50000 -s 10000 -i winnum > window_50k.bed

# now we will count the number of gene and ifere densities within the windows using the ggf file
bedtools coverage -b /sanhome2/data/annotation/m13annotation2/annotate_results/genome.gff3 -a window_50k.bed  > gdens_windows_50k.tab
