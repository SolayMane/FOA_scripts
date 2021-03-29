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
mat <-t(table)


# we need to verify thath the tip names in the tree are the same as the rownames
#this function will print any tip/rows differents between the two vectors
# if you have the output "character(0)" it's Ok you can go on the plote
setdiff(tree$tip.label,colnames(mat))


#columns names of Ttable should be exaclty the same as the names of the branches in the tree
# creat an image file 
tiff("heatmap.tiff", width = 3000, height = 2048, units = "px", res=200)

# plot the tree with a heatmap of orthogroups
phylo.heatmap(tree, mat, labels=F, col = c("white","MediumSpringGreen"))
dev.off()

