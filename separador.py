from tkinter import filedialog

def separar(linhas: int):
    file = filedialog.askopenfilename()
    with open(file, 'r', errors='ignore') as arquivo:
        lines = arquivo.readlines()
        cabecalho = lines[0]
        nfile = 0  # Numero para organizar os arquivos a serem criados, sera incrementado no loop for.
        inicio = 0  # Inicio do trecho a ser escrito
        fim = 0  # Fim do trecho
        rangeloop = len(lines) // linhas  # numero de iterações a serem executadas no loop for

        if len(lines) % linhas > 0:  # Caso a conta nao dê exata, faz uma iteração a mais para escrever o que sobrou
            rangeloop += 1

        for x in range(rangeloop):
            nfile += 1
            fim += linhas
            arq = open(file[:-4] + str(nfile) + '.csv', 'w')
            if not nfile == 1:
                arq.write(''.join(cabecalho))
            arq.write(''.join(lines[inicio:fim]))
            inicio = fim
            arq.close()


separar(108)


# quant = input('Quantas linhas em cada arquivo?\n>>> ')
# try:
#     separar(int(quant))
#     print('Pronto!')
#     time.sleep(2)
# except Exception as e:
#     print('Erro: ', e)
