a,b=input().split()
b=int(b)
f,u=a.split('.')
r=len(u)
n=int(f+u)
N='0'*b+str(n**b)
if float(a)<1:print('0',end='')
print((N[:(-r*b)]+'.'+N[(-r*b):]).strip('0'))
