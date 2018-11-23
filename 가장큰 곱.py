xs=[-2,-3,4,-5,-6]

sums=0

for i in range(len(xs)):
    for j in range(len(xs)):
        sub=xs[j]
        for k in range(len(xs)):
            if(i-1 < k):
                if(xs[k]!=0):
                    if(j==k):
                        continue
                    else:
                        sub*=xs[k]
            if(sub>sums):
                sums=sub
                
print(sums)
            
