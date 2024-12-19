from ImportsDependent import *

class Chrome:
    def __init__(self):
        load_dotenv(dotenv_path='variable.env')
        self.__UrlDomain = "http://localhost:3000/"
        self.__LoginUser = 'pmartinez'
    
    # def browser(self):
        chromeoptions = Options()
        chromeoptions.binary_location = "/usr/bin/google-chrome"
        chromeoptions.add_argument("--no-sandbox")
        chromeoptions.add_argument("--incognito")
        chromeoptions.add_argument("--disable-setuid-sandbox")
        chromeoptions.add_argument("--disable-dev-shm-usage")

        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chromeoptions)

        
    def Login(self):
        # Iniciando Browser
        try:
            self.driver.get(self.__UrlDomain)
            self.driver.maximize_window()


            # Preenche os campos de login
            WebDriverWait(self.driver, 15).until( EC.visibility_of_element_located((By.ID, 'formLoginUsuario')) ).send_keys(self.__LoginUser)
            WebDriverWait(self.driver, 15).until( EC.visibility_of_element_located((By.ID, 'formLoginPassword')) ).send_keys(os.getenv('PASSWORD'))

            # Encontra e clica no botão de login
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.TAG_NAME, 'button'))).click()

            # Tempo de espera antes de fechar o navegador
            time.sleep(10)

            return True
        except:
            print('Erro ao realizar o login')
            return False
        
        
if __name__ == '__main__':        
    navegador = Chrome()
    navegador.Login()
