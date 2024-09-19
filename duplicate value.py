#duplicate value delete

a=[10,20,30,40,10,20]
for i in a:
    for j in a:
        if i==j and a.count(i)>1:
            a.remove(j)
print(a)





