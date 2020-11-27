import tmdbsimple as tmdb
import requests
tmdb.API_KEY = '0a11e794490331ffaf9f0fdb167a701e'

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=0a11e794490331ffaf9f0fdb167a701e&language=en-US&page={p}"
       
res_body = requests.get(url=url,params = {"address":"italy"} )

data_j = res_body.json()

print(data_j)
