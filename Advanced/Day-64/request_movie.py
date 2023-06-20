import requests

API_KEY = 'b2eac59d6c813cfa75903c5dea7b9473'
API_Read_Access_Token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMmVhYzU5ZDZjODEzY2ZhNzU5MDNjNWRlYTdiOTQ3MyIsInN1YiI6IjY0OGFjZjUwMDc2Y2U4MDBjOGI5MmExMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qm16Ha7AbRDNun9QF-CVHMc2fYpXEiPFIb3FNJbvg8E'

url = "https://api.themoviedb.org/3/search/movie"

parameters = {
    "api_key": API_KEY,
    "query": "Fast 10"
}

response = requests.get(url, params=parameters).json()
print(response)
