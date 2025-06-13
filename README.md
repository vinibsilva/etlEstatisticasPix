-----

# **Transações Pix por Município**

Este repositório contém uma análise sobre os dados relacionados as trasações Pix por Município, 

-----

## Parâmetros de Consulta

Para acessar os dados, você pode utilizar os seguintes parâmetros:

  * **`DataBase`** (texto): Define a data-base para a consulta no formato `AAAAMM`.
  * **`$format`** (texto): Especifica o tipo de conteúdo de retorno.
  * **`$select`** (texto): Seleciona as propriedades a serem retornadas.
  * **`$filter`** (texto): Aplica filtros de seleção de entidades (por exemplo, `Nome eq 'João'`). Consulte as opções de operadores e funções [aqui](https://www.google.com/search?q=link-para-operadores-e-funcoes).
  * **`$orderby`** (texto): Ordena as entidades pelas propriedades especificadas (por exemplo, `Nome asc, Idade desc`).
  * **`$skip`** (inteiro): Define o índice inicial (maior ou igual a zero) da primeira entidade a ser retornada.
  * **`$top`** (inteiro): Define o número máximo (maior que zero) de entidades a serem retornadas.

-----

## Estrutura do Resultado

A consulta retornará os seguintes campos:

  * **`AnoMes`** (inteiro): Data-base no formato `AAAAMM`.
  * **`Municipio_Ibge`** (inteiro): Código IBGE do município.
  * **`Municipio`** (texto): Nome do município.
  * **`Estado_Ibge`** (inteiro): Código IBGE do estado.
  * **`Estado`** (texto): Nome do estado.
  * **`Sigla_Regiao`** (texto): Sigla da Região.
  * **`Regiao`** (texto): Região do país (Norte, Nordeste, Sul, Sudeste e Centro-Oeste).
  * **`VL_PagadorPF`** (decimal): Volume financeiro em R$ das transações cujo pagador é uma pessoa física (PF).
  * **`QT_PagadorPF`** (decimal): Quantidade de transações cujo pagador é uma pessoa física (PF).
  * **`VL_PagadorPJ`** (decimal): Volume financeiro em R$ das transações cujo pagador é uma pessoa jurídica (PJ).
  * **`QT_PagadorPJ`** (decimal): Quantidade de transações cujo pagador é uma pessoa jurídica (PJ).
  * **`VL_RecebedorPF`** (decimal): Volume financeiro em R$ das transações cujo recebedor é uma pessoa física (PF).
  * **`QT_RecebedorPF`** (decimal): Quantidade de transações cujo recebedor é uma pessoa física (PF).
  * **`VL_RecebedorPJ`** (decimal): Volume financeiro em R$ das transações cujo recebedor é uma pessoa jurídica (PJ).
  * **`QT_RecebedorPJ`** (decimal): Quantidade de transações cujo recebedor é uma pessoa jurídica (PJ).
  * **`QT_PES_PagadorPF`** (decimal): Quantidade de pagadores pessoas físicas.
  * **`QT_PES_PagadorPJ`** (decimal): Quantidade de pagadores pessoas jurídicas.
  * **`QT_PES_RecebedorPF`** (decimal): Quantidade de recebedores pessoas físicas.
  * **`QT_PES_RecebedorPJ`** (decimal): Quantidade de recebedores pessoas jurídicas.