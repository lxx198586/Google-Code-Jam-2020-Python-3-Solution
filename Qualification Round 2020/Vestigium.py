from collections import Counter

def helper():
    # find trace
    trace=0
    N=int(input())
    M=[input().split(" ") for _ in range(N)]
    # print(M)
    

    for i in range(N):
        for j in range(N):
            M[i][j]=int(M[i][j])

    # print(M)
    i,j=0,0
    while i<N:
        trace+=M[i][j]
        i+=1
        j+=1

    
    # find r is the number of the matrix that contain repeated element
    r=0
    
    for row in M:
        d=Counter(row)
        if len(d)!=N:
            r+=1

    
    # find c
    c=0
    for col in range(N):
        tempList=[]
        for row in range(N):
            tempList.append(M[row][col])
        d=Counter(tempList)
        if len(d)!=N:
            c+=1

    return str(trace)+" "+str(r)+" "+str(c)




for t in range(int(input())):
    print("Case #",str(t+1),": ",helper(),sep="")


