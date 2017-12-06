import operator
if __name__ == '__main__':
    students = [] 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    students.sort(key=lambda x: (x[1],x[0]))
    a = 1
    for i in range(1,len(students)):
        if students[i][1]==students[a][1] and students[0][1]!=students[a][1]:
            print(students[i][0])
        elif students[0][1]==students[a][1]:
            a+=1
