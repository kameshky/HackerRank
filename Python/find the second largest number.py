if __name__ == '__main__':
    n = int(input())
    
    arr = list(int(x) for x in input().split())
    print(max([x for x in arr if x!=max(arr)]))