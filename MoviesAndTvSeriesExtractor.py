# numero film 7998
# scriverlo a mo di script

# per esportazione mongo -> cvs : https://www.quackit.com/mongodb/tutorial/mongodb_export_data.cfm#:~:text=To%20export%20to%20a%20CSV,collection%20to%20a%20CSV%20file.

import requests
from pandas import DataFrame
import pymongo
from pymongo import MongoClient
from datetime import datetime
import shutil
import json


client = MongoClient('mongodb://localhost:27017/')

DomainData = client["Domain_Data"] 

Movies_collection = DomainData["Movies"]
TvSeries_collection = DomainData["TvSeries"]

 
api_key='0a11e794490331ffaf9f0fdb167a701e'
params = {'address':'italy'}
genres_list = [] # lista generi

id_series = []


seasons = []

# link doc : https://developers.themoviedb.org/3/movies/get-top-rated-movies

def getAllMovies(): # top rated permette di prendere tutti i film ordinati per il parametro rate
        # sistemare
    list_to_write = []
    data_pages = []
    for p in range(1,400): # 400 è il numero di pagine
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT&page={p}"
        res_body = requests.get(url=url,params = params ) #
        
        if(res_body.status_code != 200):
            print(f"page {p} failed \n")
            continue
        
        data_j = res_body.json()
        
        data_pages.append(data_j["results"])

            
        print(f"page {p} done \n")


    for dp in data_pages:
        for d in dp: # c'è la possibilità di mettere anche il voto che hanno dato sul sito
        
            genres = getGenres(d["genre_ids"])
        
            row = {"id":d["id"],"title":d["title"],"release_date":d["release_date"],
                    "genres":genres,"popularity":d["popularity"],
                    "poster_path":d["poster_path"],"backdrop_path":d["backdrop_path"]}
            
            list_to_write.append(row)
            Movies_collection.insert_one(row)
            

    print("Collecting film done \n")    
    #print(json.dumps(list_to_write, indent=4, default=str))
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
        
# link doc : https://developers.themoviedb.org/3/tv/get-top-rated-tv
def getAllSeries2():
    # 1 itero sulle pagine
        # 2 itero sui risultati della pagina
            # 3 creo livello tv_serie
                # 4 prendo tutte le season
                    # 5 itero sulle season e prendo gli episodi
    List_SerieTV = []
    c = 0
    for page in range(1,74): # 1
        
        url = f"https://api.themoviedb.org/3/tv/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT&page={page}"
        res_body = requests.get(url=url,params=params)
        print(f"page {page} \n")
        if res_body.status_code != 200 :
                    print("break page")
                    break 

        data_page = res_body.json()
        data_page = data_page["results"] # risultato di 1 pagina
       
        for tvS in data_page: # 2
            c = c+1
           # print("Tvs "+ str(c) +"\n")
           
            genres = getGenres(tvS["genre_ids"])
            try:
                Serie_Tv = {"id_tv_series":tvS["id"],"name_tv_series":tvS["name"],"first_air_date":tvS["first_air_date"],"genres":genres,"popularity":tvS["popularity"]
                ,"origin_country":tvS["origin_country"],
                "original_language":tvS["original_language"],"poster_path":tvS["poster_path"],"seasons":[]}
            except:
                print(f"error in serie {tvS['id']}")
                print(tvS)
                continue

            # prendo le stagioni
            url = f"https://api.themoviedb.org/3/tv/{tvS['id']}?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT" 
            
            res_body = requests.get(url=url,params=params)
            if res_body.status_code != 200 :
                    print(f"break stagioni {res_body.status_code}, url = {url} \n")
                    continue 
            data_season = res_body.json()
            data_season = data_season["seasons"]

            seasons = []

        
            for seas in data_season: # 3
                
                s = ({"season_id": seas['id'],
                "season_name":seas['name'],"n_episode":seas['episode_count'],
                "season_number":seas["season_number"],"url_image":seas["poster_path"],"episodes":[]})

                # prendo le puntate per ogni stagione 

                url = f"https://api.themoviedb.org/3/tv/{tvS['id']}/season/{seas['season_number']}?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT"
                
                #print(f"id : {tvS['id']} season : {seas['season_number']} \n")

                res_body = requests.get(url=url,params=params)
                if res_body.status_code != 200 :
                    print(f"break episodes {res_body.status_code}, url = {url}")
                    continue
                data_episodes = res_body.json()
                data_episodes = data_episodes["episodes"]
                
              

                episodes = []

                for ep in data_episodes: # 4 prendo solo qualche info sugli episodi
                    episodes.append({"episode_number":ep["episode_number"],"image_path":ep["still_path"]})
                               
                s["episodes"] = episodes
                seasons.append(s)
            
            Serie_Tv["seasons"] = seasons
            List_SerieTV.append(Serie_Tv)
        # al posto della riga sopra 
            res = TvSeries_collection.insert_one(Serie_Tv)
        
            print(f" {c}) name : {Serie_Tv['name_tv_series']} res.ack = {res.acknowledged} \n")
        
    # print(json.dumps(List_SerieTV, indent=4, default=str))
    print(f"tot number rows: {len(List_SerieTV)} = {c} \n")
       
                

