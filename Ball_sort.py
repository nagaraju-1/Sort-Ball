x=[]
y=[]
z=[]
def ball_sort(x):
    print("Fill Test Tubes X,Y,Z with any 3 Numbers Make sure Number should not be repeated more than 4 times \n#sample format \nx= 2 0 1 2\nY=0 0 1 2\nZ=1 2 0 1")
    for i in range(3):
        for j in range(4):
            if len(x)<4:
                x.append(int(input("Enter index {}  to insert into X".format(j))))
                
            elif len(y)<4:
                y.append(int(input("Enter index {} to insert in Y".format(j))))
                
            else :
                z.append(int(input("Enter index {} to insert in  Z".format(j))))
        print(x,y,z)
ball_sort(x)

def sort(y):
    print(x,y,z)
    print("Enterted into Sorting Phase")
    a=[]
    b=[]
    
    c=0
    while(1):
        if len(x)==4 and len(y)==4 and len(z) ==4:
            while(1):
                lst=[]
                d=[x,y,z,a,b]
                
                if c==1:
                    print("Sorted")
                    break
                
                for i in d:
                    
                    if len(i)>3:
                        lst.append(i)
                        #print("lst :",lst)
                        if len(lst)==3:

                            #Checking  if list  Contains Unique elements
                            if len(lst[0])==4 and len(lst[1])==4 and len(lst[2])==4 and lst[0][0]==lst[0][1]==lst[0][2]==lst[0][3] and lst[1][0]==lst[1][1]==lst[1][2]==lst[1][3] and lst[2][0]==lst[2][1]==lst[2][2]==lst[2][3]:
                                c=1
                            
                        
                #Insert Stack top value into empty tube
                                
                if len(a)<4 and len(a)==0:
                    a.append(x.pop())
                    print(x,y,z,a,b)
                    continue
                elif len(x)>0 and a[-1]==x[-1]  :
                    a.append(x.pop())
                    print(x,y,z,a,b)
                    continue
                elif len(y)>0 and (a[-1]==y[-1]):
                    
                    a.append(y.pop())
                    print(x,y,z,a,b)
                    continue
                elif len(z)>0 and (a[-1]==z[-1]):
                    
                    a.append(z.pop())
                    print(x,y,z,a,b)
                    continue
                
                #Insert Stack top value into empty tube
                
                elif len(b)<4 and len(b)==0:
                    print(x,y,z,a,b)
                    b.append(x.pop())
                    continue
                elif len(x)>0 and b[-1]==x[-1]:
                    print(x,y,z,a,b)
                    b.append(x.pop())
                    continue
                elif len(y)>0 and (b[-1]==y[-1]):
                    
                    b.append(y.pop())
                    print(x,y,z,a,b)
                    continue
                elif len(z)>0 and b[-1]==z[-1]:
                    
                    b.append(z.pop())
                    print(x,y,z,a,b)
                    continue

                #Check if last two elements in List X are similar or not
                elif len(x)>2 and x[-1]==x[-2]:
                    print(x,y,z,a,b)
                    
                    if len(y)>0 and x[-1]==y[-1]  :
                        x.append(y.pop())
                        continue
                    elif len(z)>0 and x[-1]==z[-1] :
                        x.append(z.pop())
                        continue
                    else:
                        continue
                            
                elif len(x)>1 and x[-1]==x[-2]:
                    print(x,y,z,a,b)
                    if len(y)>0 and x[-1]==y[-1] :
                        
                        x.append(y.pop())
                        continue
                    elif x[-1]==z[-1] and len(z)>0:
                        
                        x.append(z.pop())
                        continue
                    else:
                        print(x)
                        break
                    
                #Check if last two elements in List Y are similar or not    
                elif len(y)>2 and y[-1]==y[-2]:
                    print(x,y,z,a,b)
                    if len(x)>0 and y[-1]==x[-1]:
                        y.append(x.pop())
                        continue
                    elif len(z)>0 and y[-1]==z[-1]:
                        y.append(z.pop())
                        continue
                    else:
                        continue
                            
                elif len(y)>1 and y[-1]==y[-2]:
                    print(x,y,z,a,b)
                    if y[-1]==x[-1] and len(x)>0:
                        y.append(x.pop())
                        continue
                    elif y[-1]==z[-1] and len(z)>0:
                        y.append(z.pop())
                        continue
                    else:
                        continue
                    
                #Check if last two elements in List Z are similar or not
                elif len(z)>2 and z[-1]==z[-2]:
                    print(x,y,z,a,b)
                    if z[-1]==x[-1] and len(x)>0:
                        z.append(x.pop())
                        continue
                    elif y[-1]==z[-1] and len(y)>0:
                        z.append(y.pop())
                        continue
                    else:
                        continue
                            
                elif len(z)>1 and z[-1]==z[-2]:
                    if z[-1]==x[-1] and len(x)>0:
                        z.append(x.pop())
                        continue
                    elif y[-1]==z[-1] and len(y)>0:
                        z.append(y.pop())
                        continue
                    else:
                        continue


                #Check if last element in List x is matching with anyone of the other Stacks
                elif len(x)>0:
                    if len(y)>0 and x[-1]==y[-1]  :
                        
                        x.append(y.pop())
                        continue
                    elif len(z)>0 and x[-1]==z[-1] :
                        
                        x.append(z.pop())
                        continue
                    else:
                        print(x)
                        break



                #Check if last element in List y is matching with anyone of the other Stacks
                elif len(y)>0:
                    if len(x)>0 and x[-1]==y[-1]  :
                        
                        y.append(x.pop())
                        continue
                    elif len(z)>0 and y[-1]==z[-1] :
                        
                        y.append(z.pop())
                        continue
                    else:
                        print(y)
                        break

                #Check if last element in List z is matching with anyone of the other Stacks                    
                elif len(z)>0:
                    if len(x)>0 and x[-1]==z[-1]  :
                        
                        z.append(x.pop())
                        continue
                    elif len(y)>0 and y[-1]==z[-1] :
                        
                        z.append(y.pop())
                        continue
                    else:
                        print(z)
                        break

                    
                else:
                    
                    print(x,y,z,a,b)
                    break
                        
                
                    
            break
        print(a)



    
sort(y)
