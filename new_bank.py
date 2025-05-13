#---------------using for emloge------------------------------------------------srat-------------
#== import =======
import re
import os
import random
import datetime
def emloyee_MENU():
    while True:     
        try: 
            print("\n=============Main menu===================\n")
            print("\n========HI Bank employeee ...  ===========\n")

            print("1. create employee ") 
            print("2. create customer") 
            print("3. Transaction history ") 
            print("4. Check Balance") 
            print("5. Withdraw Money") 
            print("6. Deposit Money") 
            print("7. chenge password") 
            print("8. Account ditals ") 
            print("9. Log out")
            print("0. Exit")
            choice=int(input("inter your choice(1-9) :  "))
            if  0<= choice <10:
                return choice
            else:
                    print("   enter your correct choice please ....")
        except ValueError: 
                print("invalid number ... enter correct number please...")
        except TypeError: 
            print("invalid number ... enter correct number please...")
#---------------using for emloyee----------------------

#================================================================= withrow end =========================
#------------------------------------------------------srat costomer menu----------
def  customer_MENU():
    while True:   
        try:
    
            print("\n========main menu===========\n")
            print("1. Check Balance") 
            print("2. Withdraw Money") 
            print("3. Deposit Money") 
            print("4. chenge password") 
            print("5. Account Transaction ditals")
            print("6. Account ditals ") 
            print("7. log out ")
            print("0. Exit")
            choice=int(input("inter your choice(1-7) : "))
            if  0<= choice <8:
                    return choice
            else:
                print("   enter your choice please ....")
            
        except ValueError: 
                print("invalid number ... enter correct number please")
        except TypeError:
             print("invalid number ... enter correct number please")
#Define Banking Functions------------------------------def start-------------------
def deposit(balance1):
    
        global account_num
        global amount
        try:
            now = datetime.datetime.now()
            #amount=check_amount()
           
            
            if amount:
                balance=(int(balance1) + amount)
                print(f"\n ...Thank you for using ...  success full deposit {amount}, your Balance is : {balance}\n")
                with open("mony_Transaction_history_.txt","a") as file:   
                                        #account_number,amount,withrow or deposit,data,time
                    file.write(f"{account_num}, {balance},deposit,{now.date()},{now.time()},\n") 
                return balance
        
            # elif count<4 :
            #     print(f"\ninvalid amount $ {amount} ,enter your deposit amont greater than 0\n")
            # elif count== 4:
            #      print (" check ditals ")
                 
        except ValueError: 
                print("invalid number ... enter correct number please")
#===================================================================end=========================================
# Create a function withdraw using foe ----------------------------------------------

def withdraw(balance2):
    
        global amount
        global account_num
        try: 
            now = datetime.datetime.now()
            #amount=check_amount()
            count=0
            count+1
            if  amount<=int(balance2):
                balance= balance2 - amount
                print(f"\n success full withdrow.. Withdraw amount :{amount} ,balance : {balance}\n")
                with open("mony_Transaction_history_.txt","a") as file:   
                                        #account_number,amount,withrow or deposit,data,time
                    file.write(f"{account_num},{balance}, withdraw , {now.date()} , {now.time()},\n") 
            
                return balance

            # elif count<4 :
                
            #     print(f"\ninvalid amount : {amount} ,enter your withdrow amont less than your  balance\n ")
            # elif count== 4:
                #  print (" check ditals ")
                 
        except ValueError: 
                print("invalid number ... enter correct number please")
