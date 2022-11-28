sum = 0
for i in range(1, 8):
    num = int(input(""))
    sum += num
print(round(sum/7, 2))
if 75 >= sum/7 >= 65:
    print("Team Approved")
else:
    print("Team not Approved")
