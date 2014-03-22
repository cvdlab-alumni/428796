from pyplasm import *

#COLONNATO
circleBase = CYLINDER([0.3,3.8])(24)


X_circleBaseTrasl1 = T([1,2,3])([0.5,1.5,2])(circleBase)
X_circleBaseTrasl2 = T([1,2,3])([0.5,2.5,2])(circleBase)
X_circleBaseTrasl3 = T([1,2,3])([0.5,3.5,2])(circleBase)
X_circleBaseTrasl4 = T([1,2,3])([0.5,4.5,2])(circleBase)
X_circleBaseTrasl5 = T([1,2,3])([0.5,5.5,2])(circleBase)
X_circleBaseTrasl6 = T([1,2,3])([0.5,6.5,2])(circleBase)
X_circleBaseTrasl7 = T([1,2,3])([0.5,7.5,2])(circleBase)

X_circleBaseTrasl21 = T([1,2,3])([9.5,1.5,2])(circleBase)
X_circleBaseTrasl22 = T([1,2,3])([9.5,2.5,2])(circleBase)
X_circleBaseTrasl23 = T([1,2,3])([9.5,3.5,2])(circleBase)
X_circleBaseTrasl24 = T([1,2,3])([9.5,4.5,2])(circleBase)
X_circleBaseTrasl25 = T([1,2,3])([9.5,5.5,2])(circleBase)
X_circleBaseTrasl26 = T([1,2,3])([9.5,6.5,2])(circleBase)
X_circleBaseTrasl27 = T([1,2,3])([9.5,7.5,2])(circleBase)

Y_circleBaseTrasl1 = T([1,2,3])([0.5,0.5,2])(circleBase)
Y_circleBaseTrasl2 = T([1,2,3])([1.5,0.5,2])(circleBase)
Y_circleBaseTrasl3 = T([1,2,3])([2.5,0.5,2])(circleBase)
Y_circleBaseTrasl4 = T([1,2,3])([3.5,0.5,2])(circleBase)
Y_circleBaseTrasl5 = T([1,2,3])([4.5,0.5,2])(circleBase)
Y_circleBaseTrasl6 = T([1,2,3])([5.5,0.5,2])(circleBase)
Y_circleBaseTrasl7 = T([1,2,3])([6.5,0.5,2])(circleBase)
Y_circleBaseTrasl8 = T([1,2,3])([7.5,0.5,2])(circleBase)
Y_circleBaseTrasl9 = T([1,2,3])([8.5,0.5,2])(circleBase)
Y_circleBaseTrasl10 = T([1,2,3])([9.5,0.5,2])(circleBase)

Y_circleBaseTrasl21 = T([1,2,3])([0.5,7.5,2])(circleBase)
Y_circleBaseTrasl22 = T([1,2,3])([1.5,7.5,2])(circleBase)
Y_circleBaseTrasl23 = T([1,2,3])([2.5,7.5,2])(circleBase)
Y_circleBaseTrasl24 = T([1,2,3])([3.5,7.5,2])(circleBase)
Y_circleBaseTrasl25 = T([1,2,3])([4.5,7.5,2])(circleBase)
Y_circleBaseTrasl26 = T([1,2,3])([5.5,7.5,2])(circleBase)
Y_circleBaseTrasl27 = T([1,2,3])([6.5,7.5,2])(circleBase)
Y_circleBaseTrasl28 = T([1,2,3])([7.5,7.5,2])(circleBase)
Y_circleBaseTrasl29 = T([1,2,3])([8.5,7.5,2])(circleBase)
Y_circleBaseTrasl210 = T([1,2,3])([9.5,7.5,2])(circleBase)


