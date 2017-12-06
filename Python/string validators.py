if __name__ == '__main__':
    s = input()
    an,a,d,l,u = 0,0,0,0,0
    for i in s:
        if i.isalnum():
            an+=1
        if i.isalpha():
            a+=1;
        if i.isdigit():
            d+=1
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
    listto_iterate = [an,a,d,l,u]
    for x in listto_iterate:
        if x>0:
            print("True")
        else:
            print("False")