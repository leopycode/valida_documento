from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            print("O número digitado é um CPF.")
            return DocCpf(documento)
        elif len(documento) == 14:
            print("O número digitado é um CNPJ.")
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
            print("CPF validado com sucesso.")
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
      mascara = CPF()
      return f"CPF: {mascara.mask(self.cpf)}"

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
            print("CNPJ validado com sucesso.")
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)

    def format(self):
        mascara = CNPJ()
        return f"CNPJ: {mascara.mask(self.cnpj)}"