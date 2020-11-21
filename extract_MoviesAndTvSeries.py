# numero film 7998
# scriverlo a mo di script

import requests
from pandas import DataFrame

# trovare altro modo per scrivere url
# scaricare anche serie tv 
# immagini sia per film che per serie tv


 
api_key='0a11e794490331ffaf9f0fdb167a701e'
params = {'address':'italy'}
genres_list = [] # lista generi
id_to_search_image = []


def getAllMovies(): # top rated permette di prendere tutti i film ordinati per il parametro rate
        # sistemare
    list_to_write = []
    data_pages = []
    for p in range(5,9): # 400 è il numero di pagine
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=en-US&page={p}"
        res_body = requests.get(url=url,params = params )
        data_j = res_body.json()
        data_pages.append(data_j["results"])

            
        print(str(p)+"\n")

    for dp in data_pages:
        for d in dp: # c'è la possibilità di mettere anche il voto che hanno dato sul sito
        
            genres = getGenres(d["genre_ids"])
        
            row = {"title":d["title"],"release_date":d["release_date"],"genres":genres,"popularity":d["popularity"]}
            list_to_write.append(row)
            id_to_search_image.append(d["id"])
    

    print(list_to_write)    
    
    pass 

def getGenres(g_ids): # gli passo la lista genr_ids e ritorna i genere
        ret_genrs = []
        
        for id in g_ids:
            for g in genres_list:
                if(id == g["id"]):
                    ret_genrs.append(g["name"])
                    break
        
        return ret_genrs
    

            

def fillGenres(): # scarica tutti i generi da mappare con genr_ids di getAllMovies()
        url = "genre/movie/list?api_key="+api_key+"&language=it-IT"
        url="https://api.themoviedb.org/3/genre/movie/list?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT"
        
        res_body = requests.get(url = url,params = params)
        data_j = res_body.json()
        genres = data_j["genres"] # prendo generi

        for g in genres: 
            genres_list.append({"id":g["id"], "name":g["name"]})
        

def getAllSeries():
    data_pages = []
    list_to_write = []
    for p in range(5,9): # 70 pagine
        url = f"https://api.themoviedb.org/3/tv/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT&page={p}"
        res_body = requests.get(url=url,params = params)
        data_j = res_body.json()
        data_pages.append(data_j["results"])

            
    print(str(p)+"\n")
    for dp in data_pages:
        for d in dp:# c'è la possibilità di mettere anche il voto che hanno dato sul sito
            
             genres = getGenres(d["genre_ids"])
        
        
             row = {"name":d["name"],"first_air_date":d["first_air_date"],"genres":genres,"popularity":d["popularity"]
                ,"origin_country":d["origin_country"],"original_language":d["original_language"]}
             list_to_write.append(row)
             id_to_search_image.append(d["id"])
            
    print(list_to_write)    
    
    
    pass

def writeToCvs():
        pass
    
    



if __name__ == "__main__":
    
    fillGenres()
    #getAllMovies()
    getAllSeries()