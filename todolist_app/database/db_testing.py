from .connectivity import SessionLocal
from .models import TodoItem



session = SessionLocal()

new_todo = TodoItem(name='Code all day')
session.add(new_todo)
session.commit()

'''
todos = session.query(TodoItem).filter(TodoItem.id==1).first()
print(todos)

session.delete(todos)
session.commit()
'''
session.close()