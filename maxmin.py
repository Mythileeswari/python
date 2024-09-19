#to find the minimum and maximum number in list

a=[1,2,3,4,5]
maxi=a[0]
for i in range(len(a)):
    if a[i]>maxi:
        maxi=a[i]
print("maximum value:",maxi)

b=[1,2,3,4,5]
mini=b[0]
for i in range(len(b)):
    if b[i]<mini:
        mini=b[i]
print("minimum value:",mini)

