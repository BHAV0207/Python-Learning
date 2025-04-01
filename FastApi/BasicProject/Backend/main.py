from fastapi import FastAPI
from typing  import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index(): 
  return {'data' : {'name' : "bhav"}} 



@app.get('/blog')
def index(limit , published :bool):
  if published:
    return {f'{limit} is the limit'}
  else:
    return {f'{published} is the boolean'}
  
# we can define the time also in the function parameter and as well as the route

@app.get('/blog/new')
def index(limit = 10 , published :bool = False , sort :Optional[str] = None ):
  return({limit})

# when we define values for some parameters in the function , and tehre are some parameters which we dont want to be defined we can use the "Optional" class  
 
@app.get('/blog/{id}')
def show(id):
  return {'data' : id}   

@app.get('/blog/num/{id}')
def show(id :int):
  return {'data' : id}


class Blog(BaseModel):
  title : str 
  body : str 
  published : Optional[bool]
  

@app.post('/blog')
def postBlog(request : Blog):
  # return request
  return {f'blog has title {request.title}  and body {request.body}'}