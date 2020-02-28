'''
This program calculates the following sequence, explicitly:
https://oeis.org/A030186
List of more elements:
https://oeis.org/A030186/b030186.txt
For this, we first have to solve q^3 - 3q^2 - q + 1 = 0:
   q1 = -0.675130870566646
   q2 =  0.460811127189111
   q3 =  3.214319743377535
 
Then the following system of equations:
   A*q1^1 + B*q2^1 + C*q3^1 = 1;
   A*q1^2 + B*q2^2 + C*q3^2 = 2;
   A*q1^3 + B*q2^3 + C*q3^3 = 7:
       A = -0.379144119335063
       B =  0.172384544188623
       C =  0.206759575146440
 
=== Code based on wolframalpha values ===
A = -0.37914411933506301486390954
B = 0.172384544188622698495244888
C = 0.206759575146440316368662352
 
q1 = -0.67513087056664607088962
q2 = 0.460811127189110883474124
q3 = 3.214319743377535187415498
 
#accurate 'til  member #30
#already 64k+ diff at member #40
for i in range(1, 52):
   o = A*q1**i + B*q2**i + C*q3**i
   print("{0}.: {1}".format(i-1, round(o)))
 
input()
======= END =======
'''
 
import decimal as d
 
#setting precision of further calculations
d.getcontext().prec = 333
 
#calculate the roots of q^3 - 3q^2 - q + 1 = 0 with the Newton's method
def calcRoots(decimals = 8):
    #absolute value function
    def absolute(x):
        return -x if x < 0 else x
    #base function
    def f(q):
        return q**3 - 3*q**2 - q + 1
    #differential function
    def Df(q):
        return 3*q**2 - 6*q - 1
 
    #we can set a smaller precision inside the function via an argument
    prec = d.Decimal(10**-decimals)
    #approximations / base values; and a list for the final roots
    approxRoots = [-0.675, 0.461, 3.214]
    roots = []
   
    for r in approxRoots:
        #not all magic numbers work for root #3
        prev, curr = d.Decimal(r / 1.23), d.Decimal(r)
        #actually that's the Newton's method part
        while absolute(curr - prev) > prec:
            prev, curr = curr, prev - f(prev) / Df(prev)
        roots.append(curr)
    return roots
 
#determinant function for 3*3 matrices
def det(M):
    #helping determinant function for 2*2 matrices; ad - bc
    def littleDet(N):
        return N[0][0] * N[1][1] - N[0][1] * N[1][0]
 
    #   a * det([[e, f], [h, i]])
    # - b * det([[d, f], [g, i]])
    # + c * det([[d, e], [g, h]])
    return  M[0][0] * littleDet([[M[1][1], M[1][2]],  
                                 [M[2][1], M[2][2]]]) \
          - M[0][1] * littleDet([[M[1][0], M[1][2]],  
                                 [M[2][0], M[2][2]]]) \
          + M[0][2] * littleDet([[M[1][0], M[1][1]],  
                                 [M[2][0], M[2][1]]])
 
#based on the common notation (Ax = B), this calculats B_i
#(its calculated from A and B; here coeffMatrix and outcomeMatrix)
def changeMatrix(base, changer, n):
    #doesnt work w the [:] trick as matrices are just "too deep" objects
    from copy import deepcopy
    b = deepcopy(base)
    for i in range(3):
        b[i][n] = changer[i]
    return b
 
#should be d.getcontext().prec instead of 323, but it crashes w bigger number
roots = calcRoots(323)
#printing stuff
for i, r in enumerate(roots):
    print("q{0}: {1}".format(i+1, str(r)[:30]))
 
#these are the matrices of the system of equations
q1, q2, q3 = roots
coeffMatrix = [[q1**1, q2**1, q3**1],
               [q1**2, q2**2, q3**2],
               [q1**3, q2**3, q3**3]]
outcomeMatrix = [1, 2, 7]
 
#solving the SoE with matrix algebra (called Cramer's rule)
coeffs = []
for i in range(3):
    x = det(changeMatrix(coeffMatrix, outcomeMatrix, i)) / det(coeffMatrix)
    coeffs.append(x)
   
#pringing stuff again
for i, c in enumerate(coeffs):
    print("c{0}: {1}".format(i+1, str(c)[:30]))
#printing a new line
print()
 
#coefficients of the solved SoE need names just like the roots of q^3 - ... = 0
A, B, C = coeffs
#printing the most important stuff
#we use the known formula for calculating each member explicitly instead of
#recursively. every single preciding calculations lead back here...
for i in range(1, 12):
    o = A * q1**i + B * q2**i + C * q3**i
    print("{0}.: {1}".format(i-1, round(o)))
#Yeeey
print("Accurate 'til the 649th element.")
#we wont calculate several hundreds of elements. this is cool enough
 
print()
input("Press Enter to exit.\n")
