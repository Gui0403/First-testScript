import sys
sys.path.append('/home/pmartinez/Aprendizado')
from ImportsDependent import *
from Chrome import Chrome


class ElementFunctions:
    def __init__(self, browser): 
        self.browser = browser
    # browser = Chrome()
    # browser.Login()
    
    # Functions for Acess Sector LICENCE
    def clicklicense(self):
        try: 
            print("Tentando clicar no elemento de licença...") 
            element = WebDriverWait(self.browser, 15).until( EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div')) ) 
            element.click() 
            print("Elemento de licença clicado com sucesso!") 
        except Exception as e: 
            print(f"Desculpe, erro ao acessar o elemento de licença: {str(e)}")

    # def clicklicences(self):
    #     element = WebDriverWait(self.browser, 15).until(
    #              EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[2]/div'))
    #         )
    #     element.click()
    #     return element
    
    # def clickBtnLicences(self):
    #     element = WebDriverWait(self.browser, 15).until(
    #              EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[7]/div/button[1]'))
    #         )
    #     element.click()
    #     return element
    
    # def clickInputLicences(self):
    #     element = WebDriverWait(self.browser, 15).until(
    #              EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-undefined"]/div/div[1]/div[2]'))
    #         )
    #     element.click()
    #     return element

    # Functions for Acess Sector
    
class Licence(ElementFunctions):
    def __init__(self, browser): 
        super().__init__(browser)
        

    ## EditLicence
    def EditLicence(self):
        self.clicklicense()
    
 

if __name__ == '__main__':
    navegador = Chrome()
    if navegador.Login():
        Test = Licence(navegador.driver)






    # Browser Inicialization
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