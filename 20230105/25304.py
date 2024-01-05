a = int(input())
cnt = int(input())
result = 0
while cnt!=0:
    shop, cntShop = map(int,input().split())
    result += shop*cntShop
    cnt -= 1
if a == result:
    print('Yes')
else:
    print('No')