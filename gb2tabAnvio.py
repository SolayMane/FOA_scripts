#!/usr/bin/env python

import sys, argparse
from Bio import SeqIO

class MyFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def __init__(self,prog):
        super(MyFormatter,self).__init__(prog,max_help_position=48)

parser=argparse.ArgumentParser(prog='gb2tabAnvio.py', usage="%(prog)s [options] -i genbank -o tab_gene_output",
    description='''Genbank to tab file for gene caller to feed anvio pipeline''',
    epilog="""Written by Slimane Khayi (2021) slimane.khayi@inra.ma""",
    formatter_class = MyFormatter)

parser.add_argument('-i','--input', required=True, help='GenBank genome file')
parser.add_argument('-o','--out', required=True, help='Name of output basename file')
args=parser.parse_args()

tabout = open(args.out, 'w')

#gene_callers_id        contig  start   stop    direction       partial call_type       source  version Translation
tabout.write("gene_callers_id\tcontig\tstart\tstop\tdirection\tpartial\tcall_type\tsource\tversion\taa_sequence\n")

gb_file = args.input

contig = 0 # we create the first gene id thal will correspond to the ordrg of the genes
for record in SeqIO.parse(open(gb_file,"r"), "genbank") : ###parsing gbk file by reading it
    for f in record.features: # we are ietrating thorugh the  features in the recordes
        if f.type == 'CDS': # when the recorde features type if CDS we will retrieve qualifiers
            chr = record.id
            ID = f.qualifiers['locus_tag'][0]
            if ID != "":
                contig += 1 # increment the number of the genes to be assigned as gene id
            elif ID == "":
                contig = 1

            try:
                product = f.qualifiers['product'][0]
            except KeyError:
                product = "hypothetical protein"
            start = f.location.nofuzzy_start + 1
            end = f.location.nofuzzy_end
            strand = f.location.strand
            if strand == 1:
                strand = 'f'
            elif strand == -1:
                strand = 'r'
            partial = '0'
            call_type = '1'
            source = 'prodigal'
            version = 'v2.6.3'
            aa_seq = f.qualifiers ['translation'][0]
            tabout.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (contig, chr, str(start), str(end), strand, partial, call_type, source, version, aa_seq))
