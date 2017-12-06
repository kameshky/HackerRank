def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])+1
    for i in range(1,number+1):
        print(str(i).rjust(width-1)+str(oct(i))[2:].rjust(width)+str(hex(i)).swapcase()[2:].rjust(width)+str(bin(i))[2:].rjust(width))