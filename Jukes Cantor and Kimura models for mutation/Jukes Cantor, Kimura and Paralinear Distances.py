# Author - @ashwin17222

from Data import S0,S1,compute
import numpy as np

def JukesCantorDistance(S0, S1):

    p = sum([1 if S0[i] != S1[i] else 0 for i in range(len(S0))])/len(S0)

    distance = -(3/4)*np.log(1 - (4/3)*p)

    return distance

def KimuraDistance(S0, S1):

    p1 = sum([1 if (S0[i]=="A" and S1[i]=="G") or (S0[i]=="G" and S1[i]=="A") or (S0[i]=="C" and S1[i]=="T") or (S0[i]=="T" and S1[i]=="C") else 0 for i in range(len(S0))])
    p2 = sum([1 if (S0[i] == "A" and S1[i] == "C") or (S0[i] == "A" and S1[i] == "T") or (S0[i] == "G" and S1[i] == "C") or (S0[i] == "G" and S1[i] == "T") or (S0[i] == "C" and S1[i] == "A") or (S0[i] == "C" and S1[i] == "G") or (S0[i] == "T" and S1[i] == "A") or (S0[i] == "T" and S1[i] == "G") else 0 for i in range(len(S0))])

    p1 /= len(S0)
    p2 /= len(S0)

    distance = (-1/2)*np.log(abs(1-2*p1-p2)) + (-1/4)*np.log(abs(1-2*p2))

    return distance

def ParalinearDistance(S0, S1):

    f0 = [S0.count("A"), S0.count("G"), S0.count("C"), S0.count("T")]
    f1 = [S1.count("A"), S1.count("G"), S1.count("C"), S1.count("T")]

    g0 = f0[0]*f0[1]*f0[2]*f0[3]
    g1 = f1[0]*f1[1]*f1[2]*f1[3]

    F = compute(S0,S1)
    detF = np.linalg.det(F)

    distance = (-1/4)*np.log(detF) + (1/8)*np.log(g0*g1)

    return distance

# Jukes Cantor
JC_distance = round(JukesCantorDistance(S0,S1), 10)
print("Jukes Cantor Distance", JC_distance)

# Kimura Distance
KimuraDistance = round(KimuraDistance(S0,S1), 10)
print("Kimura Distance", KimuraDistance)

# Paralinear Distance
ParalinearDistance = round(ParalinearDistance(S0,S1), 10)
print("Paralinear Distance", ParalinearDistance)

# The paralinear distance should be the best estimate for the number of substitutions per site that actually occured
# they are the based on the most general method for nucleotide substitutions
