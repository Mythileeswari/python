#using tuple method
customer=["priya","mythilee","naga","nisha"]
cash=(1000,2000,3000,4000)
c=input("enter sender name:")
d=input("enter the reciver name:")
e=int(input("enter the amount:"))


for i in customer:
      if(i==c):
             print("\n")
             print("Sender Available")
             x=(customer.index(i))
             print(i,"Account Balance:",cash[x],"\nDebited Successfully")
             print(i,"Current Bank Balance:",cash[x]-e)
             a=list(cash)
             a[x]=cash[x]-e
             a=tuple(a)
             cash=a
for j in customer:
      if(j==d):
             print("\n")
             y=customer.index(j)
             print(d,"Account Balance:",cash[y],"\nCredited Successfully")
             print(d,"Current Bank Balance:",cash[y]+e)
             a=list(cash)
             a[y]=cash[y]+e
             a=tuple(a)
             cash=a
print(cash)
print(type(cash))
