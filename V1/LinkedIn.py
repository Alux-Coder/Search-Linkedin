from linkedin_api import Linkedin
import time

#Info-Base

email = "youemail@gmail.com"
password = "********"
Debtor = "Alexsander de abreu Mendonça"
Debtor2 = "Microsoft"

link = Linkedin(email, password)

#Busca pelo devedor

class Find_Debtor():

    def Debtor_people(self, debtor):
        print('Pesquisando Devedor...')
        Search_Debtor = link.search_people(debtor)
        List_peoples = []

        for peoples in range(0, len(Search_Debtor)):
            print('Pesquisando devedor: ', Search_Debtor[peoples]['name'])
            Data_Debtor = link.get_profile(urn_id=Search_Debtor[peoples]['urn_id'])
            List_peoples.append(Data_Debtor)

        print('Finalizado, encontrado ', len(Search_Debtor))

        return List_peoples
        
    def Debtor_company(self, debtor):
        print('Pesquisando Devedor...')
        Search_Debtor = link.search_companies(debtor)
        List_company = []

        for company in range(0, len(Search_Debtor)):
            print('Pesquisando devedor: ', Search_Debtor[company]['name'])
            Data_Debtor = link.get_profile(urn_id=Search_Debtor[company]['urn_id'])
            List_company.append(Data_Debtor)

        print('Finalizado, encontrado ', len(Search_Debtor))

        return List_company

test = Find_Debtor()
print(test.Debtor_people(debtor=Debtor))
time.sleep(10)
print(test.Debtor_company(debtor=Debtor2))