## read the file 
````R
mt <-read.table("test_20210319102207.tab", sep ="\t", header=T, row.names =1)
mat <- as.matrix(mt)
tiff(file ="heatmap_orthologs.tiff")
 hp <- heatmap(mat, scale ="column")
 dev.off()
