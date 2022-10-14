import csv

class ProccessFile:
    def __init__(self, url):
       self.url = url
       
       self.process_data(self.url)
       
       
    def sort_fn_object(self, dict):
        return dict['rating_count_tot']


    def append_data(self, data, items):
        items.append({
            'id_file': int(data[0]),
            'id_track': int(data[1]),
            'track_name': str(data[2]),
            'size_bytes': int(data[3]),
            'prime_genre': str(data[12]),
            'rating_count_tot': int(data[6]),
        })
            
        items.sort(key=self.sort_fn_object, reverse=True)
        
        
    def process_data(self, file):
        items = []
        with open(file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[12] == 'Book' or row[12] == 'Music':
                    self.append_data(row, items)
        return items[:10]
    
    
    def generate_document(self, _data):
        _header = ['id_file', 'id_track', 'track_name', 'size_bytes', 'prime_genre', 'rating_count_tot', 'n_citacoes']
        
        with open('./csv_files/extract_data_twitter.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=_header)
            writer.writeheader()
            writer.writerows(_data)
            
            print('Arquivo CSV gerado com sucesso !')
            
        