#==================================================================end with===================================
def withraw_deposit_lines(account_number):
    
    #global choice
    balance_amount= -1
    with open("customer_mony.txt", 'r') as file:
        lines = file.readlines()
    
    with open("customer_mony.txt", 'w') as file:
        for line in lines:
            s_line=(line.split(","))
            if  account_number!=((s_line[0])):
                file.write(line)
            elif account_number==(s_line[0]):
                if choice==5  : #Withdraw Money") 
                    balance_amount=withdraw(int(s_line[1]))
                    
                    
                      
                if choice==2 : #Withdraw Money") 
                     balance_amount=withdraw(int(s_line[1]))
                      
                elif choice==6 :
                    balance_amount=deposit(int(s_line[1]))
                    
                elif choice==3:
                    balance_amount=deposit(int(s_line[1]))
                #     #  with open("customer_mony.txt","a") as file:
                #     #         file.write(f"{account_num},{balance_amount},{id_number},\n")
            
    if balance_amount==-1:
         print("checked account nomber... ")
         
    else:
        with open("customer_mony.txt","a") as file:
            file.write(f"{account_number},{(balance_amount)},\n")
                                
#--------called----------------------------------------------start-------------------
def check_amount():#heck_amount(return amount)
    while True:
        try:       
            count=0
            count+1    
            amount=int(input("enter  amount : "))
            if amount> 0:
                return amount
            elif count<4 :
                 print(f"invalid amount $ {amount} ,enter your deposit amont greater than 0 \n")
                 print("enter correct amount pleece...--- ! 0<amount---")
        
            elif count== 4 :
                 break

        except ValueError: 
            print("invalid amount ... enter correct amount please")
#===================================================================end=======================================
#-------------------------------------------------------star-------------------
def input_ditals():
    name=(input("enter name : "))
    address=(input("Enter Address : "))
    
    while True:
        age=int(input("Enter Age 0-75 : "))
        while 0<= age <75 :
           
                mobile=(input("Enter mobile number (0771234567): "))
                mobile_num=len(mobile)
                while mobile_num==10:
                    
                        nic=input("enter NIC lenth 10-12  : ")
                        nic1=len(nic)
                        while 9<nic1<13:
                            return[name,nic,address,age,mobile]
                        else:
                            print("enter correct NIC number : ")
                else:
                    print("enter correct mobile number : ")
        else:
             print("enter correct age : ")
   
def creat_employee_login_number():
    return random.randint(10000000, 99999999)
               
def costomer_account_number_creat():
     with open("customer_ditals.txt","r") as file:             
            return random.randint(100000, 999999)
                
#====================================================================end========================================

def Transaction_history(account_num1):
   
    with open ("mony_Transaction_history_.txt") as file:   #Account_nimber,amount,withrow or deposit,data,time     
        print("Account num----Blance---methede---Date---Time---")                 
        for lines in file:
            line=(lines.split( ","))
            
            if (line[0]) == account_num1:
                
                print(list(line))
 #____________-----------------------------------________________
def account_ditals(account_num1):
   
    with open ("customer_ditals.txt") as file:   #Account_nimber,amount,withrow or deposit,data,time                      
        for lines in file:
            line=(lines.split( ","))
            # customer ditals
            if (line[0]) == account_num1:
                print(f"Account number   : {line[0]}")
                print(f"customer Name    : {line[2]}")
                print(f"customer NIC     : {line[3]}")
                print(f"customer age     : {line[5]}")
                print(f"costmer address  : {line[4]}")
                print(f"mobile number    : {line[6]}")
    with open ("employee_ditals.txt") as file:
        for lines in file:
            line=(lines.split( ","))
            # employee ditals
            if (line[0]) == account_num1:
                print(f"Account number   : {line[0]}")
                print(f"customer Name    : {line[2]}")
                print(f"customer NIC     : {line[3]}")
                print(f"customer age     : {line[5]}")
                print(f"costmer address  : {line[4]}")
                print(f"mobile number    : {line[6]}")        
#============================================================
def check_balance(account_num1):
    
     with open ("customer_mony.txt") as file:      #costomer_acount number,balance_mony       
              
        for lines in file:
            line=(lines.split( ","))
            
            if (line[0]) == account_num1:
                 #return line[1]
                 print(f"your balance is : {line[1]}")

