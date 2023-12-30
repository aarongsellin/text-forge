from fastapi import FastAPI
import requests

app = FastAPI()

posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()

@app.get('/posts')
def posts_endpoint():
    posts.sort(key=lambda post: -post['id'])
    return posts

@app.get('/ping')
def ping_endpoint():
    return {'pong':True}