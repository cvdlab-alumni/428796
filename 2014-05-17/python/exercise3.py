

from scipy import *
from splines import *
from sysml import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#funzione di enumerazione
def numbering(master):
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
    VIEW(hpc)


#funzione di merging
def diagram2cellGroup(diagram,master,group):
    group.sort();
    group.reverse();
    for i in group:
        master = diagram2cell(diagram,master,i)
    numbering(master)
    return master

#funzione di eliminazione
def cellsOff(master,group):
    V,CV = master
    master =  V,[cell for k,cell in enumerate(CV) if not (k in group)]
    numbering(master)
    return master

#funzione che automatizza la prima parte dell'operazione
def automaticInsert(master,group, diagram):
    numbering(master)
    master = diagram2cellGroup(diagram,master,group)
    return master

def automaticRemove(master, group):
	master = cellsOff(master,group)
	return master

#test
master = assemblyDiagramInit([5,5,2])([[.3,7,.1,7,.3],[.3,7,.1,7,.3],[.3,2.7]])
diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])


master = automaticInsert(master,[39,31,35], diagram)
master = automaticRemove(master,[13,32,35,17,55,61,49])

DRAW(master)



