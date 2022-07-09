#library management system
class new_user:
    #constructors used
    def __init__(self,num=None):
        #private variable used
        __password=''
        #register by phone number
        #constructor over loading concept used
        if(num==None):

            print('________ENTER YOUR DETAILS__________')
            self.jntuno=str(input(' ENTER YOUR JNTU NUMBER '))
            self.name=str(input('ENTER YOUR NAME '))
            self.phone=int(input('ENTER YOUR PHONE NUMBER '))
            self.address=str(input('ENTER YOUR ADDRESS '))
            self.passcode=str(input('ENTER YOUR PASSWORD '))
            new_user.__password=self.passcode
            print(__password)
            

        #register by the email
        else:
            print('________ENTER YOUR DETAILS__________')
            self.jntuno=str(input(' ENTER YOUR JNTU NUMBER '))
            self.name=str(input('ENTER YOUR NAME '))
            self.email=str(input('ENTER YOUR EMAIL '))
            self.address=str(input('ENTER YOUR ADDRESS '))
            self.passcode=str(input('ENTER YOUR PASSWORD '))  
            new_user.__password=self.passcode
            print(__password)
     #methods concept used        
    def get_jntu(self):
        return self.jntuno        
    def get_names(self):
        return self.name
class search_by_category:
    def all_books_that_are_available(self):
        print('________ALL AVAILABLE CATEGEROIES OF BOOKS________')
        print('1.ARTIFICAIL INTELLIGENCE')
        print('2.MACHINE LEARNING')
        print('3.DEEP LEARNING')
        print('4.BUSINESS MANAGEMENT')
        print('5.STORY BOOKS')
#INHERTANCE CONCEPT USED
class register_book:
    AI=2
    ML=4
    DL=4
    BM=2
    SB=1
    def register(self):  
        print(self.AI)
        print('________ENTER THE BOOK ID THAT YOU WANT TO SELECT________')
        print("1.AI\n2.ML\n3.DL\n4.BM\n5.sb\n ")
        val4=int(input())
        if val4==1:
            if self.AI!=0:
                self.AI=self.AI-1
                print(self.AI)
                print('BOOK REGISTERED SUCESSFULLY')
            else:
                print('NO BOOKS AVAILABLE')    
        elif val4==2:
            if self.ML!=0:
                ML=ML-1
                print('BOOK REGISTERED SUCESSFULLY')
            else:
                print('NO BOOKS AVAILABLE')    
        elif val4==3:
            if self.DL!=0:
                DL=DL-1
                print('BOOK REGISTERED SUCESSFULLY')
            else:
                print('NO BOOKS AVAILABLE')
                    
        elif val4==4:
            if self.BM!=0:
                BM=BM-1
                print('BOOK REGISTERED SUCESSFULLY')
            else:
                print('NO BOOK AVAILABLE')

        elif val4==5:
            if self.SB!=0:
                SB=SB-1
                print('BOOK REGISTERED SUCESSFULLY')
            else:
                print('NO BOOKS AVAILABLE')    
class check_availability(register_book): 
    def status_display(self):
        print('__________BOOKS STATUS_______')
        print('NUMBER OF AI BOOKS AVAILABLE',self.AI)
        print('NUMBER OF ML BOOKS AVAILABLE',self.ML)
        print('NUMBER OF DL BOOKS AVAILABLE',self.DL)
        print('NUMBER OF BM BOOKS AVAILABLE',self.BM)
        print('NUMBER OF SB BOOKS AVAILABLE',self.SB)            
class book_return_status:
    def status(self):
        print('____________STATUS_________')
        print('BOOK HAS TO BE RETURN IN 30 DAYS')
all_user_jntu=[]
all_user_names=[]
while(1):
    print('____________services____________ ')
    print('1.PRESS 1 IF YOU ARE A NEW USER')
    print('2.PRESS 2 IF YOU ARE A EXISTING USER')
    n=int(input())
    if n==1:
        print('_______CHOOSE A OPTION_________')
        print("1.IF YOU WANT TO REGISTER WITH PHONE NUMBER PRESS 1")
        print("2.IF YOU WANT TO REGISTER WITH EMAIL PRESS 0")
        T=int(input())
        if(T):
            testcase1=new_user()
        else:
            testcase1=new_user(T)  
    val1=testcase1.get_jntu()
    all_user_jntu.append(int(val1))
    val2=testcase1.get_names()
    all_user_names.append(int(val2))

    if(n!=1):
        print('_________LOGIN DETAILS________')
        print(all_user_jntu)
        print(all_user_names)
        print('ENTER JNTU NUMBER')
        val8=int(input())
        co=0
        #print(val8)
        for i in range(len(all_user_jntu)):
            if all_user_jntu[i]==val8:
                print('________PASSWORD______')
                p=str(input())
                co=1
                break
        if(co==0):
            print('_____INCORRECT DETAILS_______')
            break

                
        while(1):
            print('_________SERVICES___________')
            print('1.SEARCH BOOK BY CATEGORY')
            print('2.CHECK BOOK AVAILABILITY')
            print('3.REGISTER BOOK ')
            print('4.CHECK BOOK RETURN STATUS')
            print('5.LOGOUT')
            print('6.DELETE ACCOUNT')
            val3=int(input())
            if val3==1:
                testcase2=search_by_category()
                testcase2.all_books_that_are_available()
            elif val3==2:
                testcase3=check_availability()   
                
            elif val3==3:
                #testcase4=register_book()
                #1
                testcase3.register()
                testcase3.status_display()
            elif val3==4:
                testcase5=book_return_status() 
                testcase5.status()
            elif val3==5:
                break    
            elif val3==6:
                print("_______DELETE ACCOUNT___________")
                print("ENTER JNTU NO THAT HAS TO BE DELETED")
                val7=int(input())
                count=0
                for i in range(len(all_user_jntu)):
                    if all_user_jntu[i]==val7:
                        all_user_jntu.remove(all_user_jntu[i])
                        all_user_names.remove(all_user_names[i])
                        print('ACCOUNT DELETED SUCESSFULLY')
                        count=1
                        break
                if count==0:
                    print('NO USER FOUND WITH THAT NUMBER')    








