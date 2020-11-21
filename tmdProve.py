import tmdbsimple as tmdb
import requests
tmdb.API_KEY = '0a11e794490331ffaf9f0fdb167a701e'


p = 2
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=en-US&page={p}"
       
res_body = requests.get(url=url,params = {"address":"italy"} )

data_j = res_body.json()

print(data_j)
#URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=it-IT&page=3"

#basta iterare sul parametro pagina dell'url, si puo' fare la stessa cosa con gli show televisivi

#location = "Perugia centro"

#PARAMS = {'address':location}

#r = requests.get(url = URL,params = PARAMS)

#data = r.json()

#res = data['results']

#for r in res:
 #   print(f"title : {r['title']} , release_date : {r['release_date']}, genre : {}")

 

# Trovare modo per iterare sulla pagina, guardare issue aperto su git https://github.com/celiao/tmdbsimple/issues/73
# forse sarebbe meglio non utilizzare il wrapper, invece scrivere le api per seperare eventuali bug

# mov = tmdb.Movies(2500) # bisogna iterare sulle pagine

# movies2 = tmdb.Movies(20012)


## api = 


# print(movies2.info())

# print(str(mov.top_rated()["results"])) # questo prende tutti i film, top rated è soltanto l'ordine