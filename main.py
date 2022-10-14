from controllers.controller import ProccessFile
from api.twitter_api import main
from db.connect_db import init_connection


class Init:
   def __init__(self, url):
       self.url = url
   
   def proccess_data(self):
        r = ProccessFile(self.url)
        proccessed_data = r.process_data(self.url)
        for i in proccessed_data:
            count = main(i['track_name'])
            i['n_citacoes'] = count['count']
        print('Requisição na API do Twitter feita com sucesso !')
        r.generate_document(proccessed_data)
        
        return proccessed_data

init = Init(url="./AppleStore.csv")

try:
    proccessed = init.proccess_data()
    
    init_connection(proccessed)
    
    print('JSON Gerado: ', proccessed)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not proccess data .CSV file.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    
    raise
