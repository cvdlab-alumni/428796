from pyplasm import *
from scipy import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *



DRAW = COMP([VIEW,STRUCT,MKPOLS])



#SALOTTO

diagramSalotto = assemblyDiagramInit([3,3,2])([[.3,7.5,.1],[.3,5,.1],[.3,2.7]])
hpcSalotto = SKEL_1(STRUCT(MKPOLS(diagramSalotto)))
VSalotto,CVSalotto = diagramSalotto
hpcSalotto = cellNumbering (diagramSalotto,hpcSalotto)(range(len(CVSalotto)),CYAN,2)


#PORTA SALOTTO
toMergeSal = 11

diagramDoorSal2 = assemblyDiagramInit([3,1,2])([[4,1.5,2],[.5],[2.2,.5]])
masterSal = diagram2cell(diagramDoorSal2,diagramSalotto,toMergeSal)
hpcSal = SKEL_1(STRUCT(MKPOLS(masterSal)))
hpcSal = cellNumbering (masterSal,hpcSal)(range(len(masterSal[1])),CYAN,2)


toRemoveSal = [19,9]
masterSal = masterSal[0], [cell for k,cell in enumerate(masterSal[1]) if not (k in toRemoveSal)]

#FINESTRE SALOTTO
toMergeWinSal = 7
toMergeWinSal2 = 3

diagramWinSal = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
masterWinSal = diagram2cell(diagramWinSal,masterSal,toMergeWinSal)
diagramWinSal2 = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
masterWinSal2 = diagram2cell(diagramWinSal2,masterWinSal,toMergeWinSal2)
hpcWinSal = SKEL_1(STRUCT(MKPOLS(masterWinSal2)))
hpcWinSal = cellNumbering (masterWinSal2,hpcWinSal)(range(len(masterWinSal2[1])),CYAN,2)


toRemoveWinSal = [23,29,44,38]
masterWinSal2 = masterWinSal2[0], [cell for k,cell in enumerate(masterWinSal2[1]) if not (k in toRemoveWinSal)]



#DRAW(masterWinSal2)

#CUCINA
diagramCucina = assemblyDiagramInit([3,3,2])([[.3,4,.1],[.1,3,.1],[.3,2.7]])
hpcCucina = SKEL_1(STRUCT(MKPOLS(diagramCucina)))
VCucina, CVCucina = diagramCucina
hpcCucina = cellNumbering(diagramCucina,hpcCucina)(range(len(CVCucina)),CYAN,2)
VIEW(hpcCucina)

#PORTA CUCINA
toMergeCucina = 15
diagramDoorCucina = assemblyDiagramInit([1,3,2])([[.5],[.5,1,1.5],[2.2,.1]])
masterCucina = diagram2cell(diagramDoorCucina,diagramCucina,toMergeCucina)
hpcCuc = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpcCuc = cellNumbering (masterCucina,hpcCuc)(range(len(masterCucina[1])),CYAN,2)
toRemoveCucina = [19,9]
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemoveCucina)]


#FINESTRE CUCINA
toMergeWinCucina = 3
diagramWinCucina = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
masterWinCucina = diagram2cell(diagramWinCucina,masterCucina,toMergeWinCucina)
hpcWinCucina = SKEL_1(STRUCT(MKPOLS(masterWinCucina)))
hpcWinCucina = cellNumbering (masterWinCucina,hpcWinCucina)(range(len(masterWinCucina[1])),CYAN,2)
toRemoveWinCucina = [24,30]
masterWinCucina = masterWinCucina[0], [cell for k,cell in enumerate(masterWinCucina[1]) if not (k in toRemoveWinCucina)]



DRAW(masterWinCucina)




#CAMERA1

diagramCamera1 = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.3,5,.1],[.3,2.7]])
hpcCamera1 = SKEL_1(STRUCT(MKPOLS(diagramCamera1)))
VCamera1,CVCamera1 = diagramCamera1
hpcCamera1 = cellNumbering (diagramCamera1,hpcCamera1)(range(len(CVCamera1)),CYAN,2)

#PORTA CAMERA 1

