# teste_sistema_desconto
Teste de um sistema de descontos e avaliação dos códigos.
TESTE01
ENTRADA: -1
RESULTADO_ESPERADO: mensagem de erro sem travar o sistema.
RESULTADO_TESTE: Ele Aceita numeros negativos

TESTE02
ENTRADA: ab, letras
RESULTADO_ESPERADO: mensagem de erro sem travar o sistema.
RESULTADO_TESTE: mensagem de erro e interromper o codigo

TESTE03
ENTRADA: 100, 10%
RESULTADO_ESPERADO: Retornar valor com desconto aplicado
RESULTADO_TESTE: Retorna valor digitado

TESTE04
ENTRADA: -100, 10
RESULTADO_ESPERADO: mensagem de erro sem travar o sistema.
RESULTADO_TESTE: Valor Final: R$ -100.0

TESTE05
ENTRADA: @
RESULTADO_ESPERADO: mensagem de erro sem travar o sistema.
RESULTADO_TESTE: mensagem de erro e interromper o codigo

TESTE06
ENTRADA: 100 , -10% DESCONTO
RESULTADO_ESPERADO: mensagem de erro sem travar o sistema.
RESULTADO_TESTE: Retorna valor digitado

TESTE07
ENTRADA: 10.2 , 2%
RESULTADO_ESPERADO: Que ele siga em frente
RESULTADO_TESTE: 10.2 retornado, errado, desconto não aplicado.

TESTE08
ENTRADA: 100, 51%
RESULTADO_ESPERADO: mensagem de erro sem travar o sistema, porque ultrapassou 50%
RESULTADO_TESTE: ele retorna 100, aceita o desconto acima do valor maximo
