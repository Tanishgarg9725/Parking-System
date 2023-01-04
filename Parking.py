vehicle_number=[]
vehicle_type=[]
vehicle_name=[]
Time=[]
owner_list=[]
amt2=40
amt4=60
space2=100
space4=100
park2=0
park4=0
i=0
imer=""
vno=""
while True:
    print("1. Vehicle Entry")
    print("2. Rate")
    print("3. Remove Vehicle and get the bill")
    print("4. View the no. of parked vehicles")
    print("5. View the no. of parking spaces available")
    print("6. Exit")
    option=input("Select option: ")
    if option=="1":
        o=True
        while o==True:
            owner=input("Enter the name of the owner: ")
            if owner=="":
                print("Please enter valid name")
            else:
                owner_list.append(owner)
                o=False
        t=True
        while t==True:
            vtype=input("Enter whether your vehicle is 2 wheeler or 4 wheeler: ")
            if vtype!="2" and vtype!="4":
                print("Invalid Input, please enter either 2 or 4")
            elif vtype=="2":
                if space2==0:
                    print("Sorry for the inconvience, the parking for 2 wheelers is full")
                    t=False
                else:
                    space2-=1
                    park2+=1
                    vehicle_type.append(vtype)
                    t=False
                    break
            elif vtype=="4":
                if space4==0:
                    print("Sorry for the inconvience, the parking for 4 wheelers is full")
                    t=False
                else:
                    space4-=1
                    park4+=1
                    vehicle_type.append(vtype)
                    t=False
        n=True
        while n==True:
            vname=input("Enter Vehicle Name: ")
            if vname=="":
                print("Please Enter Appropriate Vehicle Name")
            else:
                vehicle_name.append(vname)
                n=False
        T=True
        while T==True:
            vno=input("Enter Vehicle no. (xxxx-xx-xxxx): ").upper()
            if len(vno)!=12:
                print("Invalid Input, please enter appropriate vehicle number of length 12")
            else:
                vehicle_number.append(vno)
                T=False
        q=True
        while q==True:
            tim=input("Enter entry time (HH:MM): ")
            l=tim.split(":")
            if len(tim)!=5:
                print("Enter valid time in the above given format")
            elif tim[2]!=":":
                print("Enter valid time, and please input numbers")
            elif l[0].isdigit()==False or l[1].isdigit()==False:
                print("Enter valid time in the above given format")
            elif int(l[0])>23 or int(l[0])<0 or int(l[1])>60 or int(l[1])<0:
                print("Error, please enter time in 24 hour system")
            else:
                Time.append(tim)
                q=False
        print("Vehicle succesfully entered")
    elif option=="2":
        print("For 2 wheelers its 40rs for thr first hour and for every additional hour its 20rs")
        print("For 4 wheelers its 60rs for the first hour and for every additional hour its 40rs")
    elif option=="3":
        T=True
        m=True
        k=True
        K=True
        while m==True and not (vno not in vehicle_number):
            timr=input("Enter exist time (HH:MM): ")
            l=timr.split(":")
            g1=Time[i]
            g2=g1.split(":")
            if len(timr)!=5:
                print("Enter valid time in the above given format")
            elif timr[2]!=":":
                print("Enter valid time in the above given format")
            elif int(l[0])<int(g2[0]):
                print("the exit time should be greater than entry time")
            elif int(l[0])>23 or int(l[0])<0 or int(l[1])>60 or int(l[1])<0:
                print("Error, please enter time in 24 hour system")
            else:
                imer=timr
                m=False
        while T==True:
            vno=input("Enter Vehicle no. (xxxx-xx-xxxx): to be removed: ").upper()
            if len(vno)!=12:
                print("Invalid Input, please enter appropriate vehicle number of length 12")
            elif vno in vehicle_number:
                i=vehicle_number.index(vno)
                ime=Time[i]
                l1=ime.split(":")
                hr1=int(l1[0])
                l2=imer.split(":")
                hr2=int(l2[0])
                hrs=hr2-hr1
                if vehicle_type[i]=="2":
                    space2+=1
                    park2-=1
                    while k==True:
                        if hrs<=1 or hrs==0:
                            print(f"Total amount to be paid: {amt2}rs")
                            k=False
                        elif hrs>1:
                            new_amt2=(20*(hrs-1))+40
                            print(f"Total amount to be paid: {new_amt2}rs")
                            k=False
                elif vehicle_type[i]=="4":
                    space4+=1
                    park4-=1
                    while K==True:
                        if hrs<=1 or hrs==0:
                            print(f"Total amount to be paid: {amt4}rs")
                            K=False
                        elif hrs>1:
                            new_amt4=(40*(hrs-1))+40
                            print(f"Total amount to be paid: {new_amt4}rs")
                            K=False
                vehicle_number.pop(i)
                vehicle_name.pop(i)
                Time.pop(i)
                owner_list.pop(i)
                vehicle_type.pop(i)
                print("Vehicle succesfully removed")
                T=False               
            elif vno not in vehicle_number:
                print("No such entry")
                T=False
    elif option=="4":
        c=park2
        d=park4
        print("The number of 2 wheeler parked are",c)
        print("The number of 4 wheeler parked are",d)
    elif option=="5":
        print("The number of spaces for 2 wheelers available are",space2)
        print("The number of spaces for 4 wheelers available are",space4)
    elif option=="6":
        print("Thank you for using our service")
        break
    elif option!="1" or option!="2" or option!="3" or option!="4" or option!="5" or option!="6":
        print("Invalid Option, please choose a valid option, enter the number option you want")
