import tmdbsimple as tmdb

tmdb.API_KEY = '0a11e794490331ffaf9f0fdb167a701e'

# prendere lista dei film usciti dal 2010


mov = tmdb.Movies("*") # bisogna iterare sulle pagine

movies2 = tmdb.Movies("*")

## api = 


print(movies2.top_rated())

# print(str(mov.top_rated()["results"])) # questo prende tutti i film per pagina, top rated è soltanto l'ordine