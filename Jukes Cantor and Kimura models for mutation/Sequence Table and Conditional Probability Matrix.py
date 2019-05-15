# Author - @ashwin17222

from Data import S0,S1

def compute(S0, S1):

    S0 = list(S0)
    S1 = list(S1)

    S0 = [(0 if S0[i]=="A" else 1 if S0[i]=="G" else 2 if S0[i]=="C" else 3 if S0[i]=="T" else None) for i in range(600)]
    S1 = [(0 if S1[i]=="A" else 1 if S1[i]=="G" else 2 if S1[i]=="C" else 3 if S1[i]=="T" else None) for i in range(600)]

    SequenceTable = [[0 for i in range(4)] for j in range(4)]

    for i in range(len(S0)):
        SequenceTable[S1[i]][S0[i]] += 1

    return SequenceTable

def displayfractions(SequenceTable, seqlength, id):

    if id == "1":

        f0 = sum([SequenceTable[0][i] for i in range(4)])
        f1 = sum([SequenceTable[1][i] for i in range(4)])
        f2 = sum([SequenceTable[2][i] for i in range(4)])
        f3 = sum([SequenceTable[3][i] for i in range(4)])

    elif id == "0":

        f0 = sum([SequenceTable[i][0] for i in range(4)])
        f1 = sum([SequenceTable[i][1] for i in range(4)])
        f2 = sum([SequenceTable[i][2] for i in range(4)])
        f3 = sum([SequenceTable[i][3] for i in range(4)])

    else:

        print("invalid id")

    f = [f0, f1, f2, f3]
    f = [ i/seqlength for i in f]

    print("Base A", f[0])
    print("Base G", f[1])
    print("Base C", f[2])
    print("Base T", f[3])

def conditional_probability(SequenceTable, S0):

    f0 = S0.count("A")
    f1 = S0.count("G")
    f2 = S0.count("C")
    f3 = S0.count("T")

    Probability_matrix =[[0 for i in range(4)] for j in range(4)]

    for row in range(4):
        for column in range(4):
            if column == 0:
                Probability_matrix[row][column] = SequenceTable[row][column]/f0
            elif column == 1:
                Probability_matrix[row][column] = SequenceTable[row][column]/f1
            elif column == 2:
                Probability_matrix[row][column] = SequenceTable[row][column]/f2
            elif column == 3:
                Probability_matrix[row][column] = SequenceTable[row][column]/f3

    return Probability_matrix


# Array Sequence Table
# A -> G -> C -> T
# SequenceTable = compute(S0, S1)
# for row in SequenceTable:
#    print(row)
# print()

# fraction of sites per base in S0
# displayfractions(SequenceTable, len(S0), "0")
# print()

# fraction of sites per base in S1
# displayfractions(SequenceTable, len(S1), "1")
# print()

# conditional probability matrix
# CPM = conditional_probability(SequenceTable, S0)
# for row in CPM:
#    print(row)
