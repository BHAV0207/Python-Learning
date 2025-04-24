from fastapi import FastAPI , HTTPException
from models import ToDo


app = FastAPI()

ToDo_db = []

@app.get('/')
def home():
  return {"message" : "welcome to the to-do application"}

@app.get('/todo')
def allTodo():
  return ToDo_db

@app.get('/todo/{id}')
def getById(id : int):
  for todo in ToDo_db:
    if todo.id == id:
      return todo
  
  raise HTTPException(status_code=404 , detail="Todo not found")

@app.post('/todo')
def postToDo(todo : ToDo):
  for existing in ToDo_db:
    if(existing.id == todo.id):
      raise HTTPException(status_code=400 , detail="Todo already Exist")
  
  ToDo_db.append(todo)
  return {"message": "Todo created", "todo": todo}
      
@app.put('/todo/{id}')
def updateTodo(id : int , updated_todo :ToDo):
  for index, todo in enumerate(ToDo_db):
    if(id == todo.id):
      ToDo_db[index] =  updated_todo
      return {"message": "Todo updated", "todo": updated_todo}
  
  raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todo/{id}")
def deleteTodo(id : int):
  for index , todo in enumerate(ToDo_db):
    if(todo.id == id):
      ToDo_db.pop(index)
      return {"message" : "todo deleted"}
  
  raise HTTPException(status_code=404 , detail="todo not found ")
  
      