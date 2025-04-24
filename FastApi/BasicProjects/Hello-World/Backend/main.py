from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
  return {"message" : "hello , FastApi"}

@app.get('/{name}')
def name_route(name : str):
  return {"message" : f'hello {name}'}