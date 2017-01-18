#data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

data = open("/Users/krishna/Downloads/rosalind_dna.txt").read()


A_count = 0
C_count = 0
G_count = 0
T_count = 0
for i in data:
	if i == 'A':
		A_count += 1
	if i == 'C':
		C_count += 1
	if i == 'G':
		G_count += 1
	if i == 'T':
		T_count += 1

print A_count, C_count, G_count, T_count
