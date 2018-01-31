import os
available_sheat="30"
name=[]
age=[]
sex=[]
os.system('cls')
uname=input("Username:")
password=input("Password:")
login=input("Enter 'y' or 'Y' for login: ") 
os.system('cls')
if (login=="y" or login=="Y"):
    form=input("Form:")
    to=input("To:")
    jdate=input("Journey Date:")
    submit=input("Enter 's' or 'S' for submit")
    os.system('cls')
    if(submit=='S' or submit=='s'):
        print("Select your Quota")
        print("1. LOWER BERTH/Sr. CITIZEN")
        print("2. General")
        print("3. PHYSICALLY HANDICAP")
        print("4. LADIES")
        quota=input()
        os.system('cls')
        if(quota=="1"):
            quota_type="LOWER BERTH/Sr. CITIZEN"
        if(quota=="2"):
            quota_type="General"
        if(quota=="3"):
            quota_type="PHYSICALLY HANDICAP"
        if(quota=="4"):
            quota_type="LADIES"
        os.system('cls')
        print("Select train")
        print("S.No\t"+"Train_no\t"+"Train name\t\t\t"+"from\t\t\t"+"To\t")
        print("1. \t\t"+"03302\t\t"+"DHN ASN SPL\t"+form+"\t\t\t"+to)
        print("2. \t\t"+"04767\t\t"+"HMH SGNR PASS SPL\t"+form+"\t\t\t"+to)
        print("3. \t\t"+"04567\t\t"+"PBC MKN SPL\t"+form+"\t\t\t"+to)
        train=input();
        os.system('cls')
        if(train=="1"):
            train_no="03302"
            train_name="DHN ASN SPL"
        if(train=="2"):
            train_no="04767"
            train_name="HMH SGNR PASS SPL"
        if(train=="3"):
            train_no="04567"
            train_name="PBC MKN SPL"
        os.system('cls')
        print("Select class \n 1. 1A \t 2. 2A \t 3. 3A \t 4. SL \t 5. 2S")
        clss=int(input())
        os.system('cls')
        if(clss==1):
            prefered_class="1A"
        if(clss==2):
            prefered_class="2A"
        if(clss==3):
            prefered_class="3A"
        if(clss==4):
            prefered_class="SL"
        if(clss==5):
            prefered_class="2S"
        print("Available sheat: "+available_sheat)
        sheat_count=input("enter the no of sheat you need to book")
        available_sheat=int(available_sheat)-int(sheat_count)
        os.system('cls')
        if(available_sheat>0):
            print("Train No: "+train_no+"\tJourney Date: "+jdate+"\tClass: "+prefered_class)
            print("From Station: "+form+"\tTo Station: "+to+"\tQuota: "+quota_type)
            i=0
            while(i<int(sheat_count)):
                pname=input("Passenger Name:")
                page=input("Age: ")
                gender=input("Sex M or F: ")
                name.insert(i,pname)
                age.insert(i,page)
                sex.insert(i,gender)
                i=i+1
            os.system('cls')
            print("Train No: "+train_no+"\tJourney Date: "+jdate+"\tClass"+prefered_class)
            print("From Station: "+form+"\tTo Station: "+to+"\tQuota:"+quota_type)
            print("S.NO\tPassenger Name\tAge\tGender")
            j=0
            while(j<int(sheat_count)):
                print(str(j+1)+"\t"+str(name[j])+"\t"+str(age[j])+"\t"+str(sex[j]))
                j=j+1
            print("Ticket Booking has been completed")
