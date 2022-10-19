class cliente:
    def __init__(self,nome):
        self.__nome=nome
    def get_nome(self):
        return self.__nome.title()

Cliente=cliente("pedro")
print(Cliente.get_nome())