r = 0

for i in range(5):
    a = int(input())
    
    if a < 40:
        a = 40
        
    r += a
print(r//5)