toMergeCam1 = 11
diagramDoorCam1 = assemblyDiagramInit([3,1,2])([[.2,.5,2.8],[.1],[2.2,.5]])
masterCam1 = diagram2cell(diagramDoorCam1,diagramCamera1,toMergeCam1)
hpcCam1 = SKEL_1(STRUCT(MKPOLS(masterCam1)))
hpcCam1 = cellNumbering (masterCam1,hpcCam1)(range(len(masterCam1[1])),CYAN,2)
toRemoveCam1 = [19,9]
masterCam1 = masterCam1[0], [cell for k,cell in enumerate(masterCam1[1]) if not (k in toRemoveCam1)]


#FINESTRE CAMERA 1

toMergeWinCam1 = 13
diagramWinCam1 = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
masterWinCam1 = diagram2cell(diagramWinCam1,masterCam1,toMergeWinCam1)
hpcWinCam1 = SKEL_1(STRUCT(MKPOLS(masterWinCam1)))
hpcWinCam1 = cellNumbering (masterWinCam1,hpcWinCam1)(range(len(masterWinCam1[1])),CYAN,2)
toRemoveWinCam1 = [30,24]
masterWinCam1 = masterWinCam1[0], [cell for k,cell in enumerate(masterWinCam1[1]) if not (k in toRemoveWinCam1)]



#DRAW(masterWinCam1)


#CAMERA2

diagramCamera2 = assemblyDiagramInit([3,3,2])([[.1,3,.1],[.3,5,.1],[.3,2.7]])
hpcCamera2 = SKEL_1(STRUCT(MKPOLS(diagramCamera2)))
VCamera2,CVCamera2 = diagramCamera2
hpcCamera2 = cellNumbering (diagramCamera2,hpcCamera2)(range(len(CVCamera2)),CYAN,2)


#PORTA CAMERA 2
toMergeCam2 = 11
diagramDoorCam2 = assemblyDiagramInit([3,1,2])([[1.5,1,.5],[.1],[2.2,.5]])
masterCam2 = diagram2cell(diagramDoorCam2,diagramCamera2,toMergeCam2)
hpcCam2 = SKEL_1(STRUCT(MKPOLS(masterCam2)))
hpcCam2 = cellNumbering (masterCam2,hpcCam2)(range(len(masterCam2[1])),CYAN,2)
toRemoveCam2 = [19,9]
masterCam2 = masterCam2[0], [cell for k,cell in enumerate(masterCam2[1]) if not (k in toRemoveCam2)]



#FINESTRE CAMERA 2

toMergeWinCam2 = 7
diagramWinCam2 = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
masterWinCam2 = diagram2cell(diagramWinCam2,masterCam2,toMergeWinCam2)
hpcWinCam2 = SKEL_1(STRUCT(MKPOLS(masterWinCam2)))
hpcWinCam2 = cellNumbering (masterWinCam2,hpcWinCam2)(range(len(masterWinCam2[1])),CYAN,2)
toRemoveWinCam2 = [24,30]
masterWinCam2 = masterWinCam2[0], [cell for k,cell in enumerate(masterWinCam2[1]) if not (k in toRemoveWinCam2)]



#DRAW(masterWinCam2)

#BAGNO1

diagramBagno1 = assemblyDiagramInit([3,3,2])([[.1,4,.3],[.1,2,.3],[.3,2.7]])
hpcBagno1 = SKEL_1(STRUCT(MKPOLS(diagramBagno1)))
VBagno1, CVBagno1 = diagramBagno1
hpcBagno1 = cellNumbering (diagramBagno1,hpcBagno1)(range(len(CVBagno1)),CYAN,2)

#PORTA BAGNO1
toMergeBagno1 = 7
diagramDoorBagno1 = assemblyDiagramInit([3,1,2])([[1.5,1,1.5],[.1],[2.2,.1]])
masterBagno1 = diagram2cell(diagramDoorBagno1,diagramBagno1,toMergeBagno1)
hpcBa1 = SKEL_1(STRUCT(MKPOLS(masterBagno1)))
hpcBa1 = cellNumbering (masterBagno1,hpcBa1)(range(len(masterBagno1[1])),CYAN,2)
toRemoveBagno1 = [19,8]
masterBagno1 = masterBagno1[0], [cell for k,cell in enumerate(masterBagno1[1]) if not (k in toRemoveBagno1)]


#FINESTRE BAGNO 1


