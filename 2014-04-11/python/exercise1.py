from pyplasm import *


#BASE
verts0 = [[-2,-2],[12,-2],[-2,10],[12,10]]
cells0 = [[1,2,3,4]]
pols0 = None
floor0 = MKPOL([verts0, cells0, pols0])
 
#GRADINO INTERMEDIO
verts1 = [[-1,-1],[11,-1],[-1,9],[11,9]]
cells1 = [[1,2,3,4]]
pols1 = None
floor1 = MKPOL([verts1, cells1, pols1])

#ULTIMO GRADINO
verts2 = [[0,0],[10,0],[0,8],[10,8]]
cells2 = [[1,2,3,4]]
pols2 = None
floor2 = MKPOL([verts2, cells2, pols2])

#TETTO LARGO
vertsRoof0 = [[0,0],[10,0],[0,8],[10,8]]
cellsRoof0 = [[1,2,3,4]]
polsRoof0 = None
roof0 = MKPOL([vertsRoof0, cellsRoof0, polsRoof0])

#TETTO STRETTO
vertsRoof1 = [[1.5,1.5],[1.5,6.5],[8.5,6.5],[8.5,1.5]]
cellsRoof1 = [[1,2,3,4]]
polsRoof1 = None
roof1 = MKPOL([vertsRoof1, cellsRoof1, polsRoof1])

#Traslazione e solidificazione piani e tetti
floor0Solid = PROD([floor0,Q(1)])
floor0SolidTrasl = T([1,2])([4,4])(floor0Solid)

floor1Solid = PROD([floor1,Q(1)])
floor1SolidTrasl = T([1,2,3])([4,4,1])(floor1Solid)


floor2Solid = PROD([floor2,Q(1)])
floor2SolidTrasl = T([1,2,3])([4,4,2])(floor2Solid)


roof0Solid = PROD([roof0,Q(0.5)])
roof0SolidTrasl = T([1,2,3])([4,4,6])(roof0Solid)

roof1Solid = PROD([roof1,Q(0.5)])
roof1SolidTrasl = T([1,2,3])([4,4,7.5])(roof1Solid)


allFloors = STRUCT([floor0SolidTrasl,floor1SolidTrasl,floor2SolidTrasl,roof1SolidTrasl,roof0SolidTrasl])


#COLONNATO INTERNO
columnPro = CYLINDER([0.3,3])(24)

columnWestInt1 = T([1,2,3])([11,6,3])(columnPro)
columnWestInt2 = T([1,2,3])([11,7,3])(columnPro)
columnWestInt3 = T([1,2,3])([11,8,3])(columnPro)
columnWestInt4 = T([1,2,3])([11,9,3])(columnPro)
columnWestInt5 = T([1,2,3])([11,10,3])(columnPro)


columnEastInt1 = T([1,2,3])([7,6,3])(columnPro)
columnEastInt2 = T([1,2,3])([7,7,3])(columnPro)
columnEastInt3 = T([1,2,3])([7,8,3])(columnPro)
columnEastInt4 = T([1,2,3])([7,9,3])(columnPro)
columnEastInt5 = T([1,2,3])([7,10,3])(columnPro)

allColumnInt = STRUCT([columnEastInt3,columnEastInt4,columnEastInt5,columnEastInt1,columnEastInt2,columnWestInt1,columnWestInt2,columnWestInt3,columnWestInt4, columnWestInt5])


#COLONNATO ESTERNO
columnWestExt1 = T([1,2,3])([4.5,4.5,3])(columnPro)
columnWestExt2 = T([1,2,3])([4.5,5.5,3])(columnPro)
columnWestExt3 = T([1,2,3])([4.5,6.5,3])(columnPro)
columnWestExt4 = T([1,2,3])([4.5,7.5,3])(columnPro)
columnWestExt5 = T([1,2,3])([4.5,8.5,3])(columnPro)
columnWestExt6 = T([1,2,3])([4.5,9.5,3])(columnPro)
columnWestExt7 = T([1,2,3])([4.5,10.5,3])(columnPro)
columnWestExt8 = T([1,2,3])([4.5,11.5,3])(columnPro)

allColumnWestExt = (STRUCT([columnWestExt1,columnWestExt2,columnWestExt3,columnWestExt4,columnWestExt5,columnWestExt6,columnWestExt7,columnWestExt8]))


columnEastExt1 = T([1,2,3])([13.5,4.5,3])(columnPro)
columnEastExt2 = T([1,2,3])([13.5,5.5,3])(columnPro)
columnEastExt3 = T([1,2,3])([13.5,6.5,3])(columnPro)
columnEastExt4 = T([1,2,3])([13.5,7.5,3])(columnPro)
columnEastExt5 = T([1,2,3])([13.5,8.5,3])(columnPro)
columnEastExt6 = T([1,2,3])([13.5,9.5,3])(columnPro)
columnEastExt7 = T([1,2,3])([13.5,10.5,3])(columnPro)
columnEastExt8 = T([1,2,3])([13.5,11.5,3])(columnPro)

allColumnEastExt = (STRUCT([columnEastExt1,columnEastExt2,columnEastExt3,columnEastExt4,columnEastExt5,columnEastExt6,columnEastExt7,columnEastExt8]))


columnNorthExt1 = T([1,2,3])([5.5,4.5,3])(columnPro)
columnNorthExt2 = T([1,2,3])([6.5,4.5,3])(columnPro)
columnNorthExt3 = T([1,2,3])([7.5,4.5,3])(columnPro)
columnNorthExt4 = T([1,2,3])([8.5,4.5,3])(columnPro)
columnNorthExt5 = T([1,2,3])([9.5,4.5,3])(columnPro)
columnNorthExt6 = T([1,2,3])([10.5,4.5,3])(columnPro)
columnNorthExt7 = T([1,2,3])([11.5,4.5,3])(columnPro)
columnNorthExt8 = T([1,2,3])([12.5,4.5,3])(columnPro)

allColumnNorthExt = (STRUCT([columnNorthExt1,columnNorthExt2,columnNorthExt3,columnNorthExt4,columnNorthExt5,columnNorthExt6,columnNorthExt7,columnNorthExt8]))

columnSouthExt1 = T([1,2,3])([5.5,11.5,3])(columnPro)
columnSouthExt2 = T([1,2,3])([6.5,11.5,3])(columnPro)
columnSouthExt3 = T([1,2,3])([7.5,11.5,3])(columnPro)
columnSouthExt4 = T([1,2,3])([8.5,11.5,3])(columnPro)
columnSouthExt5 = T([1,2,3])([9.5,11.5,3])(columnPro)
columnSouthExt6 = T([1,2,3])([10.5,11.5,3])(columnPro)
columnSouthExt7 = T([1,2,3])([11.5,11.5,3])(columnPro)
columnSouthExt8 = T([1,2,3])([12.5,11.5,3])(columnPro)

allColumnSouthExt = STRUCT([columnSouthExt1,columnSouthExt3,columnSouthExt4,columnSouthExt5,columnSouthExt6,columnSouthExt7,columnSouthExt2,columnSouthExt8])


allColumnExt = STRUCT ([allColumnSouthExt, allColumnNorthExt, allColumnEastExt, allColumnWestExt])



allElements = STRUCT([COLOR([1,0.937,0.835])(allColumnExt), COLOR([1,0.937,0.835])(allFloors), COLOR([1,0.937,0.835])(allColumnInt) ])

#VISTA 3D TOTALE 
VIEW(SKELETON(1)(allElements))
VIEW(allElements)

