email=input("Enter your email :")
k=0
m=0
d=0
if len(email)>=6:# wrong email 1
    if email[0].isalpha(): # wrong email 2
        if ("@" in email)and(email.count("@")==1): # wrong email 3
            if (email[-3]==".") ^ (email[-2]=="."): # wrong email 4
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i==i.isalpha():
                            if i==i.upper():
                                m=1
                            elif i.isdigit():
                                    continue
                            elif i=="_" or i=="." or i=="@":
                                    continue
                            else:
                                d=1
                            if k==1 or m==1 or d==1:
                                    print("Wrong email 5")
                            
                else:
                    print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("wrong email 2")
else:
    print("Wrong email 1")
    
