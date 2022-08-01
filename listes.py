# RAPPELS PYTHON : Les listes

# Tuples, Dictionnaires, sets
# Tableaux, Arrays, Vecteurs
# collections

from audioop import reverse


# nom = "Toto"
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

ages = [20, 25, 15]
nb_noms = len(noms)

# amis = ["Emilie", "Marc"]
#noms.append("Emilie")
# noms.extend(amis)
# noms += amis
#del noms[1]

#Slice
# slice_noms = noms[1:] inclus et exclus
# slice_noms = noms[:3]

# Tris / Sort

# noms.sort()
# noms.sort(key=lambda element : len(element))
# noms_trie =sorted(noms)

# for element in noms_trie:
#     print(element)

# Operations

# print(min(ages))
# n = noms[0]
# noms[0]= noms[-1]
# noms[-1] = n
# print(noms)

# noms[0], noms[-1] = noms[-1], noms[0]
# print(noms)

# tous_les_noms = " - ".join(noms)
# print(tous_les_noms)


# Compréhensions de listes
# len_noms = []
# for nom in noms:
#     len_noms.append(len(nom))

len_noms = [len(nom) if len(nom) > 3 else 0 for nom in noms]

print(len_noms)


