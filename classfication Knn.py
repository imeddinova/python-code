from math import sqrt

table = [['Homme',28,32],['Homme',33,35],['Femme',27,33],['Femme',31,36]] #--------Latable--------#

x = int(input('Tapez la Taille :')) #--------test = [28,34]--------#
y = int(input('Tapez la Hanche :')) #--------test = [28,34]--------#

k = int(input('Tapez la valeur de K :')) #--------La val de K--------#
while (k > len(table)) :
	k = int(input('Tapez la valeur de K :'))

table1 = []
rang = 1
for i in table :
	dist = sqrt((x-i[1])**2 + (y-i[2])**2) 
	table1 = table1 + [(i[0],dist)]
table2 = sorted(table1, key=lambda i: i[1]) #--------Calculer les distances--------#

i = 0
mal = 0
fem = 0

while (i<k) :
	a = table2[i]
	if (a[0] == 'Femme') : #--------La somme des voisins de Female--------#
		fem += 1
	else :				   #---------La somme des voisins de Male---------#	
		mal += 1
	i += 1

if (mal>fem) :			  #---------L'Affichage'---------#	
	print('Le genre est : Male')  
else :
	print('Le genre est : Female')







	
