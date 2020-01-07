# This is a comment where programmers write secret things

from flask import Flask
# Below we tell python to look for our file with our method definition
from hello_world import my_function_using_the_name

# This creates the application webpage
app = Flask(__name__)

# This is the Homepage 
@app.route('/')
def hello_repler():
  return 'Hello, Repler! You on on a webpage!'
  
# This is a new page with our function on it  
@app.route('/new-page')
def new_page():
  output = my_function_using_the_name("Penny")
  return str(output)

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8080)
    