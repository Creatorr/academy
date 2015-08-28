import string

def DNA_strand(dna):
    dna_dict = string.maketrans("ATGC","TACG")
    return dna.translate(dna_dict)

print(DNA_strand("ATTGC"))
