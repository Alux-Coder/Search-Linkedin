from fastapi import FastAPI
from Search_Linkedin import Linkedin

app = FastAPI()

@app.get('/find_debtor/{opt_search}/{name_debtor}/access_credentials/{email}/{password}')
def Search_Linkedin(opt_search: str, name_debtor: str, email: str, password: str):
    
    pesquisa = Linkedin.Search(email=email, password=password, debtor=name_debtor, opt=opt_search, headless_opt=True)

    return pesquisa