###password-------sari ---checked------------------------------------------creattttteeee-------
def password_creat():
    while True:
        print("your password  must contain least ")
        print(" 1 . 8 characters---")
        print(" 2 . one uppercase---")
        print(" 3 . one number---")
        print(" 4 . one special case chatacter---")
        
        password=(input("create a your password  : "))
        password2=(input("confirm password  : "))
        if password != password2:
            print("your passwore not correcte")
           
    
    # Check the length of the password
        elif len(password) < 8:
            print("Check the password length")
    
    # Check for at least one uppercase letter
        elif not re.search(r'[A-Z]', password):
            print("not  one uppercase letter")
    
        # Check for at least one lowercase letter
        elif not re.search(r'[a-z]', password):
            print("at least one lowercase letter")
        
        # Check for at least one digit
        elif not re.search(r'\d', password):
            print( "Fleast one digit")
        
        # Check for at least one special character
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("not special character")
         
        else:
            print("password create success")       
            return password
                

# print("-------------wellcom to bank------------ ")   
#-------------------------------------------creat file ________________------------
def creat_files ():
        

        with open("mony_Transaction_history_.txt","a") as file:   
            file.write(f"Account_nimber ,  amount , withrow/deposit , data   ,  time\n")       
                        

        with open("customer_ditals.txt","a") as file:                                 
                    file.write(f"acount_num    ,  costomer/Emloyee   , name  ,NIC   ,address ,age  , mobile num \n")       
                        

        with open("customer_mony.txt","a") as file:                                 
                     file.write(f"customer_acount number , balance_mony\n")       
                        
               # confom save you-----         
        with open("account_numbers_and_password.txt","a") as file:                                  
                     file.write(f"Account_no , password , costomer/Employee \n")       
        
        with open("employee_ditals.txt","a") as file:                                  
                     file.write(f"login_no ,  costomer/Employee  , Name  ,  NIC , address , age , mobile num \n")       
#========================================================================================
 #----------------------check 1 st login -------------
def password_change(account_num):    
        with open("account_numbers_and_password.txt", 'r') as file:
            lines = file.readlines()

        with open("account_numbers_and_password.txt", 'w') as file:
            for line in lines:
                s_line=(line.split( ","))
                if  account_num!=((s_line[0])):
                    file.write(line)
                elif account_num==((s_line[0])):     
                    password=password_creat()
        num=len(account_num)
        if num ==6:
            with open("account_numbers_and_password.txt","a") as file:            
                file.write(f"{account_num},{password},{"C"},\n")
                
                 
        elif num ==8:
            with open("account_numbers_and_password.txt","a") as file:            
                file.write(f"{account_num},{password},{"E"},\n")
        else:
           print ("Enter your correct account number . ")          
              
 #----------------------------------------------------------------------------------------------------------

while True :
    with open("account_numbers_and_password.txt","a") as file:
         print("---------------wellcome------------------")
    with open("account_numbers_and_password.txt","r") as file:
        count=0
        while file.readline():
            count +=1
        employe= count

        if employe == 0: 
            creat_files()# file  1st line creat -----
            with open("account_numbers_and_password.txt","a") as file:        #Account_no,password,costomer/Employee 
                a="E"
                s="12345"
                d="@Kobi2005"
                file.write(f"{s},{d},{a},\n")   
                print("------costomer----= ID  :   12345")
                print("------costomer----= pass-code  : @Kobi2005")
                break
        elif employe==2:
            
            print("------costomer----= ID  :   12345")
            print("------costomer----= pass-code  : @Kobi2005")
            break
        else:
            break
#==================================================
#-----------------------------------------------------------
def login_check():
    
    while True:
        id_number=input("Enter you ID or account number  :  ")
        password=(input("Enter your password  :  "))
        with open ("account_numbers_and_password.txt") as file:      #Account_no,password,costomer/Employee                    
            for lines in file:
                line=(lines.split( ","))
                
                if (line[0]) == id_number:
                    # print(id_number) 
                    # print(x[2])
                    #print(line[0])
                    
                    
                    if (line[1])==password:# login emloye------------
                        print("-------login success account-------")
                        #print("-------bank employe-------")
                        
                        
                        #         print("---------------thank you for using--------------")
                        nums = (line[2])
                        return nums,id_number
                             
             
                    else:
                       
                        print("---your password not correct----")
                        password1=(input("Enter your password  :  "))
                        if (line[1])==password1:
                             print("-------login success account-------\n")
                             nums = (line[2])
                             return nums,id_number
                        else:
                            break

            else:
                print("Invalid user / password...\n\tEnter Correct username and password. \n")       
                

                        

