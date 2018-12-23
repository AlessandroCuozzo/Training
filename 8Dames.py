#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# ==================================
# 8 Dames 
# ==================================

"""
Solution to the 8 queens problem

# https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_huit_dames
# https://en.wikipedia.org/wiki/Eight_queens_puzzle

# The script works! But we must expect a lot of Maximum Recursion Depth Exceeded ... X.X => The probability of randomly placing the 8 queens correctly is so low that you have to be lucky to do it without exceeding the limit of recursion of python ^^ '
# In fact, the number of possible combination is limited so if you place the first queen in a wrong case, the game is already lost.
# We can reduce this problem by using a chessboard with fewer squares (minimum 5), and number of queens = number of squares, or put fewer queens

# Le Script fonctionne ! Mais il faut s'attendre à bcp de Maximum Recursion Depth Exceeded... X.X => La probabilité de placer au hasard les 8 dames correctement est tellement faible qu'il faut avoir de la chance pour le faire sans dépasser la limite de recursion de python ^^'
# En fait, le nombre de combinaisons possibles est limité, donc si vous placez la première reine dans un mauvais cas, la partie est déjà perdue.
# On peut diminuer ce problème en utilisant un échiquier avec moins de cases (minimum 5), et nombre de dames=nombres de cases, ou alors mettre moins de dames

copyright (c) 2018 Alessandro Cuozzo

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""


from random import choice # on peut aussi faire import random et utiliser la fonction random.randint(1,8) à la place de choice(cases)
from numpy import roll,array,zeros
from pylab import imshow

cases=[1,2,3,4,5,6,7,8]
Dames=[]

def huit_Dames(n): # n=le nombre de dames qu'il reste à ajouter dans la liste

	colonne=choice(cases)
	ligne=choice(cases)
	new_dame=(colonne,ligne) # new_dame est un tuple correspondant aux coordonnées de la nouvelle dame sur l'échiquier

	if len(Dames)==0:
		Dames.append(new_dame)
		return huit_Dames(n-1)

	elif n==0:
		return Dames

	else:
		for dame in Dames:
			if colonne==dame[0] or ligne==dame[1] or abs(colonne-dame[0])==abs(ligne-dame[1]): # si même colonne ou même ligne ou même diagonale
				return huit_Dames(n)
		Dames.append(new_dame) # => si le for a été épuisé, ça veut dire que c'est OK => la nouvelle dame ne menace pas/n'est pas menacée par une des autres dames
		return huit_Dames(n-1)

huit_Dames(8)
print("")

############# 
# Affichage #
#############

M = zeros((8,8))
vector = array([0.,100.]*4)
for i in range(8):
    if i%2!=0:
        M[i]=roll(vector,1)
    else:
        M[i] = vector
    
D=0 
for dame in Dames:
    column = dame[0]
    row = dame[1]
    M[row-1,column-1] = 50
    D+=1
    print("============= Dame",D,"=============")
    #print("       colonne",column-1,"/","ligne",row-1)
    print("       ligne",row-1,"/","colonne",column-1)
    print("")
    imshow(M)
