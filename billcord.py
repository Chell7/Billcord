# Import the module csv that will permit to create the files to store the data 
import csv
# Make a choice between entering data for purchases or for sales
print(' Welcome to Billcord ! \n')
ask= input(' Do you want to record data for purchases or sales ?\n Do you want to read a file? \n Do you want to make some research in a file? \n Type P to record data for purchases and S for sales ; type  R to read a file and L to make research !')

# #Write a function named purchases 
def purchases () :
    print('You can enter your data now !')
    file = open('purchases.csv','a')
    date= (input('\n Enter the date : \n'))
    name = (input('Enter the name of the product \n'))
    qty = int(input ('Enter the quantity of the products : \n'))
    price_unit= int(input('Enter the price for one product : \n'))
    total= price_unit * qty 
    bal= int(input('Enter the balance if it has one , 0 if it has not : \n'))
    total_paid= total - bal
    newRecord= date + ',' + name  + ','+ str(qty) + ',' + str(price_unit) + ',' + str( total) + ',' + str(bal) + ',' + str(total_paid) + '\n'
    file.write(str(newRecord))
    file.close()
        

#Write a function named sales
def sales () :
    print('You can enter your data now !')
    file = open('sales.csv','a')
    date= (input(' \n Enter the date : \n'))
    name = (input('Enter the name of the product \n'))
    qty = int(input ('Enter the quantity of the products : \n'))
    price_unit= int(input('Enter the price for one product : \n'))
    total= price_unit * qty 
    bal= int(input('Enter the balance if it has one , 0 if it has not : \n'))
    total_received= total - bal
    newRecord= date + ',' + name  + ','+ str(qty) + ',' + str(price_unit) + ',' + str( total) + ',' + ',' + str(bal) + ',' + str(total_received) + '\n'
    file.write(str(newRecord))
    file.close()
        
        

# Write a function named read
def read() :
    ask= input ('Choose which feel to read ; P for purchases , S for sales : \n')
    if ask== 'P' or ask== 'p':
        file = open('purchases.csv','r')
        for row in file:
                print(row)
    elif ask== 'S' or ask=='s' :   
        file = open('sales.csv','r')
        for row in file:
            print(row)
    

# Write a function named research 
def research () :
    ask= input ('Choose which feel to research inside ; P for purchases , S for sales : \n')
    if ask== 'P' or ask=='p':
        file = open ('purchases.csv','r')
        search = input('Enter the data you are searching for: ')
        reader = csv.reader(file)
        for row in file:
            if search in str(row):
                print(row)
            
    elif ask== 'S' or ask=='s' :   
        file = open ('sales.csv','r')
        search = input('Enter the data you are searching for: ')
        reader = csv.reader(file)
        for row in file:
            if search in str(row):
                print(row)

#Write a main function named Menu 
def menu() :
    if ask== 'P' or ask=='p':
        purchases()
    elif ask=='S' or ask=='s':
        sales()
    elif ask=='R' or ask=='r':
        read()
    elif ask=='L'or ask== 'l':
        research ()

menu()


