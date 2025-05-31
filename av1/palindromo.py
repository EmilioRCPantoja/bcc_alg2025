str = input("digite uma palavra: ")
strrv = ""
strse = ""
aux = 0

for i in range(len(str)):
    if str[i] != " ":
        strse = strse + str[i]
        
for i in range(len(strse)):
    strrv = strrv + strse[len(strse) - i - 1]

for i in range(len(strse)):
    if strrv[i] != strse[i]:
        print("não é palindromo :(")
        aux = 1
        break
    
if aux == 0:
    print("é palindromo :)")