from larcc import *


   def diagram2cell(diagram,master,cell):
      matrix = diagram2cellMatrix(diagram)(master,cell)
      diagram =larApply(matrix)(diagram)
      (V1,CV1),(V2,CV2) = master,diagram
      x1,x2 = len(V1), len(V2)
# cerco i vertici in comune
      V, CV1, CV2, n12 = vertexSieve(master,diagram)
      comuni = range(x1-x12, x1)
      intervallo = range(x1,x1-x12+x2)


      def checkInclusion(V,cell,intervallo):
         vertici = [V[v] for v in theCell]
         minimo, massimo = min(vertici), max(vertici)
         cell += [v for v in newRange if (
            minimo[0] <= V[v][0] and minimo[1] <= V[v][1] and minimo[2] <= V[v][2]
            and
            V[v][0] <= massimo[0] and V[v][1] <= massimo[1] and V[v][2] <= massimo[2]
            )]
         return cell
# addition of new vertices into the adjacents of cell c
      CV1 = [checkInclusion(V,c,intervallo)
      if set(c).intersection(comuni) != set() else c
      for c in CV1]

   CV = [c for k,c in enumerate(CV1) if k != cell] + CV2
   master = V, CV
     return master
