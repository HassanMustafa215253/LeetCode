for i in range(33):
    print(i,"\n\n")
    
    if i%2!=0 and i!=1 or i==0:
        print(False)
        continue
    count =0
    while  count<20:
        count +=1
        if i==2 or i==1:
            print (True)
            break
        if i<2:
            print (False)
            break
        i=i/2
        print (i)