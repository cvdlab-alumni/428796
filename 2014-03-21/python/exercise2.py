from pyplasm import *


x_muroNorth = QUOTE([8])
y_muroNorth = QUOTE([0])
xy_muroNorth = INSR(PROD)([x_muroNorth,y_muroNorth,QUOTE([4]) ])
muroNorth = T([1,2,3])([1,7,2])(xy_muroNorth)

x_muroSouth= QUOTE([8])
y_muroSouth = QUOTE([0.00001])
xy_muroSouth = INSR(PROD)([x_muroSouth,y_muroSouth,QUOTE([4]) ])
muroSouth = T([1,2,3])([1,1,2])(xy_muroSouth)

entrance = CUBOID([2,0.00001,4])
entranceT = T([1,2,3])([4,1,2])(entrance)

muroentrance = DIFFERENCE([muroSouth, entranceT])


x_muroEast= QUOTE([0])
y_muroEast = QUOTE([6])
xy_muroEast = INSR(PROD)([x_muroEast,y_muroEast,QUOTE([4]) ])
muroEast = T([1,2,3])([1,1,2])(xy_muroEast)

x_muroWest= QUOTE([0])
y_muroWest = QUOTE([6])
xy_muroWest = INSR(PROD)([x_muroWest,y_muroWest,QUOTE([4]) ])
muroWest = T([1,2,3])([9,1,2])(xy_muroWest)


x_muroNorthUp = QUOTE([7])
y_muroNorthUp = QUOTE([0])
xy_muroNorthUp = INSR(PROD)([x_muroNorthUp,y_muroNorthUp,QUOTE([1.5]) ])
muroNorthUp = T([1,2,3])([1.5,6.5,7])(xy_muroNorthUp)

x_muroSouthUp= QUOTE([7])
y_muroSouthUp = QUOTE([0])
xy_muroSouthUp = INSR(PROD)([x_muroSouthUp,y_muroSouthUp,QUOTE([1.5]) ])
muroSouthUp = T([1,2,3])([1.5,1.5,7])(xy_muroSouthUp)

x_muroEastUp= QUOTE([0])
y_muroEastUp = QUOTE([5])
xy_muroEastUp = INSR(PROD)([x_muroEastUp,y_muroEastUp,QUOTE([1.5]) ])
muroEastUp = T([1,2,3])([1.5,1.5,7])(xy_muroEastUp)

x_muroWestUp= QUOTE([0])
y_muroWestUp = QUOTE([5])
xy_muroWestUp = INSR(PROD)([x_muroWestUp,y_muroWestUp,QUOTE([1.5]) ])
muroWestUp = T([1,2,3])([8.5,1.5,7])(xy_muroWestUp)

wallsUp = STRUCT([muroWestUp, muroEastUp, muroNorthUp, muroSouthUp])
wallsDown = STRUCT([muroNorth,muroentrance, muroEast, muroWest])
walls = STRUCT([wallsUp, wallsDown])
VIEW(walls)


#PASSO A "2D AND HALF MODEL"

verts2 = [[-2,-2],[12,-2],[-2,10],[12,10]]
cells2 = [[1,2,3,4]]
pols2 = None
floor0 = MKPOL([verts2, cells2, pols2])

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


floor1 = T(3)(1)(base1)
floor2 = T(3)(2)(base)
floor3 = T(3)(6)(base)
floor4 = T(3)(8)(muroInt)
floorsTot = STRUCT([floor0, floor1, floor2, floor3, floor4, walls])



VIEW(SKELETON(1)(floorsTot))
VIEW((floorsTot))