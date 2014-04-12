from pyplasm import *

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

wallsDown = (STRUCT([wallNorth,wallentrance, wallEast, wallWest]))

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


wallsUp =(STRUCT([wallWestUp, wallEastUp, wallNorthUp, wallSouthUp]))




#VETRI TETTO
vertsT = [[0,0],[2,0.5],[4,0]]
cellsT = [[1,2,3]]
polsT = None
tri = MKPOL([vertsT, cellsT, polsT])
tri3D = PROD([tri,Q(1.8)])
tri3Drot = R([3,2])(-PI/2)(tri3D)
tri3Drotagain = R([1,2])(PI/2)(tri3Drot)

tri3Dtra1 =T([1,2,3])([6.2,6,8])(tri3Drotagain)
tri3Dtra2 =T([1,2,3])([8.2,6,8])(tri3Drotagain)
tri3Dtra3 =T([1,2,3])([10.2,6,8])(tri3Drotagain)

vetri3D =STRUCT([tri3Dtra1,tri3Dtra2,tri3Dtra3])

#ROTATORIA E PRATO CIRCOSTANTI LINCOLN MEMORIAL
round1 = CYLINDER([22,0.1])(320)
round2 = CYLINDER([20,0.1])(320)
roundAbout = DIFFERENCE([round1,round2])
roundAboutTrasl = T([1,2])([9,9])(roundAbout)

#EDIFICI LATERALI A FORMA DI CROCE
halfCross1 = CUBOID([4,2,2])
halfCross2 = CUBOID([4,2,2])
halfCross2R = R([1,2])(PI/2)(halfCross2)
halfCross2T = T([1,2])([3,-1])(halfCross2R)
cross =  (STRUCT([halfCross1,halfCross2T]))
cross1 = T([1,2])([-25,-10])(R([1,2])(PI/4)(cross))
cross2 = T([1,2])([39,-10])(R([1,2])(PI/4)(cross))

#EDIFICI LATO OVEST
westBuilding1 = T([1,2])([-26,-59])(CUBOID([1,4,1]))
westBuilding3 = T([1,2])([-29,-60])(CUBOID([3,1,1]))
westBuilding4 = T([1,2])([-33,-55])(CUBOID([3,1,1]))
westBuilding6 = T([1,2])([-33,-60])(CUBOID([3,1,1]))
westBuilding7 = T([1,2])([-34,-59])(CUBOID([1,4,1]))

westBuilding2 = T([1,2])([-28,-48])(CUBOID([1,1,1]))
westBuilding5 = T([1,2])([-30,-46])(CUBOID([2,2,1]))

westBlock = STRUCT([westBuilding1,westBuilding7,westBuilding6,westBuilding5,westBuilding4,westBuilding3,westBuilding2])
westBuldingDodecaedro = T([1,2])([-25,-70])(CYLINDER([2,2])(12))

moreBuildings = STRUCT([cross1, cross2, westBuldingDodecaedro, westBlock])

#LAGO "REFLECTION LAKE"
reflectionLake = T([1,2])([5,-130])(CUBOID([10,100,0.1]))

#PRATO
bigLawn = T([1,2])([-60,-150])(CUBOID([150,250,0.1]))

#ALBERI
trunk = CYLINDER([0.2,2])(36)
foliagePro = SPHERE(0.5)([36,36])
foliage = STRUCT([T([1,3])([-0.2,2])(foliagePro), T([1,3])([0.2,2])(foliagePro), T([3])([2.2])(foliagePro)])

tree1 = T([1,2])([0,0])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree2 = T([1,2])([0,2])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree3 = T([1,2])([0,4])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree4 = T([1,2])([2,0])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree5 = T([1,2])([2,2])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree6 = T([1,2])([2,4])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree7 = T([1,2])([4,0])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree8 = T([1,2])([4,2])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))
tree9 = T([1,2])([4,4])(STRUCT([COLOR([0.5882,0.2941,0])(trunk),COLOR([0.502,0.502,0])(foliage)]))

trees =  STRUCT([tree1,tree2,tree3,tree4,tree5,tree6,tree7,tree8,tree9])

