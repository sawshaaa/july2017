from Bio import SeqIO
from Bio.Seq import Seq

##importing the file with the codon/protein letter corresponding info##
s = open("/share/data/genetic-code.txt")
D = {}
info = s.readlines()
for i in info:
  x = i.split()
  D[x[0]] = x[1]

##reading the actual gene given and separating it into readable codons##
gene = list(SeqIO.parse("/share/data/ALDH2.fa" ,"fasta"))
v = list(gene[0].seq)
v[1605] = 'A'
y = Seq("".join(v))

print y.translate()

 
 
#for i in range(0,len(gene),3):
#  print gene[i:i+3] +  "  " +  D[gene[i:i+3]]
