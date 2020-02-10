from flask import Flask
from flask_pymongo import PyMongo, pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'tasks'

app.config ['MONGO_URI'] = 'mongodb+srv://root:RootUser@myfirstdatabase-klrg6.mongodb.net/task_manager?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
def index():
        
    tasks = mongo.db.tasks
    results = tasks.find({'recipe_course' : 'Main'})
    
    for r in results:
        print(r["recipe_course"])
    return print(r["recipe_course"])  
    
    
    
    
   

if __name__ == '__main__':
    app.run(debug=True)    