toMergeWinBagno1 = 9
diagramWinBagno1 = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
masterWinBagno1 = diagram2cell(diagramWinBagno1,masterBagno1,toMergeWinBagno1)
hpcWinBagno1 = SKEL_1(STRUCT(MKPOLS(masterWinBagno1)))
hpcWinBagno1 = cellNumbering (masterWinBagno1,hpcWinBagno1)(range(len(masterWinBagno1[1])),CYAN,2)
toRemoveWinBagno1 = [24,30]
masterWinBagno1 = masterWinBagno1[0], [cell for k,cell in enumerate(masterWinBagno1[1]) if not (k in toRemoveWinBagno1)]


#DRAW(masterWinBagno1)

#CORRIDOIO


diagramCorridoio = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.1,1,.1],[.3,2.7]])
hpcCorridoio = SKEL_1(STRUCT(MKPOLS(diagramCorridoio)))
VCorridoio,CVCorridoio = diagramCorridoio
hpcCorridoio = cellNumbering (diagramCorridoio,hpcCorridoio)(range(len(CVCorridoio)),CYAN,2)

#PORTA CORRIDOIO

toMergeCorridoio = 3
diagramDoorCorridoio = assemblyDiagramInit([1,3,2])([[.1],[.1,.8,.1],[2.2,.1]])
masterCorridoio = diagram2cell(diagramDoorCorridoio,diagramCorridoio,toMergeCorridoio)
hpcCor = SKEL_1(STRUCT(MKPOLS(masterCorridoio)))
hpcCor = cellNumbering (masterCorridoio,hpcCor)(range(len(masterCorridoio[1])),CYAN,2)
toRemoveCorridoio = [19,8]
masterCorridoio = masterCorridoio[0], [cell for k,cell in enumerate(masterCorridoio[1]) if not (k in toRemoveCorridoio)]
#DRAW(masterCorridoio)


#INGRESSO



diagramIngresso = assemblyDiagramInit([3,3,2])([[.1,3.5,.1],[.1,3,.3],[.3,2.7]])
hpcIngresso = SKEL_1(STRUCT(MKPOLS(diagramIngresso)))
VIngresso, CVIngresso = diagramIngresso
hpcIngresso = cellNumbering(diagramIngresso,hpcIngresso)(range(len(CVIngresso)),CYAN,2)
#VIEW(hpcIngresso)

toMergeIngresso = 11

diagramDoorIngresso = assemblyDiagramInit([3,1,2])([[1.5,1,1.5],[.1],[2.2,.1]])
masterIngresso = diagram2cell(diagramDoorIngresso,diagramIngresso,toMergeIngresso)
hpcIng = SKEL_1(STRUCT(MKPOLS(masterIngresso)))
hpcIng = cellNumbering (masterIngresso,hpcIng)(range(len(masterIngresso[1])),CYAN,2)
VIEW(hpcIng)

toRemoveIngresso = [19,9]
masterIngresso = masterIngresso[0], [cell for k,cell in enumerate(masterIngresso[1]) if not (k in toRemoveIngresso)]
DRAW(masterIngresso)


#BAGNO2
diagramBagno2 = assemblyDiagramInit([3,3,2])([[.3,2,.1],[.1,1.5,.3],[.3,2.7]])
hpcBagno2 = SKEL_1(STRUCT(MKPOLS(diagramBagno2)))
VBagno2, CVBagno2 = diagramBagno2
hpcBagno2 = cellNumbering(diagramBagno2,hpcBagno2)(range(len(CVBagno2)),CYAN,2)

#PORTA BAGNO 2
toMergeBagno2 = 7
diagramDoorBagno2 = assemblyDiagramInit([3,1,2])([[.5,1,.5],[.1],[2.2,.1]])
masterBagno2 = diagram2cell(diagramDoorBagno2,diagramBagno2,toMergeBagno2)
hpcBa2 = SKEL_1(STRUCT(MKPOLS(masterBagno2)))
hpcBa2 = cellNumbering (masterBagno2,hpcBa2)(range(len(masterBagno2[1])),CYAN,2)
toRemoveBagno2 = [19,8]
masterBagno2 = masterBagno2[0], [cell for k,cell in enumerate(masterBagno2[1]) if not (k in toRemoveBagno2)]

