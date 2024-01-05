a,b,c = map(int,input().split())
r = 0
if a==b==c:
    r += 10000+(a*1000)
elif a==b or a==c:
    r += 1000+a*100
elif b==c:
    r += 1000+b*100
else:
    r += 100*max(a,b,c)
print(r)