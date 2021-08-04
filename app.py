#Flask Dependancy
from flask import Flask

#Create New Flask Instance ##Variables with underscores like this are called magic methods
app = Flask(__name__)

#Create Flask Route (First line creates the starting point or "root")
@app.route('/')
def skilldrill():
    return 'Well this is something huh?'

