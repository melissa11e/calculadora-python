sinal=input("digite:\n + para soma;\n - para subtração;\n * para divisão;\n / para divisão;\n % para calculadora de pocentagem:\n ")

if sinal=='+' or sinal=="-" or sinal=="*" or sinal=="/":

 n1=float(input("Digite o primeiro número: "))
 n2=float(input("Digite o segundo número: "))

 if sinal=="+":
  resultado=n1+n2

 elif sinal=="-":
  resultado=n1-n2

 elif sinal=="*":
  resultado=n1*n2

 elif sinal=="/":
  if n2!=0:
    resultado=n1/n2
  else:
      resultado="Não existe divisão por 0."

elif sinal=="%":
  print("Digite o tipo de cálculo desejado:")
  sinal2=input("Porcentagem: %;\nDesconto de porcentagem: -%;\nAcréscimo de porcentagem: +%\n")
  valor=float(input("Digite o valor: "))
  porcentagem=float(input("digite sua porcentagem (somente o número): "))


  if sinal2=="%":
    resultado=valor*(porcentagem/100)

  elif sinal2=="-%":
    resultado=valor-valor*(porcentagem/100)

  elif sinal2=="+%":
    resultado=valor+valor*(porcentagem/100)
  else:
    resultado+"Inválido"


else:
  resultado="Resultado inválido"


print("O resultado é: %.2f" %resultado)