import tmdbsimple as tmdb

tmdb.API_KEY = '0a11e794490331ffaf9f0fdb167a701e'

# Trovare modo per iterare sulla pagina, guardare issue aperto su git https://github.com/celiao/tmdbsimple/issues/73


mov = tmdb.Movies("*") # bisogna iterare sulle pagine

movies2 = tmdb.Movies("*")

## api = 


print(movies2.top_rated())

# print(str(mov.top_rated()["results"])) # questo prende tutti i film, top rated è soltanto l'ordine