def split_and_join(line):
    # write your code here
    split_line = line.split()
    join_line = "-".join(split_line)
    return join_line
print(split_and_join(input()))