#!/bin/bash

fasta_file=Solanum_tuberosum.SolTub_3.0.pep.all.fa
filtered=filtered.fasta
blastp=blastp_result.txt

# ============================== #
# Keep only 1 isoform per gene
# ============================== #
python3 ./filter_isoforms.py $fasta_file


# ================================================================================== #
# Make database with fasta file of sequences of Vitis Vinifera (1 isoform per gene)
# ================================================================================== #
makeblastdb -in $filtered -dbtype prot


# ========================================================================================= #
# Run blastp on previously created database and fasta file of sequences of Vitis Vinifera
# -evalue : threshold for saving hits
# -matrix : name of the scoring matrix to use (default BLOSUM62)
# -num_threads : nb of threads to use during the search
# -out : name of the file to write the output
# -outfmt : format of the output
# ========================================================================================= #
blastp -query $filtered -db $filtered -out $blastp -outfmt "6 qseqid sseqid pident qlen length mismatch gapopen evalue bitscore qstart qend" -num_threads 8

import itertools

v=list()
stuff = [1, 2, 3]
for L in range(0, len(stuff)+1):
	for subset in itertools.combinations(stuff, L):
		print(subset)
		if len(subset) != 2:
			print("NO")
		else:
			v.append(subset)

			

print (v)

import itertools
v=list()
s=[1,2,3]
for L in range(1,len(s)+1):
	for sub in itertools.combinations(s,L):
		
		if len(sub) != 2 :
			print("NO")
		else :
			v.append(sub)
print(v)