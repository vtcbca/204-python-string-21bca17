# write a script to enter five string in list and check and print string whoes lenth has been even number character without any string function

def creatlist():
    l=[]
    for i in range(6):
        s=input("Enter string")    
        l.append(s)
     return(creatlist)   
def even(l):
    count=0
    for i in l:
        for j in i:
            if(j%2==0):
                print("total string of even {} character:".format(j))
                count+=l
    return(even)
createlist()
ans=count(l)
print(ans)

    
     

