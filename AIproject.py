print("we have doctors for these problems\n             FEVER  COLD  STOMACH PAIN  HEADACHE\n")
a=input("tell me your problem \n")
x=open("a.txt","wt")
x.write(a)
x.close()



    
if a=="fever":
    d=input("when was started \n")
    y=open("b.txt","wt")
    y.write(d)
    y.close()
    
   
    e=input("is there any vomiting happens \n")
    y=open("b.txt","a")
    y.write(e)
    y.close()
    
    if e=="yes":
        y=open("feverVomating.txt","r")
        print(" =====================================Report====================================\n",y.read())
    else:
        y=open("fever.txt","r")
        print("=====================================Report====================================\n",y.read())

elif a=="cold":
    d=input("when was started \n")
    y=open("b.txt","wt")
    y.write(d)
    y.close()
    
    
    y=open("cold.txt","r")
    print("=====================================Report====================================\n",y.read())
    #e=input("is there any vomiting happens \n")
    #y=open("b.txt","a")
    #y.write(d)
    #y.close()

elif a=="stomach pain":
    d=input("when was started \n")
    y=open("b.txt","wt")
    y.write(d)
    y.close()
    
    e=input("is there any vomiting happens \n")
    y=open("b.txt","a")
    y.write(e)
    y.close()
    f=input("rank your pain\n LOW   MEDIUM   HEIGH  \n\n\n")
    
    #for stomach pain level
    if f=="low":
        z=open("lowStomachpain.txt","r")
        print(" =====================================Report====================================\n",z.read())
    elif f=="medium":
        z=open("mediumStomachpain.txt","r")
        print(" =====================================Report====================================\n",z.read())
    
    elif f=="heigh":
        z=open("heighStomachpain.txt","r")
        print(" =====================================Report====================================\n ",z.read())
    else:
        print("nothing")
    
elif a=="headache":
    d=input("when was started \n")
    y=open("b.txt","wt")
    y.write(d)
    y.close()          
    g=input("rank your pain\n LOW   MEDIUM   HEIGH  \n")    
    
    
    # for headch pain level        
    if g=="low":
        z=open("lowHeadch.txt","r")
        print(" =====================================Report====================================\n",z.read())
    elif g=="medium":
        z=open("mediumHeadch.txt","r")
        print(" =====================================Report====================================\n ",z.read())
    
    else:
        z=open("heighHeadch.txt","r")
        print(" =====================================Report====================================\n",z.read())
else:
    print("thank you")
 
b=input("Any other essue\n yes or no\n")
if b=="yes":
    c=input("tell me the essue \n")
    x=open("a.txt","a")
    x.write(c)
    x.close()
    if c=="fever":
        y=open("fever.txt","r")
        print("=====================================Report====================================\n",y.read())
    elif c=="cold":
        y=open("cold.txt","r")
        print("=====================================Report====================================\n",y.read())

    elif c=="headache":
        z=open("lowHeadch.txt","r")
        print("=====================================Report====================================\n",y.read())

    elif c=="stomach pain":
        z=open("heighStomachpain.txt","r")
        print("=====================================Report====================================\n",y.read())

               
    
else:
    print("thank you for showing your intrest")       
#x=open("a.txt","r")
#print("problem == ",x.read())
#y=open("b.txt","r")
#print("started , womating== ",y.read())





