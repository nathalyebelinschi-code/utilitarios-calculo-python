# ==============================================================================
# Script: conversor_temperatura.py
# Propósito: Converter uma temperatura de graus Celsius para Fahrenheit
# Contexto: Experiência Prática 1 - DataCode Solutions
# ==============================================================================

# --- ETAPA 1: Captura de dados e conversão explícita (Casting) ---
# A função input() recebe a entrada do usuário estritamente como formato string.
# Envolvemos essa captura com a função float() para realizar o casting (conversão
# explícita de tipos), transformando o texto digitado em um número decimal, 
# mitigando erros lógicos e permitindo o posterior processamento aritmético.
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# --- ETAPA 2: Processamento e Aplicação da Fórmula Matemática ---
# Realiza o cálculo de conversão respeitando as regras de precedência de operadores.
# Multiplicação e divisão ocorrem primeiro, seguidas pela adição. Isolamos a 
# fração (9 / 5) entre parênteses para otimizar a legibilidade do código estruturado.
temperatura_fahrenheit = (temperatura_celsius * (9 / 5)) + 32

# --- ETAPA 3: Saída de Dados Formatada ---
# Exibe a resposta final na saída padrão (terminal) utilizando f-strings.
# Aplicamos o especificador de formato ":.2f" dentro das chaves para delimitar
# a exibição do resultado de ponto flutuante a exatamente duas casas decimais.
print(f"A temperatura convertida é {temperatura_fahrenheit:.2f} graus Fahrenheit.")