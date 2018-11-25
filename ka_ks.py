from Bio import SeqIO
import re
import sys
import subprocess



# Parse protein sequences from fasta file (PEP)
filinPEP = sys.argv[1]
dataPEP = SeqIO.parse(filinPEP,"fasta")
PEP = {}

for record in dataPEP :
	# Retrieve gene name
	m = re.search(r'gene:(\S*)\s+transcript:(\S*)\s+', record.description)
	gene = m.group(1)
	isoform = m.group(2)

	#print("gene : " + gene + ", isoform : " + isoform)

	l = len(record.seq)
	# If gene is not in dictionnary ==> store it
	if gene not in PEP:
		PEP[isoform] = [record.seq, gene, l]

	# If gene already in dictionnay ==> keep the record with the longest sequence
	else:
		if l > PEP[isoform][2]:
			PEP[isoform] = [record.seq, gene, l]



# Parse DNA sequences from fasta file (CDS)
filinCDS = sys.argv[2]
dataCDS = SeqIO.parse(filinCDS,"fasta")
CDS = {}

for record in dataCDS :
	# Retrieve gene name
	m = re.search(r'gene:(\S*)\s+', record.description)
	gene = m.group(1)

	#print("gene : " + gene)

	l = len(record.seq)
	# If gene is not in dictionnary ==> store it
	if gene not in CDS:
		CDS[gene] = [record.seq, l]

	# If gene already in dictionnay ==> keep the record with the longest sequence
	else:
		if l > CDS[gene][1]:
			CDS[gene] = [record.seq, l]



# Create couple from same family and calculate Ka/ks
filinFam = open(sys.argv[3], 'r')
filinFam.readline()
i = 0
li = []

for gene in filinFam :
	name = gene.split()[0]
	family = gene.split()[1]

	# If different family / 1st line ==> create new list
	if family != i or family == 0 :
		li = []
		i = family

	# If same family ==> calcultate ka/ks
	else :
		# Make pairs with other gens already in list
		for gen in li :
			# Create temporary files
			print(name, gen)
			print(PEP[name][0], PEP[gen][0])
			print(CDS[PEP[name][1]][0], CDS[PEP[name][1]][0])
			# Run PAML
			# subprocess.run("... > test.nt")
			
	# Add to list
	li.append(name)


# young and nelson 2000
