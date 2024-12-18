from ImportsDependent import *

class Chrome:
    def __init__(self):
        load_dotenv(dotenv_path='variable.env')
        self.__UrlDomain = "http://localhost:3000/"
        self.__LoginUser = 'pmartinez'
    
    def browser(self):
        chromeoptions = Options()
        chromeoptions.binary_location = "/usr/bin/google-chrome"
        chromeoptions.add_argument("--no-sandbox")
        chromeoptions.add_argument("--incognito")
        chromeoptions.add_argument("--disable-setuid-sandbox")
        chromeoptions.add_argument("--disable-dev-shm-usage")

        service = Service(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chromeoptions)
        
    def Login(self):
        # Iniciando Browser
        Browser = Chrome().browser()
        Browser.get(self.__UrlDomain)
        
        WebDriverWait(Browser, 15).until(
            EC.visibility_of_element_located((By.ID, 'formLoginUsuario'))
        )
        WebDriverWait(Browser, 15).until(
            EC.visibility_of_element_located((By.ID, 'formLoginPassword'))
        )

        # Limpa os campos de login
        elementLogin = Browser.find_element(By.ID, 'formLoginUsuario')
        elementPasswd = Browser.find_element(By.ID, 'formLoginPassword')
        elementLogin.clear()
        elementPasswd.clear()

        # Preenche os campos de login
        elementLogin.send_keys(self.__LoginUser)
        elementPasswd.send_keys(os.getenv('PASSWORD'))

        # Encontra e clica no botão de login
        btn = Browser.find_element(By.TAG_NAME, 'button')
        btn.click()

        # Tempo de espera antes de fechar o navegador
        time.sleep(10)

        ## Fecha o navegador
        Browser.quit()
        
        
if __name__ == '__main__':        
    Chrome().Login()
