#task amount debited and credited transaction
'''customer=["priya","mythilee","naga","nisha"]
cash=[1000,2000,3000,4000]
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
      elif(i==d):
             print("\n")
             y=customer.index(i)
             print(d,"Account Balance:",cash[y],"\nCredited Successfully")
             print(d,"Current Bank Balance:",cash[y]+e)
             break
      else:
            print("the customer not available")
            break'''

#another method"

'''customer=["priya","nisha","mythilee","naga"]
cash=[1000,2000,3000,4000]
c=input("sender name:")
d=input("receiver name:")
e=int(input("enter the amount:"))
j=0
for i in customer:
    if(i==c):
        print("\n")
        i1=cash[j]
        print("irukango")
        print("sender amount:",i1)
        print("now available amount:",i1-e)
    
    elif(i==d):
        print("\n")
        i2=cash[j]
        print("receiver amount:",i2)
        print("now amount receive",i2+e)
    j+=1
    
else:
    print("the sender is not avilable")'''


    
   


        






