

data = open("/Users/krishna/Downloads/rosalind_revc.txt").read()

comp = []
for i in data:
	if i == 'A':
		comp.append('T')
	if i =='T':
		comp.append('A')
	if i == 'G':
		comp.append('C')
	if i =='C':
		comp.append('G')

print ''.join(comp)