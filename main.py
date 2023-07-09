x,y,z,n=map(int,input().split())
near,val=max(x,y,z),'L1'
l=[x,y,z]
for i in range(3):
    if near-n>l[i]-n and l[i]-n>=0:
        near=l[0]
        val='L'+str(i+1)
print(val)
