if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_marks = student_marks[query_name]
    sum_listmarks = 0
    for x in list_marks:
        sum_listmarks+=x;
    average_marks = sum_listmarks/len(list_marks)
    print("{:.2f}".format(average_marks))
    
