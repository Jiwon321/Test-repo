#touchdown Jiwon321
#정지원/202103177/컴퓨터공학부

a=int(input())
b=int(input())
c=int(input())

max = None

if a>b and a>c:
	max = a
elif b>c:
	max = b
else:
	max = c
	
print(max)
