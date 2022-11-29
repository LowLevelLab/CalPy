from differential_equations import ODE

y1 = lambda x,y,z : x+y-z
y2 = lambda x,y,z : x-y-2*z
y = ODE([y1,y2],[0,1])
data = y.euler2([1,2])




