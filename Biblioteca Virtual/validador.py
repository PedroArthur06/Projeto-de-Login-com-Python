import re

def validaCPF(cpf: str) -> bool:
  cpf = ''.join(filter(str.isdigit, cpf))
  if len(cpf) != 11:
    return False

  num1 = int(cpf[0])
  num2 = int(cpf[1])
  num3 = int(cpf[2])
  num4 = int(cpf[3])
  num5 = int(cpf[4])
  num6 = int(cpf[5])
  num7 = int(cpf[6])
  num8 = int(cpf[7])
  num9 = int(cpf[8])
  num10 = int(cpf[9])
  num11 = int(cpf[10])

  if (num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8 == num9 == num10 == num11):
        return False

  soma1 = num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 + num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2
  resto1 = (soma1 * 10) % 11
  if resto1 == 10:
    resto1 = 0

  soma2 = num1 * 11 + num2 * 10 + num3 * 9 + num4 * 8 + num5 * 7 + num6 * 6 + num7 * 5 + num8 * 4 + num9 * 3 + num10 * 2
  resto2 = (soma2 * 10) % 11
  if resto2 == 10:
    resto2 = 0

  if (resto1 == num10) and (resto2 == num11):
    return True
  else:
    return False


def validaEmail(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))


def validaSenha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
    if not re.search(r'[A-Z]', senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")
    if not re.search(r'[a-z]', senha):
        erros.append("A senha deve conter pelo menos uma letra minúscula.")
    if not re.search(r'\d', senha):
        erros.append("A senha deve conter pelo menos um dígito.")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', senha):
        erros.append("A senha deve conter pelo menos um caractere especial.")

    if erros:
        return False, erros
    return True, ["A senha é forte."]




