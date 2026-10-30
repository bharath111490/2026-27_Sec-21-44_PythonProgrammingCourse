num = int(input("Enter a number: "))
orig_num=num
work=num
total=0
while work>0:
    digit=work%10
    total=total+digit
    work=work//10
    print(f"sum of digits of {orig_num} is {total}")
