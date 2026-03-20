import math

def f0(x):
    return math.exp(x) - 1 - x - (x**2 / 2)

def f1(x):
    return math.exp(x) - 1 - x
    
    
def f2(x):
    return math.exp(x) - 1 

def u0(x):
    return f0(x) * f1(x)

def u1(x):
    return (f1(x)**2) - (f0(x) * f2(x))
    
def newton_method(x0):
    
    x = x0
    iterations = 0
    
    for i in range(100):
        f0x = f0(x)
        f1x = f1(x)
        
        if abs(f0x) < 1e-10:
            return x, iterations
        if abs(f0x) > 1e5:
            return x, iterations
        
        x_new = x - f0x / f1x
        iterations += 1
        x = x_new
    
    return x, iterations

def newton_modified(x0):
    
    x = x0
    iterations = 0
    
    for i in range(100):
        f0x = f0(x)
        u0x = u0(x)
        u1x = u1(x)
        
        if abs(f0x) < 1e-10:
            return x, iterations
        if abs(f0x) > 1e5:
            return x, iterations
        
        x_new = x - (u0x/u1x)
        iterations += 1
        x = x_new
        
    return x, iterations


x0 = 1.0

root_newton, iter_newton = newton_method(x0)
root_modified, iter_modified = newton_modified(x0)
print(root_newton, iter_newton)
print(root_modified, iter_modified)