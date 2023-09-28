from documento import Documento

print("\n\033[1m{:=^60} \033[m \n".format(" Consulta de documentos [CPF / CNPJ] "))

while True:
    print("-" * 60)
    doc = str(input("\nDigite o número do documento: "))
    print()
    documento = Documento.cria_documento(doc)
    print(documento)
    print("\nConsulta finalizada...")
    nova_consulta = str(input("\nDeseja consultar outro documento [S/N]? ")).strip().upper()[0]
    if nova_consulta == "N":
        break

print("\n\033[1m{:=^60} \033[m \n".format(" Consulta de documentos finalizada "))
