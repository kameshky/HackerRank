n = int(input())
dictionary_new = {}
for i in range(0,n):
    list_dict = input().split()
    dictionary_new.update({list_dict[0]:list_dict[1]})
while(True):
    string_test = input()
    if string_test != "":
        if string_test in dictionary_new:
            print(string_test+"="+dictionary_new[string_test])
        else:
            print("Not found")
    else:
        break