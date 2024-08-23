# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo
MONGODB_URI = 'mongodb+srv://divineivara:tBKKjVsXLUNFvV0e@flaskapp.hv7ov.mongodb.net/?retryWrites=true&w=majority&appName=flaskapp'
client = pymongo.MongoClient(MONGODB_URI)
db = client.flaskapp
# Creating students collection and inserting a document
db.students.insert_one({'name': 'Divine', 'country': 'Nigeria', 'city': 'calabar', 'age': 250,})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)