#FINESTRE BAGNO 2
toMergeWinBagno2 = 3
diagramWinBagno2 = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
masterWinBagno2 = diagram2cell(diagramWinBagno2,masterBagno2,toMergeWinBagno2)
hpcWinBagno2 = SKEL_1(STRUCT(MKPOLS(masterWinBagno2)))
hpcWinBagno2 = cellNumbering (masterWinBagno2,hpcWinBagno2)(range(len(masterWinBagno2[1])),CYAN,2)
toRemoveWinBagno2 = [24,30]
masterWinBagno2 = masterWinBagno2[0], [cell for k,cell in enumerate(masterWinBagno2[1]) if not (k in toRemoveWinBagno2)]

#DRAW(masterWinBagno2)



#ANTIBAGNO


diagramAnti = assemblyDiagramInit([3,3,2])([[.3,2,.1],[.1,1,.1],[.3,2.7]])
hpcAnti = SKEL_1(STRUCT(MKPOLS(diagramAnti)))
VAnti, CVAnti = diagramAnti
hpcAnti = cellNumbering(diagramAnti,hpcAnti)(range(len(CVAnti)),CYAN,1)
#VIEW(hpcAnti)

toMergeAnti = 7

diagramDoorAnti = assemblyDiagramInit([3,1,2])([[.5,1,.5],[.1],[2.2,.1]])
masterAnti = diagram2cell(diagramDoorAnti,diagramAnti,toMergeAnti)
hpcAn = SKEL_1(STRUCT(MKPOLS(masterAnti)))
hpcAn = cellNumbering (masterAnti,hpcAnti)(range(len(masterAnti[1])),CYAN,1)
#VIEW(hpcAn)

toRemoveAnti = [19,8]
masterAnti = masterAnti[0], [cell for k,cell in enumerate(masterAnti[1]) if not (k in toRemoveAnti)]
#DRAW(masterAnti)



#master

master = assemblyDiagramInit([2,2,1])([[7.5,7.8],[5,6.4],[3]])
hpcMaster = SKEL_1(STRUCT(MKPOLS(master)))
VMaster,CVMaster = master
hpcMaster = cellNumbering (master,hpcMaster)(range(len(CVMaster)),CYAN,2)
#VIEW(hpcMaster)

#inserisco salotto
toMerge = 0
masterWithSal = diagram2cell(masterWinSal2,master,toMerge)
hpcMasterWithSal = SKEL_1(STRUCT(MKPOLS(masterWithSal)))
hpcMasterWithSal = cellNumbering (masterWithSal,hpcMasterWithSal)(range(len(masterWithSal[1])),CYAN,2)

#VIEW(hpcMasterWithSal)

#taglio x cucina
cut1 = assemblyDiagramInit([2,2,1])([[4,3.5],[3,2.5],[3]])
toMerge = 0
masterCut1 = diagram2cell(cut1,masterWithSal,toMerge)
hpcCut1 = SKEL_1(STRUCT(MKPOLS(masterCut1)))
hpcCut1 = cellNumbering (masterCut1,hpcCut1)(range(len(masterCut1[1])),CYAN,2)
#VIEW(hpcCut1)

#inserisco cucina
toMergeCook = 47
masterCook = diagram2cell(masterWinCucina,masterCut1,toMergeCook)
hpcMasterCook = SKEL_1(STRUCT(MKPOLS(masterCook)))
hpcMasterCook = cellNumbering (masterCook,hpcMasterCook)(range(len(masterCook[1])),CYAN,2)
#VIEW(hpcMasterCook)

#taglio x camere da letto
cut2 = assemblyDiagramInit([2,1,1])([[3,4],[5],[3]])
toMerge = 0
masterCut2 = diagram2cell(cut2, masterCook, toMerge)
hpcCut2 = SKEL_1(STRUCT(MKPOLS(masterCut2)))
hpcCut2 = cellNumbering (masterCut2,hpcCut2)(range(len(masterCut2[1])),CYAN,2)
VIEW(hpcCut2)


#inserisco camera 1

toMergeRoom1 = 83
masterRoom1 = diagram2cell(masterWinCam1, masterCut2, toMergeRoom1)
hpcMasterRoom1 = SKEL_1(STRUCT(MKPOLS(masterRoom1)))
hpcMasterRoom1 = cellNumbering (masterRoom1,hpcMasterRoom1)(range(len(masterRoom1[1])),CYAN,2)
#VIEW(hpcMasterRoom1)


#inserisco camera 2

