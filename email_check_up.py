email= input("Enter your gmail: ")
# mdsani017888@gmail.com
j,d,k=0,0,0
if len(email)>=8:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k==1
                    elif i.isalpha():
                        if i.isupper():
                            
                            j==1
                    elif i.isdigit():
                        continue
                    elif i== "_" or i=="@"  or i==".":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("Wrong error ! --5")
                else:
                    print("The gmail is correct!!!")
            else:
                print("Wrong error ! -- 4")
        else:
            print("Wrong erro ! --3")
    else:
        print("Wrong error ! -- 2")

else:
    print("Wrong error ! --1")