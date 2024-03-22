professores = []

def validate(data):
    # Validação do nome
    if not isinstance(data.get("name"), str):
        raise TypeError("O nome deve ser uma string.")
    
    # Validação do gênero
    if data.get("gender") not in ["M", "F"]:
        raise ValueError("Gênero inválido. Deve ser 'M' ou 'F'.")
    
    # Validação do RG
    if not isinstance(data.get("rg"), str):
        raise TypeError("O RG deve ser uma string.")
    
    # Validação do CPF
    if not isinstance(data.get("cpf"), str):
        raise TypeError("O CPF deve ser uma string.")
    # Aqui você pode adicionar uma lógica para verificar se o CPF é válido
    
    # Validação do estado civil
    if data.get("maritalstatus") not in ["Solteiro", "Casado", "Divorciado", "Viúvo"]:
        raise ValueError("Estado civil inválido.")
    
    # Validação do endereço
    if not isinstance(data.get("address"), str):
        raise TypeError("O endereço deve ser uma string.")
    
    # Validação do estado
    if not isinstance(data.get("state"), str):
        raise TypeError("O estado deve ser uma string.")
    
    # Validação da cidade
    if not isinstance(data.get("city"), str):
        raise TypeError("A cidade deve ser uma string.")
    
    # Validação do telefone fixo

    
    if not isinstance(data.get("landline"), int):
        raise TypeError("O telefone fixo deve ser um número inteiro.")
    
    # Validação do telefone celular
    if not isinstance(data.get("phonenumber"), int):
        raise TypeError("O telefone celular deve ser um número inteiro.")
    
    # Validação do email
    if not isinstance(data.get("email"), str):
        raise TypeError("O email deve ser uma string.")
    # Aqui você pode adicionar uma lógica para verificar se o email é válido

    # Se todas as validações passarem, os dados são enviados
    send(data)

def send(data):
    professores.append(data)

def rightTest():
    data = {
        "name": "Joselito Junior Motta de Carvalho",
        "dateofbirth": "1990-01-01T00:00:00.000Z",
        "gender": "M",
        "rg": "123456789",
        "cpf": "12983127398",
        "maritalstatus": "Solteiro",
        "raceethnicity": "Branco",
        "address": "Rua A, 123",
        "state": "São Paulo",
        "city": "São Paulo",
        "landline": 11222233334,
        "phonenumber": 11999998888,
        "email": "joselito.junior@gmail.com"
    }

    try:
        validate(data)
        print('Dados enviados com sucesso!')
    except Exception as e:
        print('Ocorreu um erro durante a validação:', e)

def wrongTest():
    data = {
        "name": "Joselito Junior Motta de Carvalho",
        "dateofbirth": "1990-01-01T00:00:00.000Z",
        "gender": "M",
        "rg": "123456789",
        "cpf": "12983127398",
        "maritalstatus": "Solteiro",
        "raceethnicity": "Branco",
        "address": "Rua A, 123",
        "state": "São Paulo",
        "city": "São Paulo",
        "landline": '11222233334',
        "phonenumber": 11999998888,
        "email": "joselito.junior@gmail.com"
    }

    try:
        validate(data)
        print('Dados enviados com sucesso!')
    except Exception as e:
        print('Ocorreu um erro durante a validação:', e)

rightTest()
wrongTest()
