#find the smallest value of the expression such as y = 10*x**2-35*x+2
# further write the code to solve any expression
def smallest_value_of_equation(a,b,c):
    x=-b/(2*a)
    print("x=",x)
    y=a*(x**2)+b*x+c
    return y

print(smallest_value_of_equation(10,-35,2))
