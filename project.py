#project
add1={}
class product:
         detail={101:{'Name':'oil','Price':135,'Stock':15,'Exp-date':'nov/1/2024'},
                102:{'Name':'soap','Price':45,'Stock':10,'Exp-date':'nov/2/2024'},
                103:{'Name':'honey','Price':20,'Stock':5,'Exp-date':'nov/3/2024'},
                104:{'Name':'biscuit','Price':10,'Stock':25,'Exp-date':'nov/4/2024'},
                105:{'Name':'chocolate','Price':40,'Stock':18,'Exp-date':'nov/5/2024'},
                106:{'Name':'ice-cream','Price':15,'Stock':20,'Exp-date':'nov/6/2024'},
                107:{'Name':'cocount-oil','Price':115,'Stock':23,'Exp-date':'nov/7/2024'},
                108:{'Name':'face-cream','Price':80,'Stock':22,'Exp-date':'nov/8/2024'},
                109:{'Name':'shampoo','Price':1,'Stock':80,'Exp-date':'nov/9/2024'},
                110:{'Name':'juice','Price':30,'Stock':20,'Exp-date':'nov/10/2024'}}
         def view(self):
            for i,j in self.detail.items():
                 print('\n',end='')
                 id1=i
                 print("Id:",id1)
                 for x,y in j.items():
                     print(x,":",y)
                
            if add1:
                    for i, j in add1.items():
                            print('\n',end='')
                            print("Id:",i)
                            for x, y in j.items():
                                    print(x,":",y)
                 
         def adding(self):
                print('\n',end='')
                detail=['Name','Price','Stock','Exp-date']
                def adding(s):
                        a=input(f"Enter {s}:")
                        return(s,a)
                id=int(input("enter the Id:"))
                a=dict(map(adding,detail))
                print('\n',end='')
                add1[id]=(a)
                for i,j in add1.items():
                    print('\n',end='')
                    print("Id:",id)
                    for x,y in j.items():
                            print(x,":",y)
                    print('\n',end='')
                    print("Product Adding sucessfully")
                
         def search(self):
                print('\n',end='')
                get=input("Enter Product name:")
                m=self.detail.copy()
                def search(g):
                        a1,a2=g
                        return a2['Name']==get
                g=filter(search,m.items())
                g=dict(g)
                for i,j in g.items():
                        print('\n',end='')
                        print("Id:",i)
                        for x,y in j.items():
                                print(x,":",y)

         def exp(self):
             print('\n',end='')
             name=input("Enter the Product name:")
             m1=self.detail.copy()
             exp=input("Enter the Expired date:")
             for i,j in m1.items():
                 if ('Exp-date'==exp):
                     print('\n',end='')
             del self.detail[i]
             print('\n',end='')
             print("Deleted the product sucessfully")

class orders(product):
    def billing(self):
        add2=[]
        add3=0
        print('\n',end='')
        #m2=self.detail.copy()
        while True:
            print('\n',end='')
            pn=input("Enter Product name:")
            pq=int(input("Quantity:"))
            for i,j in self.detail.items():
                if j['Name']==pn:
                    a=j['Price']*pq
                    j['Stock'] -= pq
                    add3+=a
                    add2.append({"Product name":pn,"Quantity":pq,"Price":a})
            mn = input("If you want continue yes/no:")
            if mn == 'no':
                if add2:
                    print('\n',"-----BILLING PROCESS---")
                    print('\n',end='')
                    for mm in add2:
                        print("Product name:",mm['Product name'],"Quantity:",mm['Quantity'],"Price:",mm['Price'],'\n',end='')
                    print('\n',end='')
                    print("Total amount:",add3)
                    break
            

d=product()
d1=orders()

while True:
    print("\n",end='')
    print("1.View the product details")
    print("2.Add the new product")
    print("3.Search product")
    print("4.Delete the product")
    print("5.Billing product")
    print('\n',end='')
    n1=int(input("enter the option:"))
    if(n1==1):
        d.view()
    elif(n1==2):
        d.adding()
    elif(n1==3):
        d.search()
    elif(n1==4):
        d.exp()
    elif(n1==5):
        d1.billing()
        
