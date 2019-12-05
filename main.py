from math import sqrt, exp, cos, pi
n, m = map(int, input().split())
 
listMark = []
val = []
for i in range(n):
    l = list(map(int, input().split()))
    val.append(l.pop())
    listMark.append(l)
 
request = list(map(int, input().split()))
 
str_distance = input()
str_kernel = input()
str_window = input()
k = int(input())
 
distance = {
    "manhattan" : lambda l1, l2: sum(abs(x1 - x2) for (x1, x2) in zip(l1, l2)),
    "euclidean" : lambda l1, l2: sqrt(sum(((x1 - x2) * (x1 - x2)) for (x1, x2) in zip(l1, l2))),
    "chebyshev" : lambda l1, l2: max(abs(x1 - x2) for (x1, x2) in zip(l1, l2))
    }
 
 
kernel = {
    "uniform"      : lambda u: 0.5,
    "triangular"   : lambda u: (1 - abs(u)),
    "epanechnikov" : lambda u: 0.75 * (1 - u * u),
    "quartic"      : lambda u: 15 / 16 * pow(1 - u * u, 2),
    "triweight"    : lambda u: 35 / 32 * pow(1 - u * u, 3),
    "tricube"      : lambda u: 70 / 81 * pow(1 - pow(abs(u), 3), 3),
    "gaussian"     : lambda u: (1 / sqrt(2 * pi)) * exp(-0.5 * u * u),
    "cosine"       : lambda u: pi / 4 * cos(pi / 2 * u),
    "logistic"     : lambda u: 1 / (exp(u) + 2 + exp(-u)),
    "sigmoid"      : lambda u: 2 / pi / (exp(u) + exp(-u))
    }
 
def restrictKer(inp):
    lam = kernel[inp]
    if(inp == "gaussian" or
       inp == "logistic" or
       inp == "sigmoid"):
        return lam
    else:
        return (lambda u: (lam(u) if(abs(u) < 1) else 0))
 
 
dist = distance[str_distance]
ker = restrictKer(str_kernel)
listDist = list(map((lambda l: dist(l, request)), listMark))
listDistVal = list(zip(
    listDist,
    val))
 
listDistVal.sort()
 
 
if (str_window == "fixed"):
    h = k
else:
    h = listDistVal[k][0]
aver = sum(val) / n
 
d0 = 0
sum0 = 0
for (d, v) in listDistVal:
    if (d == 0):
        d0 += 1
        sum0 += v
    else:
        break
if (d0 != 0):
    print("%.9f"%(sum0 / d0))
elif (h == 0):
    print("%.9f"%aver)
else:
    sumKer = sum(map(ker,
                     map(lambda x: x / h, listDist)
                     ))
    if (sumKer == 0):
        print("%.9f"%aver)
    else:
        sumYKer = sum(v * ker(d / h) for (d, v) in listDistVal)
        print("%.9f"%(sumYKer / sumKer))
