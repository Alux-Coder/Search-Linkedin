import undetected_chromedriver as uc
from undetected_chromedriver import By
import random
import time

email = "youemail@gmail.com"
password = "********"

Devedor = str(input('Declare o devedor: '))
Company = str(input('Empresa: S/N? '))

print('Abrindo Navegador...')

chromedriver_path = "D:\\Projects\\Projects_Cobrance\\Search Linkedin\\drivers\\chromedriver.exe"

driver = uc.Chrome(
    driver_executable_path=chromedriver_path, headless=True, use_subprocess=True
)

web = 'https://www.linkedin.com'

driver.get(url=web)

print('Logando...')
time.sleep(random.randint(3, 7))
Botão = '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button'
input_email = driver.find_element(By.ID, 'session_key')
input_password = driver.find_element(By.ID, 'session_password')
login_button = driver.find_element(By.XPATH, Botão)

time.sleep(random.randint(2, 4))
input_email.send_keys(email)
time.sleep(random.randint(1, 2))
input_password.send_keys(password)
time.sleep(random.randint(2, 4))
login_button.click()


print('Logado!!!')

time.sleep(random.randint(2, 4))
Devedor = Devedor.replace(' ', '%20')

print('Pesquisando devedor...')
if Company == 's':
    url_pesquisa = web + f'/search/results/companies/?keywords={Devedor}'
elif Company == 'n':
    url_pesquisa = web + f'/search/results/people/?keywords={Devedor}'
else:
    url_pesquisa = web + f'/search/results/all/?keywords={Devedor}'

driver.get(url=url_pesquisa)
list_urn = []

for resultados in range(1, 10):
    path_element_urn = f"/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{resultados}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a"
    try :
        href = driver.find_element(By.XPATH, path_element_urn).get_attribute('href')
        list_urn.append(href)
        print('Link: ', href, '\n')
    except:
        try:
            path_element_urn = f"/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{resultados}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a"
            href = driver.find_element(By.XPATH, path_element_urn).get_attribute('href')
            list_urn.append(href)
            print('Link: ', href, '\n')
        except:
            print('Não encontrado')
        pass

print(f'Localizado {len(list_urn)} perfis \n')
print(f'Raspando {len(list_urn)} perfis \n')

for perfis in range(0, len(list_urn)):
    if Company == 's':
        driver.get(list_urn[perfis] + '/about/')
        time.sleep(5)

        #Nome
        try:
            name_xpath = "/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div/h1"
            nome = driver.find_element(By.XPATH, name_xpath).text
            print(nome)
        except:
            try:
                name_xpath = "/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div/h1"
                nome = driver.find_element(By.XPATH, name_xpath).text
                print(nome)
            except:
                print('Não encontrado nome do perfil')
            pass

        #Sobre (para empresas)
        Title_cont, Sub_cont = 0, 0
        limit_try = 0
        while True:
            Title_cont += 1 
            Sub_cont += 1
            if limit_try < 6:
                try:
                    title_xpath = f"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dt[{Title_cont}]"
                    subtext_xpath = f"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[{Sub_cont}]"
                    try:
                        Site_Company = driver.find_element(By.XPATH, subtext_xpath+'/a/').get_attribute('href')
                        print('Site: ' + '\n' + Site_Company)
                    except:
                        pass
                    Titulo = driver.find_element(By.XPATH, title_xpath).text
                    Subtext = driver.find_element(By.XPATH, subtext_xpath).text
                    if Titulo == 'Tamanho da empresa':
                        print(Titulo + ': ' + '\n' + Subtext)
                        Sub_cont += 1
                        subtext_xpath = f"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[{Sub_cont}]"
                        Subtext = driver.find_element(By.XPATH, subtext_xpath).text
                        print(Subtext)
                    else:
                        print(Titulo + ': ' + '\n' + Subtext)
                except:
                    try:
                        title_xpath = f"/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dt[{Title_cont}]"
                        subtext_xpath = f"/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[{Sub_cont}]"
                        try:
                            Site_Company = driver.find_element(By.XPATH, subtext_xpath+'/a/').get_attribute('href')
                            print('Site: ' + '\n' + Site_Company)
                        except:
                            pass
                        Titulo = driver.find_element(By.XPATH, title_xpath).text
                        Subtext = driver.find_element(By.XPATH, subtext_xpath).text
                        if Titulo == 'Tamanho da empresa':
                            print(Titulo + ': ' + '\n' + Subtext)
                            Sub_cont += 1
                            subtext_xpath = f"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[{Sub_cont}]"
                            Subtext = driver.find_element(By.XPATH, subtext_xpath).text
                            print(Subtext)
                        else:
                            print(Titulo + ': ' + '\n' + Subtext)
                    except:
                        limit_try += 1
            else:
                break


    else:
        link = str(list_urn[perfis])
        link = link[0:link.find('?')]
        print('Raspando perfil: ' + link)
        driver.get(link + '/overlay/contact-info/')
        time.sleep(5)

        #Nome
        try:
            nome = driver.find_element(By.ID, 'pv-contact-info').text
            print(nome)
            
        except:
            print('Não localizado contatos')

        #Contatos
        seleções = driver.find_elements(By.CLASS_NAME, 'pv-contact-info__contact-type')
        print(str(len(seleções)) + ' seleções encontradas.\n')
        if len(seleções) > 1:
            for seleção in range(1, len(seleções)+1):
                #email
                title_xpath = f'/html/body/div[3]/div/div/div[2]/section/div/section[{seleção}]/h3'
                Titulo = driver.find_element(By.XPATH, title_xpath).text
                try:
                    match Titulo:

                        case 'E-mail':
                            email_xpath = f'/html/body/div[3]/div/div/div[2]/section/div/section[{seleção}]/div/a'
                            email = driver.find_element(By.XPATH, email_xpath).text
                            print('O email é ' + email + '\n')

                        case 'telefone':
                            tel_xpath = f'/html/body/div[3]/div/div/div[2]/section/div/section[{seleção}]/ul/li/span[1]'
                            telefone = driver.find_element(By.XPATH, tel_xpath).text
                            print('O telefone é ' + telefone + '\n')

                        case 'site':
                            try:
                                site_path = f'/html/body/div[3]/div/div/div[2]/section/div/section[{seleção}]/ul/li/a'
                                site = driver.find_element(By.XPATH, site_path).get_attribute('href')
                                print('O site é ' + site + '\n')
                            except:
                                for sites in range(1, len(seleções)):
                                    try:
                                        site_path = f'/html/body/div[3]/div/div/div[2]/section/div/section[{seleção}]/ul/li[{site}]/a'
                                        site = driver.find_element(By.XPATH, site_path).get_attribute('href')
                                        print('O site é ' + site + '\n')
                                    except:
                                        pass

                        case _:
                            pass
                except:
                    print('Erro na localização\n')
        else:
            print('Sem dados uteis para raspagem')

