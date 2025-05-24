s=input()
s2=""
s=list(s)
i=1

for i in range(len(s)):
    s2+=s[(len(s)-1)-i]

print(s2)

