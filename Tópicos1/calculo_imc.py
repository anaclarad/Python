nome= input("Insira seu nome:")
idade=input("Insira sua idade:")
peso= float(input("Insira seu peso:"))
altura= float(input("Insira sua altura:"))

imc=peso//(altura*altura)



if imc <18.5:
   print("Você está abaixo do seu peso ideal")

elif   10.5>+ imc  <= 24.9:
 
 print("Seu peso está normal")

elif  25.0 >= imc <=29.9: 
  
 print("você está com excesso de peso")

elif  30.0>= imc <= 34.9:
 
 print("Você apresenta o quadro de Obesidade Classe I")

elif 35.0 >= imc <=39.9:
  print("Você apresenta o quadro de Obesidade Classe II")

else:
    imc > 40.0
    print("Você apresenta o quadro de Obesidade Classe III")

    