wood = STRUCT([T([1,2])([7,15])(trees),T([1,2])([-5,0])(trees),T([1,2])([-5,10])(trees),T([1,2])([20,0])(trees),T([1,2])([20,10])(trees)])

lakeTreeEast = STRUCT([T([1,2])([16,-30])(tree1),T([1,2])([16,-33])(tree1),T([1,2])([16,-36])(tree1),T([1,2])([16,-39])(tree1),T([1,2])([16,-42])(tree1),T([1,2])([16,-45])(tree1),T([1,2])([16,-48])(tree1),T([1,2])([16,-51])(tree1)])
lakeWoodEast = STRUCT([lakeTreeEast,T([2])(-25)(lakeTreeEast),T([2])(-50)(lakeTreeEast),T([2])(-75)(lakeTreeEast)])

lakeTreeWest = STRUCT([T([1,2])([4,-30])(tree1),T([1,2])([4,-33])(tree1),T([1,2])([4,-36])(tree1),T([1,2])([4,-39])(tree1),T([1,2])([4,-42])(tree1),T([1,2])([4,-45])(tree1),T([1,2])([4,-48])(tree1),T([1,2])([4,-51])(tree1)])
lakeWoodWest = STRUCT([lakeTreeWest, T([2])(-25)(lakeTreeWest),T([2])(-50)(lakeTreeWest),T([2])(-75)(lakeTreeWest)])

#LAMPIONI

post = COLOR([0.502,0.502,0.502])(CYLINDER([0.06,1.5])(36))
bulb = COLOR([1,1,0.4])(T(3)(1.5)(SPHERE(0.2)([36,36])))

lamp = STRUCT([post, bulb])
illumination = STRUCT([T([1,2])([-5,-5])(lamp),T([1,2])([5,-10])(lamp),T([1,2])([15,-10])(lamp),T([1,2])([23,-5])(lamp),T([1,2])([25,20])(lamp),T([1,2])([5,28])(lamp),T([1,2])([15,28])(lamp),T([1,2])([-7,20])(lamp),T([1,2])([-10,10])(lamp),T([1,2])([29,10])(lamp)])

#PANCHINE
support = CUBOID([.5,.5,.5])
sitting = CUBOID([5,1,.2])
backrest = CUBOID([5,.2,.5])
backSupport = CUBOID([.2,.1,.75])

benchPro = STRUCT([T([1,2])([.75,0.25])(support),T(3)(.5)(sitting),T([1,2])([3.75,0.25])(support),T(3)(1)(backrest), T([1,2,3])([.9,-0.1,.5])(backSupport),T([1,2,3])([3.9,-0.1,.5])(backSupport)])
bench  = COLOR([0.7647,0.6902,0.5686])(S([1,2,3])([0.7,0.7,0.7])(benchPro))

benchesInPark = STRUCT([T([1,2])([8,-8])(bench),T([1,2])([25,-15])(R([1,2])(PI/4)(bench)),T([1,2])([-15,-15])(R([1,2])(-PI/4)(bench)), T([1,2])([20,-35])(bench),T([1,2])([-5,-35])(bench)])

#LINCOLN MEMORIAL - Edificio principale
allElements = STRUCT([COLOR([1,0.937,0.835])(allColumnExt), COLOR([1,0.937,0.835])(allFloors), COLOR([1,0.937,0.835])(allColumnInt),COLOR([1,0.937,0.835])(wallsUp), COLOR([1,0.937,0.835])(wallsDown),COLOR([0.6706,0.804,0.737])(vetri3D)])

#VISTA 3D TOTALE 
VIEW(STRUCT([allElements, COLOR([0.898,0.8784,0.8353]) (roundAboutTrasl), COLOR([0.753,0.8588,0.6078])(T([1,2])([9,9])(round2)), COLOR([1,0.937,0.835])(moreBuildings), COLOR([0.651,0.7764,1])(reflectionLake),COLOR([0.753,0.8588,0.6078]) (bigLawn), wood, lakeWoodEast, lakeWoodWest, illumination, benchesInPark]))

