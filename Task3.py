# 1. separating odd & even number in to two lists
L = [10,501, 22, 37, 100, 999,87, 351]
L_even = []
L_odd = []
for i in L:
    if i%2 == 0:
        L_even.append(i)
    else:
        L_odd.append(i)
print('Even List:', L_even)
print('Odd List:', L_odd)

# 2. Extracting & counting prime nums
L_prime = []
L_notprime = []
for i in range(2, len(L)):
    prime = True
    for j in range(2, L[i]):
        if L[i]%j == 0:
            prime = False
    if prime == True:
        L_prime.append(L[i])
    if prime == False:
        L_notprime.append(L[i])
print('Prime List:',L_prime)
print('Non prime List:',L_notprime)

# 3. Find & count Happy numbers
def happy_number(n):
    while n != 1:
        n = sum(int(i) ** 2 for i in str(n))
        if (n == 1):
            return True
        else:
            return False
L_HN = []
for i in L:
    h = happy_number(i)
    if h == True:
        L_HN.append(i)
print("There are ",len(L_HN),"Happy numbers in list, they are: ", L_HN)

 # 4. Sum of first & last digits
print("Enter the number to find sum of last & first digits:")
num1 = input()
num2 = str(num1)
sumfl = int(num2[0])+int(num2[-1])
print("sum of last & first digits:", sumfl)

# 6. Common elements among lists
List1 = [56, 32, 24, 45, 23, 46]
List2 = [65, 32, 24, 54, 29, 6]
List3 = [96, 32, 24, 87, 29, 96]
com_ele = list(filter(lambda x: x in List2 and x in List3, List1))
print("Common elements in the lists are: ", com_ele)

# 7. first non repeating numbers
List7 = [10, 11, 40, 39, 10, 23, 50, 10]
non_rep = []
for n in List7:
    if n in non_rep:
        non_rep.pop(non_rep.index(n))
    else:
        non_rep.append(n)

print("First non repeating number is: ", non_rep[0])

# 8. Minimum element in the rated & sorted list
List1 = [10,501,22,37,100,999,87,351]
print("Taken List:", List1)
List1.sort()
print("In the taken list, minimum element is: ",List1[0] )

# 9. find the triplet in the list whose sum is equal to the given value
List5 = [10,20,30,9]
triplet =[]
val = 59
for i in range(len(List5)):
    for j in range(i+1, len(List5)):
        for k in range(j+1, len(List5)):
            if List5[i]+List5[j]+List5[k] == val:
                triplet.append(List5[i])
                triplet.append(List5[j])
                triplet.append(List5[k])
            break
print("Triplets are:",triplet)

# 10. Find if there is a sub-list with sum equal to zero

List6 = [4,2,-3,1, 6]
sublist =[]
val = 0
for i in range(len(List6)):
    for j in range(i+1, len(List6)):
        if List6[i]+List6[j] == val:
            sublist.append(List6[i])
            sublist.append(List6[j])
            break
        else:
            for k in range(j+1, len(List6)):
                if List6[i]+List6[j]+List6[k] == val:
                    sublist.append(List6[i])
                    sublist.append(List6[j])
                    sublist.append(List6[k])
                break
print("Sublist that sums up to 0 is:",sublist)