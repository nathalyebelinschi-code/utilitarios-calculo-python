# ==============================================================================
# Script: calculo_fatorial.py
# Propósito: Calcular o fatorial de um número inteiro utilizando a biblioteca math
# Contexto: Experiência Prática 1 - DataCode Solutions
# ==============================================================================

# --- ETAPA 1: Importação de Bibliotecas Nativas ---
# Importamos o módulo math para reutilizar funções matemáticas otimizadas
import math

# --- ETAPA 2: Entrada e Validação de Dados Inteiros ---
# Capturamos a entrada do usuário através da função input() e aplicamos a função int() 
# para realizar o casting (conversão explícita) dos dados do formato textual (string) 
# para um número inteiro (int), garantindo a integridade do dado para operações matemáticas.
numero_escolhido = int(input("Digite um número inteiro entre 1 e 10 para o cálculo do fatorial: "))

# --- ETAPA 3: Processamento e Aplicação do Cálculo de Fatorial ---
# Invocamos a função própria .factorial() pertencente ao escopo da biblioteca math
resultado_fatorial = math.factorial(numero_escolhido)

# --- ETAPA 4: Saída de Dados Formatada ---
# Exibimos o resultado final concatenando as variáveis via f-string na saída do terminal
print(f"O fatorial de {numero_escolhido} é {resultado_fatorial}.")