import sys
sys.path.append('/home/pmartinez/Aprendizado')
from ImportsDependent import *
from Chrome import Chrome


class ElementFunctions:

    # Click Elements
    def clickElement(self, by, position, timeout=15):
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((by, position))
            ).click()
            return element
        
        except Exception as e:
            print(f"Desculpe, erro ao acessar o elemento {position}: houve um erro: {str(e)}")

    # Functions for Acess Sector LICENCE

   
    # Functions for Acess Sector


class Licence(ElementFunctions):

    # Browser Inicialization
    browser = Chrome()
        # def __init__(self, 
        #         centroCusto= None, Equipamento = None, 
        #         contrato = None, cliente = None, 
        #         distribuidor = None, versão = None,
        #         produto = None, chaveProduto = None,
        #         quantidade = None, valorUnitario = None,
        #         numeroPedido = None, dataPedido = None,
        #         dataAquisicao = None, dataAtivacao = None,
        #         dataVencimento = None, licencaOperacional = None):
        #     self.centroCusto = centroCusto
        #     self.Equipamento = Equipamento
        #     self.contrato = contrato
        #     self.cliente = cliente
        #     self.distribuidor = distribuidor
        #     self.versão = versão
        #     self.produto = produto
        #     self.chaveProduto = chaveProduto
        #     self.quantidade = quantidade
        #     self.valorUnitario = valorUnitario
        #     self.numeroPedido = numeroPedido
        #     self.dataPedido = dataPedido
        #     self.dataAquisicao =dataAquisicao
        #     self.dataAtivacao = dataAtivacao
        #     self.dataVencimento = dataVencimento
        #     self.licencaOperacional = licencaOperacional

    

    # Login test 
    if browser.Login():
        def EditLicence(self):
            return self.browser.clickLicence()
            
        ## EDITLICENCE
        def clickLicences(self):
            self.clickElement(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[1]')

            self.clickElement(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[2]/div')

            self.clickElement(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/button')
            
            self.clickElement(By.XPATH, '//*[@id="react-select-undefined"]/div/div[1]/div[2]')
                    
            
 

if __name__ == '__main__':
    Test = Licence()
    Test.clickLicences()