toMergeRoom2 = 82
masterRoom2 = diagram2cell(masterWinCam2, masterRoom1, toMergeRoom2)
hpcMasterRoom2 = SKEL_1(STRUCT(MKPOLS(masterRoom2)))
hpcMasterRoom2 = cellNumbering (masterRoom2,hpcMasterRoom2)(range(len(masterRoom2[1])),CYAN,2)
#VIEW(hpcMasterRoom2)

#taglio x bagno1 e corridoio

cutX = assemblyDiagramInit([2,2,1])([[4,3],[3,2.5],[3]])
toMerge = 0
masterCutX = diagram2cell(cutX,masterRoom2,toMerge)
hpcCutX = SKEL_1(STRUCT(MKPOLS(masterCutX)))
hpcCutX = cellNumbering (masterCutX,hpcCutX)(range(len(masterCutX[1])),CYAN,2)
#VIEW(hpcCutX)



cut3 = assemblyDiagramInit([1,2,1])([[4],[1,2],[3]])
toMerge = 147
masterCut3 = diagram2cell(cut3,masterCutX,toMerge)
hpcCut3 = SKEL_1(STRUCT(MKPOLS(masterCut3)))
hpcCut3 = cellNumbering (masterCut3,hpcCut3)(range(len(masterCut3[1])),CYAN,2)
#VIEW(hpcCut3)

#inserisco bagno 1

toMergeBath1 = 151
masterBath1 = diagram2cell(masterWinBagno1,masterCut3,toMergeBath1)
hpcMasterBath1 = SKEL_1(STRUCT(MKPOLS(masterBath1)))
hpcMasterBath1 = cellNumbering (masterBath1,hpcMasterBath1)(range(len(masterBath1[1])),CYAN,2)
#VIEW(hpcMasterBath1)


#inserisco corridoio
toMergeCorridor = 150
masterCorridor = diagram2cell(masterCorridoio,masterBath1,toMergeCorridor)
hpcMasterCorridor = SKEL_1(STRUCT(MKPOLS(masterCorridor)))
hpcMasterCorridor = cellNumbering (masterCorridor,hpcMasterCorridor)(range(len(masterCorridor[1])),CYAN,2)
#VIEW(hpcMasterCorridor)


#inserisco ingresso

toMergeHall = 46
masterHall = diagram2cell(masterIngresso, masterCorridor, toMergeHall)
hpcMasterHall = SKEL_1(STRUCT(MKPOLS(masterHall)))
hpcMasterHall = cellNumbering (masterHall,hpcMasterHall)(range(len(masterHall[1])),CYAN,2)
#VIEW(hpcMasterHall)

#taglio per bagno2 e antibagno
cut4 = assemblyDiagramInit([2,2,1])([[2,2],[1,1.5],[3]])
toMerge = 45
masterCut4 = diagram2cell(cut4,masterHall,toMerge)
hpcCut4 = SKEL_1(STRUCT(MKPOLS(masterCut4)))
hpcCut4 = cellNumbering (masterCut4,hpcCut4)(range(len(masterCut4[1])),CYAN,2)
#VIEW(hpcCut4)

#inserisco bagno2
toMergeBath2 = 224
masterBath2 = diagram2cell(masterWinBagno2,masterCut4,toMergeBath2)
hpcMasterBath2 = SKEL_1(STRUCT(MKPOLS(masterBath2)))
hpcMasterBath2 = cellNumbering (masterBath2,hpcMasterBath2)(range(len(masterBath2[1])),CYAN,.5)
#VIEW(hpcMasterBath2)

#inserisco antibagno
toMergePre = 223
masterPre = diagram2cell(masterAnti, masterBath2, toMergePre)
hpcMasterPre = SKEL_1(STRUCT(MKPOLS(masterPre)))
hpcMasterPre = cellNumbering (masterPre,hpcMasterPre)(range(len(masterPre[1])),CYAN,.2)
VIEW(hpcMasterPre)

#rimuovo le celle in eccesso e i solai
toRemoveEnd = [146,145,147,45,224,223,94,187,190,209,205,215,267]
masterEnd = masterPre[0], [cell for k,cell in enumerate(masterPre[1]) if not (k in toRemoveEnd)]
hpcMasterEnd = SKEL_1(STRUCT(MKPOLS(masterEnd)))
hpcMasterEnd = cellNumbering (masterEnd,hpcMasterEnd)(range(len(masterEnd[1])),CYAN,2)

VIEW(hpcMasterEnd)
DRAW(masterEnd)