# Teste de Validação de Dados de Professores

Este documento descreve um caso de teste para enviar e validar os dados de professores em uma lista. O teste consiste em dois cenários: um onde os dados estão corretos e outro onde há um erro de validação.

## Caso de Teste

### Objetivo
Inserir um professor em uma lista.

### Pré-condição
Os dados do professor devem ser fornecidos de acordo com o formato esperado.

### Procedimento de Teste
1. Chamar a função `validate` com os dados do professor.
2. Capturar exceções caso ocorram durante a validação.

### Resultado Esperado
- Se todos os dados estiverem corretos, os dados do professor devem ser inseridos na lista de professores.
- Se houver qualquer erro de validação, uma exceção deve ser levantada indicando o tipo de erro.

### Resultado Obtido
- No cenário onde os dados estão corretos, a mensagem "Dados enviados com sucesso!" deve ser impressa.
- No cenário onde há um erro de validação, a mensagem de erro correspondente deve ser impressa.

### Pós-condição
Os dados do professor devem ser inseridos na lista de professores apenas se passarem pela validação com sucesso.
