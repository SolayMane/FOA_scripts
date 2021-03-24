# Orthofinder orthogroups presence/absence martic combined to species tree
## we will converte the file Orthogroups.GeneCount.tsv to 0/1 matrix using excel if function
## The species tree from orthofinder results folder will be used toghtehr with the 0/1 matrix from orthogroups
````R

# we nedd to set the working directory that containing the above mentioned files
setwd("C:/Users/workstation_bioinfo/Desktop/R/PangenomeFoa")

#install phytools package
install.package("phytools")

#load phytools library
library(phytools)

#load the files
table <-read.table("orthogroups_0_1.txt", sep ="\t", header =T, row.names=1)
tree<-read.tree("SpeciesTree_rooted.txt")

#
#we need to transpose our table
tTable <-t(table)

#columns names of Ttable should be exaclty the same as the names of the branches in the tree
# creat an image file 
tiff("heatmap.tiff", width = 2000, height = 768, units = "px", res=100)

# plot the tree with a heatmap of orthogroups


