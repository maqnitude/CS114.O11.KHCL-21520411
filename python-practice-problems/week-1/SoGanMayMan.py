number = input()

lucky_count = number.count('4') + number.count('7')
     
if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")