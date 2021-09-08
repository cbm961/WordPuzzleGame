#a)
def create_grid(fileName):
    f=open(fileName, 'r')
    r=f.readline()
    L=r.split()
    for i in range(len(L)):
        L[i]=int(L[i])
    t=f.read()   
    M=[]                     
    for s in range(L[1]):
        R=t[s*L[0]:((s+1)*L[0])]
        M+=[R]
    f.close()
    return M

M=create_grid('grid.txt')
for x in M:
    print(x)
    
#b)
def puzzleSearch(fileName, word):
    M=create_grid(fileName)
    
    t=False
    for i in range(len(M)):
        if word in M[i]:
            p=i
            for j in range(len(M[i])):
                if M[i][j]==word[0]:
                    o=j
                    t=True
                    break
    b=''
    c=''
    for w in range(len(M)):
        for v in range(len(M[i])):
            f=False
            l=False
            if M[w][v]==word[0]:
                for e in range(1,len(word)):
                    if w+e<(len(M[0])):
                        if M[w+e][v]==word[e]:
                            x=w
                            y=v
                            b+=M[w+e][v]
                    if w+e<(len(M[0])) and v+e<(len(M[1])):
                        if M[w+e][v+e]==word[e]:
                            x=w
                            y=v
                            c+=M[w+e][v+e]
    if (word[0]+b)==word:
        f=True
    if (word[0]+c)==word:
        l=True
        
    if t==True:
        print('Result:', word, 'found: row', p+1,', column',o+1 ,', going right')
    if f==True:
        print('Result:',word[0]+b, 'found: row', x+1,', column',y+1 ,', going down')
    if l==True:
        print('Result:',word[0]+c, 'found: row', x+1,', column',y+1 ,', going diagonally')
    if t==False and f==False and l==False:
        print('Result:', word,'not found')
        
        
        
puzzleSearch('grid.txt', 'huw')