Y_circleBaseTot1 = STRUCT([X_circleBaseTrasl1,X_circleBaseTrasl2,X_circleBaseTrasl3,X_circleBaseTrasl4,X_circleBaseTrasl5,X_circleBaseTrasl6,X_circleBaseTrasl7])
Y_circleBaseTot2 = STRUCT([X_circleBaseTrasl21,X_circleBaseTrasl22,X_circleBaseTrasl23,X_circleBaseTrasl24,X_circleBaseTrasl25,X_circleBaseTrasl26,X_circleBaseTrasl27])
X_circleBaseTot2 = STRUCT([Y_circleBaseTrasl21,Y_circleBaseTrasl22,Y_circleBaseTrasl23,Y_circleBaseTrasl24,Y_circleBaseTrasl25,Y_circleBaseTrasl26,Y_circleBaseTrasl27,Y_circleBaseTrasl28,Y_circleBaseTrasl29,Y_circleBaseTrasl210])
X_circleBaseTot1 = STRUCT([Y_circleBaseTrasl1,Y_circleBaseTrasl2,Y_circleBaseTrasl3,Y_circleBaseTrasl4,Y_circleBaseTrasl5,Y_circleBaseTrasl6,Y_circleBaseTrasl7,Y_circleBaseTrasl8,Y_circleBaseTrasl9,Y_circleBaseTrasl10])
X_Y_circleBaseTot = STRUCT([Y_circleBaseTot1, X_circleBaseTot1, Y_circleBaseTot2, X_circleBaseTot2])



#WALLS

x_muroNorth = QUOTE([8])
y_muroNorth = QUOTE([0.2])
xy_muroNorth = INSR(PROD)([x_muroNorth,y_muroNorth,QUOTE([4]) ])
muroNorth = T([1,2,3])([1,7,2])(xy_muroNorth)

x_muroSouth= QUOTE([8])
y_muroSouth = QUOTE([0.2])
xy_muroSouth = INSR(PROD)([x_muroSouth,y_muroSouth,QUOTE([4]) ])
muroSouth = T([1,2,3])([1,1,2])(xy_muroSouth)

entrance = CUBOID([2,0.2,4])
entranceT = T([1,2,3])([4,1,2])(entrance)

muroentrance = DIFFERENCE([muroSouth, entranceT])

x_muroEast= QUOTE([0.2])
y_muroEast = QUOTE([6])
xy_muroEast = INSR(PROD)([x_muroEast,y_muroEast,QUOTE([4]) ])
muroEast = T([1,2,3])([1,1,2])(xy_muroEast)

x_muroWest= QUOTE([0.2])
y_muroWest = QUOTE([6])
xy_muroWest = INSR(PROD)([x_muroWest,y_muroWest,QUOTE([4]) ])
muroWest = T([1,2,3])([9,1,2])(xy_muroWest)



x_muroNorthUp = QUOTE([7])
y_muroNorthUp = QUOTE([0.1])
xy_muroNorthUp = INSR(PROD)([x_muroNorthUp,y_muroNorthUp,QUOTE([1.5]) ])
muroNorthUp = T([1,2,3])([1.5,6.5,7])(xy_muroNorthUp)

x_muroSouthUp= QUOTE([7])
y_muroSouthUp = QUOTE([0.1])
xy_muroSouthUp = INSR(PROD)([x_muroSouthUp,y_muroSouthUp,QUOTE([1.5]) ])
muroSouthUp = T([1,2,3])([1.5,1.5,7])(xy_muroSouthUp)

x_muroEastUp= QUOTE([0.1])
y_muroEastUp = QUOTE([5])
xy_muroEastUp = INSR(PROD)([x_muroEastUp,y_muroEastUp,QUOTE([1.5]) ])
muroEastUp = T([1,2,3])([1.5,1.5,7])(xy_muroEastUp)

x_muroWestUp= QUOTE([0.1])
y_muroWestUp = QUOTE([5])
xy_muroWestUp = INSR(PROD)([x_muroWestUp,y_muroWestUp,QUOTE([1.5]) ])
muroWestUp = T([1,2,3])([8.5,1.5,7])(xy_muroWestUp)

#DECORAZIONE FREGIO
x_muroNorthFregio = QUOTE([7])
y_muroNorthFregio = QUOTE([0.1])
xy_muroNorthFregio = INSR(PROD)([x_muroNorthFregio,y_muroNorthFregio,QUOTE([0.5]) ])
muroNorthFregio = T([1,2,3])([1.5,6.5,8])(xy_muroNorthFregio)

