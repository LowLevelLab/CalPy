from differential_equations import ODE

y1 = lambda x,y,z : 0.1*y -0.1*y*z
y2 = lambda x,y,z : 0.02*y*z-0.1*z  
y = ODE([y1,y2],[0,365], iterations=500)
data = y.rk4([3,1], graphic=True)
print(data)




