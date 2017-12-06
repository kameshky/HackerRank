def print_rangoli(size):
    l = ['-','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # your code goes here
    for i in range(size,0,-1):
        lis = []
        for j in range(size,i-1,-1):
            lis.append(l[j])
        for k in range(i+1,size+1):
            lis.append(l[k])
        print("-".join(lis).center(size*4-3,"-"))
    for i in range(2,size+1):
        lis = []
        for j in range(size,i-1,-1):
            lis.append(l[j])
        for k in range(i+1,size+1):
            lis.append(l[k])
        print("-".join(lis).center(size*4-3,"-"))
    
            
            
        