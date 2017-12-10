def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(0,len(string)):
        if string[i] in ['A','I','O','E','U']:
            kevin += len(string)-i
        else:
            stuart += len(string)-i 
    if(stuart>kevin):
        print("Stuart "+str(stuart))
    elif(stuart == kevin):
        print("Draw")
    else:
        print("Kevin "+str(kevin))
            
    