def calculadora ():
  operacao = input('escolha uma operação(soma,subtracao,multiplicacao,divisao,expoente):')
  valor_1 =input('informe o primeiro valor:')
  valor_2 =input('infome o segundo valor: ')
  if operacao == "soma":
    resultado = int(valor_1) + int(valor_2)
    print('O resultado da operação é:',resultado)
  elif operacao == "subtracao":
      resultado = int(valor_1) - int(valor_2)
      print('O resultado da operação é:',resultado)
  elif operacao == "multiplicacao":
        resultado = int(valor_1) * int(valor_2)
        print('O resultado da operação é:',resultado)
  elif operacao == "divisao":
        if int(valor_2) == 0:
            print('não pode executar')
        else:
            resultado = int(valor_1) / int(valor_2)
            print('O resultado da operação é:',resultado)
  elif operacao == "expoente":
    resultado = int(valor_1) ** int(valor_2)
    print('O resultado da operação é:',resultado)
  else:
    print('resultado errado')
calculadora()
