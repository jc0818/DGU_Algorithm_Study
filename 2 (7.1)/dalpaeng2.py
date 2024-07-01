a,b,v = map(int, input().split())

if((v-a)%(a-b)==0):
    n = (v-a)/(a-b)+1
else:
    n = (v-a)/(a-b)+2

print(int(n))