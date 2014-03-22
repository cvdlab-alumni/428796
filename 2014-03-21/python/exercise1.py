from pyplasm import *


#MODELLA IN 2D LA BASE DEL GRADINO PIU' ESTERNO

verts2 = [[-2,-2],[12,-2],[-2,10],[12,10]]
cells2 = [[1,2,3,4]]
pols2 = None
floor0 = MKPOL([verts2, cells2, pols2])
 


#MODELLA IN 2D LA BASE DEL GRADINO INTERMEDIO

verts1 = [[-1,-1],[11,-1],[-1,9],[11,9]]
cells1 = [[1,2,3,4]]
pols1 = None
base1 = MKPOL([verts1, cells1, pols1])


verts = [[0,0],[10,0],[0,8],[10,8]]
cells = [[1,2,3,4]]
pols = None
base = MKPOL([verts, cells, pols])


vertsMuroInt = [[1.5,1.5],[1.5,6.5],[8.5,6.5],[8.5,1.5]]
cellsMuroInt = [[1,2,3,4]]
polsMuroInt = None
muroInt = MKPOL([vertsMuroInt, cellsMuroInt, polsMuroInt])


baseTot = DIFFERENCE([floor0,(base1)])


vertsMuro = [[1,1],[1,7],[9,7],[9,1]]
cellsMuro = [[1,2,3,4]]
polsMuro = None
muro = MKPOL([vertsMuro, cellsMuro, polsMuro])

#MODELLA IN 2D L'AREA DELIMITATA DAL MURO INTERNO
baseMuro = DIFFERENCE([base, muro])
baseTot2 = STRUCT([COLOR([0.96,0.44,0.44])(baseTot), COLOR([0.95,0.96,0.63])(baseMuro),COLOR([0.82,0.96,0.64])(muroInt)])

#MODELLA IN 2D IL COMPLESSO (VISTO DALL'ALTO)
VIEW((baseTot2)) 
skel = STRUCT([floor0, base1, base, muroInt])
VIEW(SKELETON(1)(skel))


#VISUALIZZA I VARI PIANI IN VERSIONE TWO D AND AN HAlF
floor1 = T(3)(1)(base1)
floor2 = T(3)(2)(base)
floor3 = T(3)(6)(base)
floor4 = T(3)(9)(muroInt)
floorsTot = STRUCT([floor0, floor1, floor2, floor3, floor4])

VIEW((floorsTot))
VIEW(SKELETON(1)(floorsTot))
