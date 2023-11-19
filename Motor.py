import os
import json

class Motor():

    def __init__(self, base_dados: str):
        """"
            base_dados -> Indicar apenas o caminho para carregar ou salvar a fonte de dados.
            Não colocar sufixos ex: .csv .json...
        """
        print("Inicializando a classe motores")
        self.__baseDados = base_dados
        self.__countMotor = 0
        self.__dicMotores = dict()
        self.__caminhoArquivoDados = os.path.join(self.__baseDados, "dados_motores.json")
        self.__loadDatabase()


    @property
    def conta_motores(self):
        return self.__countMotor
    
    @property
    def caminho_arquivo_dados_json(self):
        return self.__caminhoArquivoDados

    @property
    def dic_motores(self):
        return self.__dicMotores

    def __verificaCaminhodados(self, caminho_desejado):
        if not os.path.exists(caminho_desejado):
            print(f"Caminho {caminho_desejado} não existe.")
            return False          
        else:
            print(f"Caminho {caminho_desejado} já existe.")
            return True

    def __criarArvorePastas(self, caminho_desejado):
        os.makedirs(caminho_desejado)
        print(f"Caminho {caminho_desejado} criado com sucesso.")

    def __verificaArquivoDados(self):
        if os.path.exists(self.__caminhoArquivoDados):
            return True
        else:
            return False
        
    def __loadDatabase(self):
        print("Local da base de dados: {}".format(self.__baseDados))
        if not self.__verificaCaminhodados(self.__baseDados):
            self.__criarArvorePastas(self.__baseDados)
        if self.__verificaArquivoDados():
            with open(self.__caminhoArquivoDados, 'r') as arquivo_json:
                self.__dicMotores = json.load(arquivo_json)
                self.__countMotor = len(self.__dicMotores)

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

    @property
    def printMotores(self) -> str:
        for i in self.__dicMotores:
            print(self.__dicMotores[i])
    
    @property
    def salvaBaseDados(self):
        with open(self.__caminhoArquivoDados, 'w') as dados_motores:
            json.dump(self.__dicMotores, dados_motores)



caminho_atual = os.path.join(os.getcwd(), "base_dados")
dados = Motor(caminho_atual)

dados.addMotor('destilaria', 'reserva', "kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'bomba de ácido', "kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)
dados.addMotor('destilaria', 'Mexedor de algo',"kl123", 5, 3.5, 380, 7, 1800)

dados.printMotores

dados.salvaBaseDados



