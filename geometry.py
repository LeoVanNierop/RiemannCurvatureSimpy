import simpy as sp 
from IPython.display import Latex

class Geometry(object):
"""
   Initialize this class with a tuple of coordinates of type sp.Symbol,
   and a nonsingular square matrix (sp.Matrix) with valid sympy expressions 
   in the coordinates. Define your arbitrary functions as type sp.Function
   """
    def __init__(self, coordinates, metric):
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
                            self.connection[i][j][k] += self.guu[i,m]*(self.gdd[m,j].diff(self.x[k]) + self.gdd[m,k].diff(self.x[j]) - self.gdd[k,j].diff(self.x[m]))/2
            self.Riemanntensor = [[[[0for in in self.index]for i in self.index]for i in self.index]for i in self.index]
            for i in self.index:
                for j in self.index:
                    for k in self.index:
                        for m in self.index:
                            self.Riemanntensor[i][j][k][m] += self.connection[i]][j][k].diff(self.x[m])-self.connection([i][j][m].diff(self.x[k])
                            for n in self.index:
                                self.Riemanntensor[i][j][k][m] += self.connection[n][j][k]*self.connection[i][m][n] - self.connection[n][j][m]*self.connection[i][k][n]
            
            self.Riccitensor = [[0 for i in self.index]for i in self.index]
            for i in self.index:
                for j in self.index:
                    for k in self.index:
                        self.Riccitensor[i][j] += self.Riemanntensor[n][i][n][j]
                        
            self.Riemannscalar = 0 
            for i in self.index:
                for j in self.index:
                    self.Riemannscalar += self.guu[i,j]*self.Riccitensor[i][j]           
        else:
            print "Creation failed. Please use an n-tuple of coordinate names with a square, n times n matrix"
            
# initialization of the geometric quantities is done
# below here are the "access" functions to retrieve them in nice latex

    def Riemanntensorlatex(self):
        string = "The nonzero components of the Riemann tensor (up to its symmetries) are:\n"
        for i in self.index:
            for j in self.index:
                for k in self.index:
                    for l in self.index:
                        if l>=k and j>=i and self.Riemanntensor[i][j][k][l] != 0:
                            string += r"\begin{equation}R^{" + str(self.x[i]) + r"}_{\phantom{a}" + str(self.x[j]) + r" " + str(self.x[k]) + r" " + str(self.x[l]) + r"}= " + latex(self.Riemanntensor[i][j][k][l]) + r"\end{equation}"+"\n"

        return string                    
                            
    def Riccitensorlatex(self):
        string = "The nonzero components of the Ricci tensor (up to symmetry) are:\n"
        for i in self.index:
            for j in self.index:
                if i>=j and self.Riemanntensor[i][j] != 0:
                    string += r"\begin{equation} R_{" +str(self.x[i]) + " " + str(self.x[j]) + "}= " + latex(self.Ricci[i][j])+"\n" + r"\end{equation}"
        return string                    
                            
    def Riemanscalarlatex(self)
        return r"\begin{equation} R = " + latex(self.Riemannscalar) + r"\end{equation}"
                            
                            
    if __name__ == '__main__":
        t=sp.Symbol(r"t")
        r=sp.Symbol(r"r")
        theta=sp.Symbol(r"\theta")
        phi=sp.Symbol(r"phi")
        coords = (t,r,theta,phi)
        A = sp.Function(r"A")
        B = sp.Function(r"B")        
        metric = sp.Matrix((
        (-exp(2*A(r)), 0, 0, 0)
        (0, exp(2*B(r)), 0, 0)
        (0, 0, r**2, 0)
        (0, 0, 0, r**2*(sp.sin(theta))**2)                           
        ));                    
        Blackhole = geometry(coords, metric)
        Latex(Blackhole.Riccitensorlatex())

        