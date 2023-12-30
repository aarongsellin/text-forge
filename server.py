from fastapi import FastAPI
import requests

app = FastAPI()

posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()

@app.get('/posts')
def posts_endpoint():
    return posts