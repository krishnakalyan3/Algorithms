# Convert DNA to RNA (Replace all T by U)
# RNA to Protein (Based on the codon table)

import protein as pro

#data = open("/Users/krishna/Downloads/rosalind_rna.txt").read()
data = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

protein = []
for i in xrange(0,len(data), 3):
	if len(data[i:i+3]) > 2:
			protein.append(pro.RNA_TABLE[data[i:i+3]])

print ''.join(protein)