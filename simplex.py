import csv
import numpy as np
import copy

##Importing A and converting to int##

with open('my_A.csv', 'r') as f:
    reader = csv.reader(f)
    A=list(reader)

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = int(A[i][j])

print("A = ",end=" ")
print(A)

##Importing C and converting to int##

with open('my_c.csv', 'r') as f:
    reader = csv.reader(f)
    C=list(reader)

for i in range(len(C)):
    for j in range(len(C[i])):
        C[i][j] = int(C[i][j])

print("C = ",end=" ")
print(C)

##Importing B and converting to int##

with open('my_b.csv', 'r') as f:
    reader = csv.reader(f)
    B=list(reader)

for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j] = int(B[i][j])

print("B = ",end=" ")
print(B)

##Importing X and converting to int##

with open('my_x.csv', 'r') as f:
    reader = csv.reader(f)
    X=list(reader)

for i in range(len(X)):
    for j in range(len(X[i])):
        X[i][j] = int(X[i][j])

print("X = ",end=" ")
print(X)

##Error message when matrix sizes do not match as per LP requirements##

if (len(A) != len(B[0])):
    print ("Number of rows in A not equal to number of rows in B\nTerminating the program");
    quit();

if (len(C[0]) != len(X[0])):
    print ("The number of entries in x is different than the coeffcients in c\nTerminating the program");
    quit();

##To check if Phase1 initialization is required##

n = 0;
for i in range(len(B)):
    for j in range(len(B[i])):
        if B[i][j] < 0:
            n=n+1

if n>0:
    print("\nSince one of the values of B is negative, Phase 1 initialization is Required")
else:
    print("\nAll the values of B are positive, Phase 1 initialization is Not Required")

##Printing the linear equation##

n = 1;
Y = []
for i in range(len(X)):
    for j in range(len(X[i])):
        Y.append(n)
        n = n+1

print("\nThe Linear Program is: \n")

##Objective Function

print("MAX    ",end=" ")

for i in range(len(X)):
    for j in range(len(X[i])):
        print(C[i][j],end=" ")
        if j == len(C[i]) - 1:
            print("X",end="")
            print(j+1)
        else:
            print("X",end="")
            print(j+1,end=" ")
            print("+ ",end="")

##Check number of variables less than 10

        
if len(X[0]) > 10:
    print ("Number of Variables greater than 10\nTerminating the program");
    quit();



##Constraints


print("SUBJECT TO  ")

for i in range(len(A)):
    for j in range(len(A[i])):        
        print(A[i][j],end=" ")
        if j == len(A[i]) - 1:
            print("X",end="")
            print(j+1,end=" ")
            print("<=", end=" ")
            print(B[0][i])
        else:
            print("X",end="")
            print(j+1,end=" ")
            print("+ ",end="")
            
for j in range(len(X[0])):        
        if j == len(X[0]) - 1:
            print("X",end="")
            print(j+1,end=" ")
            print(">=",end=" ")
            print("0.00")
        else:
            print("X",end="")
            print(j+1,end=" ")
            print(", ",end="")

##Calculate the Objective Value

ObjectiveValue=0
for j in range(len(C[0])):
    ObjectiveValue = ObjectiveValue + C[0][j]*X[0][j]

##Check if the solution is feasible

feasible=0
for i in range(len(A)):
    sum=0
    for j in range(len(A[i])):
        product = A[i][j]*X[0][j]
        sum = sum + product
    print ("\nThe sum of current constraint on left hand  side is",end=" ")
    print (sum,end=". ")
    print ("Value of B on right hand side is",end=" ")
    print (B[0][i],end=". ")

    if sum <= B[0][i]:
        print("This constraint is satisfied")
    else:
        print("This constraint is not satisfied.")
        feasible= feasible + 1

if feasible==0:
    print("\nAll constraints satisfied. The solution is Feasible")
    print("The value of the Objective function is ",end="")
    print (ObjectiveValue)
else:
    print("\nAll constraints not satisfied. This solution is Not Feasible")
    print("The value of the Objective function would have been ",end="")
    print (ObjectiveValue)

#abc = input("\nEnter any key to end the program")

## converting all the lists to matrices for the Project Question#1

N = np.matrix(A)
C = np.matrix(C)
b = np.matrix(B)
X = np.matrix(X)

##First Iteration

##Specifying Nu and Beta

NuSize = N.shape[1]
Nu = []

for i in range(NuSize):
    Nu.append(i+1)
    i = i+1

print("Nu =",end=" ")
print(Nu)

BetaSize = b.shape[1]
Beta = []

for i in range(BetaSize):
    Beta.append(NuSize+i+1)
    i = i+1

print("Beta =",end=" ")
print(Beta)

##Specifying N, B and A(joined by N and B)

print("N =")
print(N)
##print (N.item(0))

B = np.zeros((BetaSize,BetaSize))

for i in range(BetaSize):
   B[i][i] = 1

B = np.matrix(B)

print("B =")
print(B)

A = np.concatenate((N,B),axis=1)
print("A =")
print(A)

##Transposing b, Specifying xBetaStar