def getAllSeries(): 
    data_pages = []
    list_to_write = []
    for p in range(5,9): # itero sulle pagine, 70 
        url = f"https://api.themoviedb.org/3/tv/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT&page={p}"
        res_body = requests.get(url=url,params = params)
        data_j = res_body.json()
        data_pages.append(data_j["results"])

            
    
    for dp in data_pages: # itero sulle pagine
        for d in dp:# c'è la possibilità di mettere anche il voto che hanno dato sul sito
            
             genres = getGenres(d["genre_ids"])
        
        
             row = {"id_tv_series":d["id"],"name":d["name"],"first_air_date":d["first_air_date"],"genres":genres,"popularity":d["popularity"]
                ,"origin_country":d["origin_country"],
                "original_language":d["original_language"],"poster_path":d["poster_path"],"seasons":[]}
             
             list_to_write.append(row)
             
    #print(list_to_write)    
    
    print(f"\n numero di serie tv trovate : {len(list_to_write)} ,extract seasons for each tv series \n")
    


    # per ogni serie_id devo estrarre il numero di stagioni e puntate
    for r in list_to_write:
        print("a")
        url = f"https://api.themoviedb.org/3/tv/{r['id']}?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT"
        res_body = requests.get(url=url,params=params)
        data_j = res_body.json()
        
        seasons_t = data_j['seasons']
        season_id = []
        for s in seasons_t: # dati necessari per trovare gli episodi per ogni stagione 
            season_id.append({"id_tv" : r['id'], "season_id": s['id'],
                "season_name":s['name'],"n_episode":s['episode_count'],
                "season_number":s["season_number"],"url_image":s["poster_path"]})
        
        
        seasons.append(season_id)
        season_id = []

    #print(seasons)
    #season lista di liste = [[lista episodi serie_1],[lista episodi serie_2],...,[lista episodi serie_n]] 
    #estrarre episodi per ogni serie tv 
    episode = []
    for l in seasons: # scorro sulla stagione della serie
        print(f"l : {l}")
        for e in l:# per ogni stagione prendo episodio
            print(f"e : {e}")
            url = f"https://api.themoviedb.org/3/tv/{e['id_tv']}/season/{e['season_number']}?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT"
            body_j = requests.get(url = url,params=params)
            data_j = body_j.json()
            epi = data_j["episodes"]
            episode.append({"id_tv":e['id_tv'],"season_number":e['season_number'],
                            "episode_number":epi["episode_number"],"image_path":epi["still_path"]})
    
    print(episode)
    pass



def getMoviesImage():

   # prendo tutti i film, poster path e backdrop path

   for movie in Movies_collection.fin({},{"_id":0,"title":1,"poster_path":1,"backdrop_path":1}) :

       if(movie["poster_path"] != ''):
           img_url = f"https://image.tmdb.org/t/p/original{movie['poster_path']}"
           name = f"poster_{movie['title']}.png" 
           # request immagine
           pass
       
       if(movie["backdrop_path"] != '')
           img_url = f"https://image.tmdb.org/t/p/original{movie['backdrop_path']}"
           name = f"backdrop_{movie['title']}.png" 
           
           pass
       
       print(f"{}")

   img_url = "https://image.tmdb.org/t/p/original/zCKmhauiC5RY8uPkM7Ss2TtGrxD.jpg"
   name_img = "img.jpg" 
   r = requests.get(img_url,stream = True)
  
   # per mettere meglio il nome name = img_url.slice('/')[-1] -1 per dire l'ultimo
   # per Movies le immagini poster_path, backdrop_path
   # per TVSeries poster path, per le stagioni : poster_path e sugli episodi : image_path, 
  
   if(r.status_code == 200):
       r.raw.decode_content = True # altrimenti img.size = 0
       r.raw
       with open(name_img,"wb") as f:
           shutil.copyfileobj(r.raw,f)



# Documentazione per prendere immagini : https://developers.themoviedb.org/4/getting-started/images


if __name__ == "__main__":
    print("Start \n")
    now = datetime.now()
    
    fillGenres()
    #getAllMovies()
    getAllSeries2()

    #getImage()
    time = datetime.now() - now
    print(f"time for execute : {time}")
    print("End \n")