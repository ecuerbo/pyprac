#!/opt/anaconda3/bin/python

dna = input('Enter DNA sequence: ')

if 'n' in dna or 'N' in dna:
    nbases=dna.count('n')+dna.count('N')
    total_nuc = len(dna)
    print("dna sequence has %d undefined bases " %nbases)
    print('There are %d bases in the dna' %total_nuc)
else:
    print("dna sequence has no undefined bases")