x_muroSouthFregio= QUOTE([7])
y_muroSouthFregio = QUOTE([0.1])
xy_muroSouthFregio = INSR(PROD)([x_muroSouthFregio,y_muroSouthFregio,QUOTE([0.5]) ])
muroSouthFregio = T([1,2,3])([1.5,1.5,8])(xy_muroSouthFregio)

x_muroEastFregio= QUOTE([0.1])
y_muroEastFregio = QUOTE([5])
xy_muroEastFregio = INSR(PROD)([x_muroEastFregio,y_muroEastFregio,QUOTE([0.5]) ])
muroEastFregio = T([1,2,3])([1.5,1.5,8])(xy_muroEastFregio)

x_muroWestFregio= QUOTE([0.1])
y_muroWestFregio = QUOTE([5])
xy_muroWestFregio = INSR(PROD)([x_muroWestFregio,y_muroWestFregio,QUOTE([0.5]) ])
muroWestFregio = T([1,2,3])([8.5,1.5,8])(xy_muroWestFregio)

#WALLS
wallsFregio = STRUCT([muroSouthFregio, muroNorthFregio, muroEastFregio, muroWestFregio])
wallsUp = STRUCT([muroWestUp, muroEastUp, muroNorthUp, muroSouthUp])
wallsDown = STRUCT([muroNorth,muroentrance, muroEast, muroWest])



verts2 = [[-2,-2],[12,-2],[-2,10],[12,10]]
cells2 = [[1,2,3,4]]
pols2 = None
floor0 = MKPOL([verts2, cells2, pols2])
floor03D = PROD([floor0,Q(-1)])

verts1 = [[-1,-1],[11,-1],[-1,9],[11,9]]
cells1 = [[1,2,3,4]]
pols1 = None
base1 = MKPOL([verts1, cells1, pols1])
base13D = PROD([base1,Q(-1)])


verts = [[0,0],[10,0],[0,8],[10,8]]
cells = [[1,2,3,4]]
pols = None
base = MKPOL([verts, cells, pols])
base3Dbottom = PROD([base,Q(-1)])
base3Dup = PROD([base,Q(1.5)])


vertsMuroInt = [[1.5,1.5],[1.5,6.5],[8.5,6.5],[8.5,1.5]]
cellsMuroInt = [[1,2,3,4]]
polsMuroInt = None
muroInt = MKPOL([vertsMuroInt, cellsMuroInt, polsMuroInt])



#VETRI TETTO
vertsT = [[0,0],[2,0.5],[4,0]]
cellsT = [[1,2,3]]
polsT = None
tri = MKPOL([vertsT, cellsT, polsT])
tri3D = PROD([tri,Q(1.8)])
tri3Drot = R([3,2])(-PI/2)(tri3D)
tri3Drotagain = R([1,2])(PI/2)(tri3Drot)

tri3Dtra1 =T([1,2,3])([2,2,8])(tri3Drotagain)
tri3Dtra2 =T([1,2,3])([4,2,8])(tri3Drotagain)
tri3Dtra3 =T([1,2,3])([6,2,8])(tri3Drotagain)

vetri3D = STRUCT([tri3Dtra1,tri3Dtra2,tri3Dtra3])


#FINAL BUILDING
floor1 = T(3)(1)(base13D)
floor2 = T(3)(2)(base3Dbottom)
floor3 = T(3)(5.5)(base3Dup)
floor4 = T(3)(8)(muroInt)
floorsTot = STRUCT([floor03D, floor1, floor2, floor3, floor4, COLOR([0.68,0.7,0.71]) (wallsDown),wallsUp, COLOR([0.77,0.94,0.96])(vetri3D),COLOR([0.71,0.91,0.91])(wallsFregio)])
building = STRUCT([floorsTot, X_Y_circleBaseTot])

VIEW(building)
VIEW(SKELETON(1)(building))


