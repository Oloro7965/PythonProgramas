class equipamento:
    def __init__(self,a1,a2):
        self.__a1=a1
        self.__a2=a2
    def exibe(self):
        return f'{self.__a1}\n{self.__a2}'
    @property
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self,a1novo):
        self.__a1=a1novo
    @property
    def a2(self):
        return self.__a2
    @a2.setter
    def a2(self,a2novo):
        self.__a2=a2novo
class computador(equipamento):
    def __init__(self,a1,a2,b1,b2):
        super().__init__(a1,a2)
        self.__b1=b1
        self.__b2=b2
    @property
    def b1(self):
        return self.__b1
    @b1.setter
    def b1(self,b1novo):
        self.__b1=b1novo
    @property
    def b2(self):
        return self.__b2
    @b2.setter
    def  b2(self,b2novo):
        self.__b2=b2novo
    def exibe(self):
        return f'{self._equipamento__a1},{self._equipamento__a2},{self.__b1},{self.__b2}'
class testaequipamento:
    equip1 = equipamento(2, 28)
    equip2 = computador(34, 47, 12, 3)
    @classmethod
    def main(cls):
        return f'equip1\na1-{cls.equip1.a1}\na2-{cls.equip1.a2}\nequip2\na1-{cls.equip2.a1}\na2-{cls.equip2.a2}\nb1-{cls.equip2.b1}\nb2-{cls.equip2.b2}'
e1=computador(24,26,94,86)
print(e1.a1)
print(e1.exibe())
print(testaequipamento.main())