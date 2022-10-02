#5-1 정수 n개의 합
def solve(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum



#5-3 한수
n = int(input())
a = 0

for i in range(1,n+1):
    if i <=99:
        a+=1
    else:
        s = str(i)
        if int(str(s[0]))-int(str(s[1]))==int(str(s[1]))-int(str(s[2])):
            a+=1
print(a)
    

#6-1 아스키 코드
a = input("알파벳 소문자, 대문자, 숫자 0-9 중 하나를 입력하시오 : ")

print(ord(a))

#6-2 숫자의 합
n = int(input())
a = input()
sum = 0

for i in range(n):
    sum = sum + int(a[i])
print(sum)
