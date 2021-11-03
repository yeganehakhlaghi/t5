import csv
product=[]
def menue():
    print("welcom")
    print("1- add")
    print("2- edit")
    print("3- delete")
    print("4- show list")
    print("5- search")
    print("6- buy")
    print("7- exit")


#rows=[]
def load_data_from_database():
    f=open('database.csv','r')
    for row in f:
        info=row[:-1].split(',')
        new_dic={'code':info[0],'name':info[1],'price':info[2],'number':info[3]}
        product.append(new_dic)
   




def add():
    id=int(input("Enter the product code:"))
    Name=input("Enter the product name:")
    Price=int(input("Enter the product price:"))
    Count=int(input("Enter the product count:"))
    new_dict={'code':id, 'name':Name , 'price':Price , 'number':Count}
    product.append(new_dict)
  
    
def edit():
    f=0
    edit_id=(input("Enter the product code you want to change:"))
    for p in product:
        
        if edit_id == p['code'] :

            while True:
               i = int(input("which part do you want to edit ? \n 1- name\n 2- price\n 3- number \n"))
               if i== 1:
                   edit_name = input('Enter the  new product name: ')
                   p['name'] = edit_name
                   break
               elif i == 2:
                   edit_price = input('Enter the new product price:')
                   p['price'] = edit_price
                   break
               elif i == 3:
                   edit_number = input('Enter the new product count:')
                   p['number'] = edit_number
                   break
               else:
                   break
    if f==0:
        print("The wrong code!!")

   
    
    
def delete():
    f=1
    del_id=(input("Enter the product code you want to delete:"))
    for p in product:
        if del_id == p['code'] :
            product.remove(p)
    if f==0:
        print("The wrong code!!")
def search():
    f=0
    search_id=(input("Enter the product code :"))
    for p in product:
        if search_id == p['code'] :
            f=1
            print(p)
    if f==0:
        print("The wrong code!!")
def buy():
    buy_id=input("Enter the product code you want to buy:")
    cnt=int(input("How many do you want?"))
    for p in product:
        if buy_id == p['code'] :
            n=int(p['number'])
            if n==0:
                print("The product is not available")
                break
            else:
                p['number']=n-cnt


def show_list():
    for prod in product:
        print(prod)

def save():
    list = ['', '', '', '']
    f = open("database.csv", 'w')
    writer = csv.writer(f)
    for p in product :
        list[0] = p["code"]
        list[1] = p["name"]
        list[2] = p["price"]
        list[3] = p["number"]
        writer.writerow(list)
    f.close()

load_data_from_database()
while True:
     
     print()
     menue()
     chose=int(input("Please Enter Your Choose:"))
        
     if chose==1:
         add()
         show_list()

     elif chose==2:
        edit()
        show_list()

     elif chose==3:
         delete()
         show_list()

     elif chose==4:
         show_list()

     elif chose==5:
         search()

     elif chose==6:
         buy()
         show_list()

     elif chose==7:
         save()
         show_list()
         break

     else:
         print("The number entered is incorrect!!")

