matriz = []
for z in range(26):
    linha = []
    for y in range(26):
        number = 97 + (y+z)%26
        linha.append(chr( (number) ))
    matriz.append(linha)
palavraChaveStart = input()
N = int(input())
if(len(palavraChaveStart) > 2 and len(palavraChaveStart)<=45 and N>0 and N<=150):
    crypto_mens = ""
    for i in range(N):
        mensagemCompleta = input().split()
        cont = 0
        for mensagem in mensagemCompleta:
            size_chave = len(palavraChaveStart)
            palavraChave = ""
            for p in range(len(mensagem)):
                if(ord(mensagem[p])>=97 and ord(mensagem[p])<=122):
                    palavraChave = palavraChave + palavraChaveStart[cont%size_chave]
                    cont += 1
                else:
                    palavraChave = palavraChave + mensagem[p]
            if(mensagem[0] in "aeiou"):
                crypto_mens += mensagem
            else:
                for j in range(len(mensagem)):
                    linha = ord(palavraChave[j])-97
                    coluna = ord(mensagem[j])-97
                    if(linha>=0 and linha<26 and coluna>=0 and coluna<26):
                        #print("Matriz[",linha, ']-->[',coluna,']-->',matriz[linha][coluna])
                        crypto_mens += matriz[linha][coluna]
                    else:
                        #print("Matriz[", linha, ']-->[', coluna, ']-->', mensagem[j])
                        crypto_mens += mensagem[j]
            crypto_mens += ' '    
        crypto_mens += '\n'    
    print(crypto_mens)