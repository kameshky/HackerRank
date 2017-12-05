if __name__ == '__main__':
    N = int(input())
    listt = []
    for i in range(0,N):
        comm = input().split()
        if comm[0] == 'insert':
            listt.insert(int(comm[1]),int(comm[2]))
        elif comm[0] == 'remove':
            listt.remove(int(comm[1]))
        elif comm[0] == 'append':
            listt.append(int(comm[1]))
        elif comm[0] =='sort':
            listt.sort()
        elif comm[0]=='pop':
            listt.pop()
        elif comm[0]=='reverse':
            listt.reverse()
        else:
            print(listt)
        