b = b.transpose()

print("b =")
print(b)

xBetaStar = b

print("xBetaStar =")
print(xBetaStar)

##Transposing cNu, Specifying zNuStar 

cNu = C.transpose()

print("cNu =")
print(cNu)

zNuStar  = -cNu

print("zNuStar =")
print(zNuStar)

##Starting the iteration steps

while 1:

    ##First Step

    print("\nStep1")

    if (zNuStar > 0).all():
        print("Solution is optimal Now.")
        break
    else:
        print("Solution is not optimal. Proceeding towards Step2")

    ##Second Step

    print("\nStep2")

    zNuStarMinIndex = np.argmin(zNuStar)
    j = Nu[zNuStarMinIndex]

    print("j =",end=" ")
    print(j)

    ##Third Step

    print("\nStep3")

    EjSize = N.shape[1]

    Ej = np.zeros(EjSize)
    Ej[zNuStarMinIndex] = 1

    Ej = np.matrix(Ej)
    Ej = Ej.transpose()

    print("Ej =")
    print(Ej)

    Binverse = B.I

    print("Binverse =")
    print(Binverse)

    DeltaxBeta = Binverse*N*Ej

    print("DeltaxBeta =")
    print(DeltaxBeta)

    ##Fourth Step

    print("\nStep4")
    tlist = []

    bSize = b.shape[0]

    for i in range(bSize):
        titem = DeltaxBeta.item(i) / xBetaStar.item(i)
        tlist.append(titem)

    tmax = max(tlist)

    t = 1/tmax

    print("tlist = ",end="")
    print(tlist)

    print("t = ",end="")
    print(t)

    ##Fifth Step

    print("\nStep5")

    tindex = tlist.index(max(tlist))

    print("Index of t with maximum value = ",end="")
    print(tindex)

    i = tindex + N.shape[1] + 1

    print("So, the basis index, i = ",end="")
    print(i)

    ##Sixth Step

    print("\nStep6")

    EiSize = b.shape[0]

    Ei = np.zeros(EiSize)
    Ei[tindex] = 1

    Ei = np.matrix(Ei)
    Ei = Ei.transpose()

    print("Ei =")
    print(Ei)

    Binverse = B.I

    BInverseIntoN = Binverse*N

    BInverseIntoNTranspose = BInverseIntoN.T

    DeltaZNu = -BInverseIntoNTranspose*Ei

    print("DeltaZNu =")
    print(DeltaZNu)

    ##Seventh Step

    print("\nStep7")

    s = zNuStar.item(zNuStarMinIndex)/DeltaZNu.item(zNuStarMinIndex)

    print("s = ",end="")
    print(s)

    ##Eigth Step

    print("\nStep8")

    xBetaStar = xBetaStar - (t*DeltaxBeta) 

    xBetaStar[j-1] = t;

    print("xBetaStar =")
    print(xBetaStar)

    zNuStar = zNuStar - s*DeltaZNu

    zNuStar[zNuStarMinIndex] = s;

    print("zNuStar =")
    print(zNuStar)

    ##Ninth Step

    print("\nStep9")

    Beta[tindex] = j;

    print("Beta =",end=" ")
    print(Beta)

    Nu[zNuStarMinIndex] = i;

    print("Nu =",end=" ")
    print(Nu)

    tempB = np.matrix(B)
    tempN = np.matrix(N)

    B[:,tindex] = tempN[:,zNuStarMinIndex]

    N[:,zNuStarMinIndex] = tempB[:,tindex]

    print("B =")
    print(B)

    print("N =")
    print(N)

####Printing the optimal solution##
##
##n = 1;
##Y = []
##for i in range(len(X)):
##    for j in range(len(X[i])):
##        Y.append(n)
##        n = n+1
##
##print("\nThe Linear Program is: \n")
##
####Objective Function
##
##print("MAX    ",end=" ")
##
##for i in range(len(X)):
##    for j in range(len(X[i])):
##        print(C[i][j],end=" ")
##        if j == len(C[i]) - 1:
##            print("X",end="")
##            print(j+1)
##        else:
##            print("X",end="")
##            print(j+1,end=" ")
##            print("+ ",end="")
####Constraints
##
##
##print("SUBJECT TO  ")
##
##for i in range(len(A)):
##    for j in range(len(A[i])):        
##        print(A[i][j],end=" ")
##        if j == len(A[i]) - 1:
##            print("X",end="")
##            print(j+1,end=" ")
##            print("<=", end=" ")
##            print(B[0][i])
##        else:
##            print("X",end="")
##            print(j+1,end=" ")
##            print("+ ",end="")
##            
##for j in range(len(X[0])):        
##        if j == len(X[0]) - 1:
##            print("X",end="")
##            print(j+1,end=" ")
##            print(">=",end=" ")
##            print("0.00")
##        else:
##            print("X",end="")
##            print(j+1,end=" ")
##            print(", ",end="")
##
####Calculate the Objective Value
##
##ObjectiveValue=0
##for j in range(len(C[0])):
##    ObjectiveValue = ObjectiveValue + C[0][j]*X[0][j]
##
##
