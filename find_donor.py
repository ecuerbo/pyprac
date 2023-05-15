dna=input('Enter DNA sequence: ')
pos = dna.find("gt", 0) #position of the donor splice site

while pos>-1:
    print('Donor splice site candidate at position %d'%pos)
    pos=dna('gt', pos+1)