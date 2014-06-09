import simpy as sp 
from IPython.display import Latex

class Geometry(object):
"""
   Initialize this class with a tuple of coordinates of type sp.Symbol,
   and a nonsingular square matrix (sp.Matrix) with valid sympy expressions 
   in the coordinates. 
"""
    def __init__(self, coordinates,metric):
        if len(coordinates)==metric.rows and len(coordsinates)=metric.cols:
            self.gdd = metric #stands for down-down components of the metric g
            self.x = coordinates
            self.dim = len(self.x)
            self.index = range(self.dim)
            self.guu = metric.inv()
            
            self.connection = [[[0 for i in self.index] for i in self.index] for i in self.index]
            for i in self.index:
                for j in self.index:
                    for k in self.index:
                        for m in self.index:
                            self.connection[i][j][k] += 
            
        else:
            print "Creation failed. Please use an n-tuple of coordinate names with a square, n times n matrix"
            

