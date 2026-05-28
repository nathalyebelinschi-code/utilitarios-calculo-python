# 🧮 Utilitários de Cálculo em Python — DataCode Solutions

Este repositório contém os utilitários de cálculo desenvolvidos em Python como parte da Experiência Prática da graduação em Análise e Desenvolvimento de Sistemas. O projeto simula o cenário de atuação de uma Programadora Júnior na equipe de Suporte a Cálculos da empresa fictícia DataCode Solutions, focando na integridade e transformação de dados primitivos.

## 🚀 Funcionalidades

O projeto é dividido em scripts independentes para atender a requisitos operacionais específicos:

* **Requisito A (Calculadora de Conversão de Medidas):** Um utilitário que recebe uma temperatura em graus Celsius informada pelo usuário, realiza a conversão explícita de tipos (*casting* de String para Float) para garantir o processamento numérico e exibe o resultado formatado em Fahrenheit com precisão de duas casas decimais.
* **Requisito B (Cálculo de Fatorial Simples):** Utilitário que captura um número inteiro (preferencialmente entre 1 e 10) e calcula o seu fatorial de forma otimizada utilizando as funções nativas do módulo `math`, abstraindo a complexidade de laços de repetição manuais.

## 🛠️ Conceitos Praticados
* Entrada e saída padrão de dados (`input()` e `print()`)
* Conversão explícita de tipos primitivos (*Casting* de String para Float e String para Int)
* Importação e consumo de bibliotecas nativas (`import math`)
* Precedência de operadores aritméticos
* Formatação de strings (*f-strings* e especificadores de casas decimais)
* Padronização de código conforme as boas práticas da PEP 8 (convenção *snake_case*)

## 🗂️ Estrutura do Projeto

* `conversor_temperatura.py`: Script responsável pela conversão de escalas de temperatura.
* `calculo_fatorial.py`: Script responsável pelo processamento do cálculo de fatorial.
* `README.md`: Documentação técnica do projeto.

## 📦 Como Executar o Projeto

Este projeto utiliza o **uv** (um gerenciador de pacotes e ambientes Python ultra-rápido desenvolvido pela Astral). 

1. Certifique-se de ter o `uv` ou o Python instalado em sua máquina.
2. Clone o repositório:
```bash
git clone https://github.com/nathalyebelinschi-code/utilitarios-calculo-python.git
