from ImportsDependent import *

## Constantes Globais
UrlDomain = "http://localhost:3000/"
load_dotenv(dotenv_path='variable.env')
LoginUser = os.getenv('LOGIN')

## Configuração do Navegador
options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Instancia a classe Service corretamente
service = Service(executable_path=ChromeDriverManager().install())
Browser = webdriver.Chrome(service=service, options=options)
Browser.get(UrlDomain)
actions = ActionChains(Browser)

## Script de Comando
Browser.maximize_window()

# Espera até que os campos estejam presentes e visíveis
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
elementLogin.send_keys(LoginUser)
elementPasswd.send_keys(os.getenv('PASSWORD'))

# Encontra e clica no botão de login
btn = Browser.find_element(By.TAG_NAME, 'button')
btn.click()

# Espera até que o próximo botão esteja presente e visível
licence = WebDriverWait(Browser, 15).until( EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[1]')) )
if (licence):
    licence.click()
    licences = WebDriverWait(Browser, 15).until( EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[2]/div')) )

    if (licences):
        licences.click()
        WebDriverWait(Browser, 15).until( EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/button')) ).click()
        input = WebDriverWait(Browser, 15).until( EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-undefined"]/div/div[1]/div[2]')) ).click()
        
        # Central de Custo*
        Keys.ARROW_DOWN
        Keys.ENTER
        Keys.TAB

        # Equipamento
        Keys.TAB

        # # Contrato
        # Keys.TAB
        
        # # Cliente*
        # Keys.TAB
        
        # # Distribuidor*
        # WebDriverWait(Browser, 15).until( EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-undefined"]/div/div[1]/div[2]')) ).click()
        
        # # Versão*
        # Keys.TAB
        # Keys.ENTER
        
        # # Produto
        
        
        # # Chave do Produto
        
        
        # # Quantidade*
        
        # # Valor Unitário
        
        # # Numero Pedido
        
        # # Data Pedido
        # Keys.TAB
        # Keys.TAB 
        # Keys.ENTER
        # Keys.ENTER
        # Keys.TAB 
        
        # # Data Aquisição*
        # Keys.TAB
        # Keys.TAB
        # Keys.ENTER
        # Keys.ENTER
        # Keys.TAB
        
        # # Data Ativação
        # Keys.TAB
        # Keys.TAB
        # Keys.ENTER
        # Keys.ENTER
        # Keys.TAB
        
        # # Data Vencimento
        # Keys.TAB
        # Keys.TAB
        # Keys.ENTER
        # Keys.ENTER
        # Keys.TAB
        
        # # Licença de Registro Operacional?
        # Keys.ENTER
        
    else:
        print("Nao acessou o botao licences!")
else:
    print("Nao acessou o botao licence!")

# Tempo de espera antes de fechar o navegador
time.sleep(10)

## Fecha o navegador
Browser.quit()
