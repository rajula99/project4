str = input()
n = int(input())

ls = len(str)
a_count = str.count('a')
if 'a' in str:
    if a_count == ls:
        print(n)
    elif n % ls == 0:
        print(a_count * int(n / ls))
    else:
        count = a_count * int(n / ls)
        #print(count)
        rem = int(n % ls)
        for i in range(rem):
            if str[i] == 'a':
                count += 1
        print(count)
else:
    print(0)


#correct
