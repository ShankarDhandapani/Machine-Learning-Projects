A = [[1,2,3], 
     [2,3,3], 
     [1,2,5]]
B = [[1,2,3,5], 
     [2,3,3,5], 
     [1,2,5,1]]
I = [[1,0,0,0],
     [0,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]


''' This is the unittest.py class '''


def shape(M):
    h = len(M)
    w = len(M[0])
    return h,w

def matxRound(M, decPts=4):
    st = "{:." + str(decPts) + "f}"
    for i in range(h):
        ct = 0
        for j in M[i]:
            el = st.format(j)
            List = M[i]
            List[ct] = float(el)
            print (el)
            ct = ct + 1
    #return j

def transpose(M):
    m = [[1,2],[3,4],[5,6]]
    #for row in m :
        #print(row)
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    #print("\n")
    for row in rez:
        print(row)
    return None

def matxMultiply(v, G):
    result = []
    total = 0
    for i in range(len(G)):
        r = G[i]
        for j in range(len(v)):
            total = total + (r[j] * v[j])
        result.append(total)
    print result  

h,w = shape(A)
print(shape(I))
print(matxRound(A,1))
print(transpose(A))
##print(matxMultiply(A,B))
matxMultiply(A,B)

      
