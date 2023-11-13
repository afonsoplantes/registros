

class Motor():

    def __init__(self):
        print("classe carregada")
        self.__countMotor = 0
        self.__dicMotores = dict()

    def addMotor(self, local: str, identificacao: str, tag: str, potCV: int, potKW: float, tensao: float, corrente: float, rpm: int):
        dados = {'index': self.__countMotor,
                 'local': local,
                 'identificacao': identificacao,
                 'tag': tag, 
                 'potCV': potCV, 
                 'potKW': potKW, 
                 'tensao': tensao, 
                 'corrente': corrente, 
                 'rpm': rpm}
        self.__dicMotores[self.__countMotor] = dados
        self.__countMotor += 1
    
    def printMotores(self) -> str:
        for i in self.__dicMotores:
            print(self.__dicMotores[i])
    


dados = Motor()
dados.addMotor('destilaria', 'reserva', "kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'bomba de ácido', "kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)

dados.printMotores()