#=======================================================================================================   
def customer_ditals_menu():
        try: 
                while True:

                    print("1. customer ditals ") 
                    print("2. chenge ditals ") 
                
                    choice=int(input("inter your choice(1-2) :  "))
                    
                         
                    if 0< choice <3:

                        return choice
                    else:
                        print("   enter your correct choice please ....")
        except ValueError: 
                print("invalid number ... enter correct number please...")
        except TypeError: 
            print("invalid number ... enter correct number please...")
#___________________________________
   
   #==================================
    
while True:
    check=login_check()
    account_num=(check[1])
    check_C_E=(check[0])

    while True:     
    
        if "E" == check_C_E:
            choice=emloyee_MENU()
            if choice==1:                    #print("1. create employee ") 
                                            # print("2. create customer") 
                                            # print("3. Transaction history ") 
                                            # print("4. Check Balance") 
                                            # print("5. Withdraw Money") 
                                            # print("6. Deposit Money") 
                                            # print("7. cheng password") 
                                            # print("8. Exit")
                #creat a amployeeee
                ditals=input_ditals()     #name,nic,address,age
                password=password_creat()
                login_num=creat_employee_login_number()
                # primary_key=primary_key_creat()
                name=ditals[0]
                nic=ditals[1]
                address=ditals[2]
                age=ditals[3]
                mobile=ditals[4]
                
                with open("account_numbers_and_password.txt","a") as file:
                    file.write(f"{login_num},{password},E,\n")   #------------Account_no,password, C or E
                with open("employee_ditals.txt","a") as file:
                    file.write(f"{login_num},E,{name},{nic},{address},{age},{mobile},\n")
                                                                    #"login_no,Password,,Name,NIC,a C/E address,age creatre id\n")  
                print("NEW Employee login number : ",login_num)
                print("NEW Employee login password : ",password)


            elif choice==2:                                               # print("2. create customer") 
                                            
                    #creat a costomer-------------------
                c_ditals=input_ditals()     #name,nic,address,age
                c_password=password_creat()
                c_account_num=costomer_account_number_creat()
                # c_primary_key=primary_key_creat()
                
                c_name=c_ditals[0]
                c_nic=c_ditals[1]
                c_address=c_ditals[2]
                c_age=c_ditals[3]
                mobile=c_ditals[4]
                
                
                print("NEW Customer login Account number : ",c_account_num)
                print("NEW Customer login password : ",c_password)
                print("New customer bank balance 0 ... deposit the mony ....")
                with open("account_numbers_and_password.txt","a") as file:
                    file.write(f"{c_account_num},{c_password},C, \n")   #Account_no,password,primary_key
                deposit_mony=check_amount()
                now = datetime.datetime.now()
                with open("mony_Transaction_history_.txt","a") as file:   
                                        #account_number,amount,withrow or deposit,data,time
                    file.write(f"{c_account_num}, {deposit_mony} , deposit , {now.date()} , {now.time()} ,\n") 
                
                with open("customer_ditals.txt","a") as file:
                    file.write(f"{c_account_num},C,{c_name} , {c_nic} , {c_address} , {c_age} ,{mobile},\n")
                                                                    #"login_no,Password, C/E ,Name,NIC,address,age, creater_id\n")  
                with open("customer_mony.txt","a") as file:
                    print(f" success full deposit : {deposit_mony} ")
                    file.write(f"{c_account_num},{deposit_mony},\n")
                                                                            #costomer_acount number,balance_mony       


            elif choice==3:    # print("3. Transaction history ") 
                try: 
                    account_num=(input("enter costomer Account number : "))
                    while True:
                       
                        Transaction_history(account_num)
                        break

                # except ValueError:
                #     print("enter your correct account number .. ") 
                except   TypeError:
                       print("enter your correct account number .. ") 

            elif choice==4:   #print("4.  E Check Balance")
                try: 
                    account_num1=(input("enter costomer Account number : ")) 
                    while True: 
                        check_balance(account_num1)
                        
                        break
                except ValueError:
                    print("enter your correct account number .. ")
                    
                            

            elif 4<choice<7: #Withdraw Money") 
                try: 
                    
                    while True: 
                        account_num1=(input("enter costomer Account number : ")) 
                        amount=check_amount()
                        amount=withraw_deposit_lines(account_num1)
                        break
                except ValueError:
                    print("enter your correct account number .. ")
                        

            elif choice==7: #cheng password"
                # try: 
                    account_num=(input("enter costomer Account number : ") )
                    while True: 
                        password_change(account_num)
                        break
             
                # except ValueError:
                #      print("enter your correct account number .. ")
            
            elif choice ==8:




                try: 
                    account_num=(input("Ditals chenge  Account number or employee number : ") )
                    choice=customer_ditals_menu()
                    if choice==1:
                         account_ditals(account_num)

                         
                    elif choice==2:
                        ditals=input_ditals()
                        name=ditals[0]
                        nic=ditals[1]
                        address=ditals[2]
                        age=ditals[3]
                        mobile=ditals[4]

                        num=len(account_num)
                        if num==6:
                            with open("customer_ditals.txt", 'r') as file:
                                lines = file.readlines()

                            with open("customer_ditals.txt", 'w') as file:
                                for line in lines:
                                    s_line=(line.split( ","))
                                    if  account_num!=((s_line[0])):
                                        file.write(line)
                                    elif account_num==((s_line[0])):     
                                        print ("success full  .")
                            
                            if num ==6:
                                with open("customer_ditals.txt","a") as file:
                                    file.write(f"{account_num},C,{name} , {nic} , {address} , {age} ,{mobile},\n")
                        if num==8:        
                            with open("customer_ditals.txt", 'r') as file:
                                lines = file.readlines()

                            with open("customer_ditals.txt", 'w') as file:
                                for line in lines:
                                    s_line=(line.split( ","))
                                    if  account_num!=((s_line[0])):
                                        file.write(line)
                                    elif account_num==((s_line[0])):     
                                        print ("success full  .")    
                                with open("employee_ditals.txt","a") as file:
                                    file.write(f"{account_num},E,{name},{nic},{address},{age},{mobile},\n")                            
                        else:
                            print ("Enter your correct account number . ")          
            
             
                except ValueError:
                     print("enter your correct account number .. ")
                 
                
                 
                     

            elif choice==9: #log out
                print(F"{'-'*50}\n----THANK YOU FOR USING SYSTEM-----\n{'-'*50}")
                break
                
            elif choice ==0 :# (Exit)
                 exit()

            
        elif "C" == check_C_E:                           
                                                                
            choice=customer_MENU()
            if choice ==1: #   print("1. Check Balance")
                    
                    print(check_balance(account_num))
             
            elif 1<choice<4:     #  print("2. Withdraw Money")

                amount=check_amount()
                withraw_deposit_lines(account_num)
         
            elif choice==4:    # print("5. Transaction history ") 
            
                 password_change(account_num)

              #print("4. chenge password")
                
            elif choice == 5:
                 Transaction_history(account_num)
                 
            elif choice==6:  
                 account_ditals(account_num)
                #account_ditals(account_num)
                #6
                # Transaction_mony(account_num)
                # print(account_num)
                
            
            elif choice==7:   #  print("6. log out")
                 #Transaction_mony(account_num)
                print(F"{'-'*50}\n----THANK YOU FOR USING SYSTEM-----\n{'-'*50}")
                break
            elif choice ==0 :# (Exit)
                 exit()

        else:
            
             break
                

        

        

                        
                        

        
                            
        
