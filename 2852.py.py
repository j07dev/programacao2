matriz=[]
for z in range(26):
    linha=[]
    for y in range(0,26):
        number=97+(y+z)%26
        linha.append(chr(number))
    matriz.append(linha)
palavrachavestart=input()
N=int(input())
if(len(palavrachavestart)>0 and len(palavrachavestart)<=45 and N>0 and N<=150):
    for i in range(N):
        mensagem=input()
        repeticao=len(mensagem)/len(palavrachavestart)
        size_chave=len(palavrachavestart)
        palavrachave=''
        cont=0
        for p in range(len(mensagem)):
            if (ord(mensagem[p])>=97 and ord(mensagem[p])<=122):
                palavrachave=palavrachave+palavrachavestart[cont%size_chave]
                cont+=1
            else:
                palavrachave=palavrachave+mensagem[p]
    print(palavrachave)
    crypto_mens=''
    for j in range(len(mensagem)):
        linha=ord(palavrachave[j])-97
        coluna=ord(mensagem[j])-97
        if (linha>=0 and linha<26 and coluna>=1 and coluna<26):
            crypto_mens+=mensagem[j]
        else:
            crypto_mens+=mensagem[j]