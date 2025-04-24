from fastapi import FastAPI , HTTPException
from models import ToDo , ToDoCreate , ToDoUpdate
from itertools import count


app = FastAPI()

id_counter = count(1)
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
def postToDo(todo : ToDoCreate):
  new_todo = ToDo(id = next(id_counter) , **todo.dict())
  ToDo_db.append(new_todo)
  return {"message": "Todo created", "todo": new_todo}


@app.patch('/todo/{id}/completed')
def completedTodo(id : int):
  for todo in ToDo_db:
    if(todo.id == id):
      todo.completed = True
      return {"message" : "todo marked as completed" , "todo":todo}
  raise HTTPException(status_code=404, detail="Todo not found")

      
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
  
      