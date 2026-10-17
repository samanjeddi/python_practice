List_1 = [1,2,3,4,5]
List_2 = [4,5,6,7,8]
List_3 =[]

for num in List_1:
    List_3.append(num)

for num in List_2:
    if num not in List_3:
        List_3.append(num)

print(List_3[:3])