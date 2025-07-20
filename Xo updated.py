k=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        print(k[i][j], end=" ")
    print()
T=[[0,0,0],[0,0,0],[0,0,0]]
x=['x','x','x']
o=['o','o','o']
l=0  
A=[]*9
        

while l<10:
    n1=int(input("ENTER::"))
   
    for i in range(9):
     if n1 in A:
       print("don't cheat")
       n1=int(input("ENTER::"))
    A.append(n1) 
 

    
    for i in range(3):
        for j in range(3):
            if n1==k[i][j]:
                k[i][j]='x'

    for i in range(3):
        for j in range(3):
            print(k[i][j],end=" ")
        print()

    
    if  k[0][0]==k[1][1]==k[2][2] or k[2][0]==k[1][1]==k[0][2]:
        print("win")
        break

    if  k[0][0]==k[0][1]==k[0][2] or k[2][0]==k[2][1]==k[2][2] or k[1][0]==k[1][1]==k[1][2]:
        print("win")
        break

    if  k[0][0]==k[1][0]==k[2][0] or k[0][1]==k[1][1]==k[2][1] or k[0][2]==k[1][2]==k[2][2]:
        print("win")
        break

    n2=int(input("ENTER2::"))
    
    for i in range(9):
     if n2 in A:
       print("Don't cheat")
       n2=int(input("ENTER2::"))
    A.append(n2)
    
    for i in range(3):
        for j in range(3):
            if n2==k[i][j]:
                k[i][j]='o'

    for i in range(3):
        for j in range(3):
            print(k[i][j],end=" ")
        print()

    
    if  k[0][0]==k[1][1]==k[2][2] or k[2][0]==k[1][1]==k[0][2]:
        print("win")
        break

    if  k[0][0]==k[0][1]==k[0][2] or k[2][0]==k[2][1]==k[2][2] or k[1][0]==k[1][1]==k[1][2]:
        print("win")
        break

    if  k[0][0]==k[1][0]==k[2][0] or k[0][1]==k[1][1]==k[2][1] or k[0][2]==k[1][2]==k[2][2]:
        print("win")
        break
        
    l+=1