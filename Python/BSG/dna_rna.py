# Usually we convert DNA to RNA
# 'A', 'C', 'G', and 'U'
# RNA string is formed by replacing all occurrences of 'T' in tt with 'U' in uu.

data = open("/Users/krishna/Downloads/rosalind_rna.txt").read()

rna_data = []
for i in data:
	if i == 'T':
		rna_data.append('U')
	else:
		rna_data.append(i)

print ''.join(rna_data)