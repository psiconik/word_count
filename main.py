# Zak Alexandre Kiraly
# 12 sept 2023
# TP1

#fonction comptage du nombre de mots
def nombre_mots(chaine):
   mots = chaine.split()
   compte = len(mots)
   return compte

#fonction interactive
count_word = input('que voulez-vous me dire?')
compte_final = nombre_mots(count_word)
print('vous avez',compte_final,'mots')
