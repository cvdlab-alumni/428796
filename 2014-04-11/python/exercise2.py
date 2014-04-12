from pyplasm import *

#FACCIATE ESTERNE INFERIORI

x_wallNorth = QUOTE([8])
y_wallNorth = QUOTE([0.5])
xy_wallNorth = INSR(PROD)([x_wallNorth,y_wallNorth,QUOTE([3]) ])
wallNorth = T([1,2,3])([5,10.5,3])(xy_wallNorth)

x_wallSouth = QUOTE([8])
y_wallSouth = QUOTE([0.5])
xy_wallSouth = INSR(PROD)([x_wallSouth,y_wallSouth,QUOTE([3]) ])
wallSouth = T([1,2,3])([5,5,3])(xy_wallSouth)

entrance = CUBOID([2,0.5,4])
entranceT = T([1,2,3])([8,5,3])(entrance)

wallentrance = DIFFERENCE([wallSouth, entranceT])


x_wallWest= QUOTE([0.5])
y_wallWest = QUOTE([6])
xy_wallWest = INSR(PROD)([x_wallWest,y_wallWest,QUOTE([3]) ])
wallWest = T([1,2,3])([5,5,3])(xy_wallWest)

x_wallEast= QUOTE([0.5])
y_wallEast = QUOTE([6])
xy_wallEast = INSR(PROD)([x_wallEast,y_wallEast,QUOTE([3]) ])
wallEast = T([1,2,3])([12.5,5,3])(xy_wallEast)

wallsDown = STRUCT([wallNorth,wallentrance, wallEast, wallWest])

#FACCIATE ESTERNE SUPERIORI

x_wallNorthUp = QUOTE([7])
y_wallNorthUp = QUOTE([0.2])
xy_wallNorthUp = INSR(PROD)([x_wallNorthUp,y_wallNorthUp,QUOTE([2]) ])
wallNorthUp = T([1,2,3])([5.5,10.5,6.5])(xy_wallNorthUp)

x_wallSouthUp= QUOTE([7])
y_wallSouthUp = QUOTE([0.2])
xy_wallSouthUp = INSR(PROD)([x_wallSouthUp,y_wallSouthUp,QUOTE([2]) ])
wallSouthUp = T([1,2,3])([5.5,5.5,6.5])(xy_wallSouthUp)

x_wallEastUp= QUOTE([0.2])
y_wallEastUp = QUOTE([5])
xy_wallEastUp = INSR(PROD)([x_wallEastUp,y_wallEastUp,QUOTE([2]) ])
wallEastUp = T([1,2,3])([5.5,5.5,6.5])(xy_wallEastUp)

x_wallWestUp= QUOTE([0.2])
y_wallWestUp = QUOTE([5.2])
xy_wallWestUp = INSR(PROD)([x_wallWestUp,y_wallWestUp,QUOTE([2]) ])
wallWestUp = T([1,2,3])([12.5,5.5,6.5])(xy_wallWestUp)


wallsUp = STRUCT([wallWestUp, wallEastUp, wallNorthUp, wallSouthUp])
VIEW(COLOR([1,0.937,0.835])((STRUCT([wallsUp,wallsDown]))))



