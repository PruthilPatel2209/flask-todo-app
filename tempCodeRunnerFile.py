from flask import Flask,request,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/', methods=['POST','GET'])
def hello():
    # if request.method == 'GET' :
    #     return "THIS IS A GET REQUEST"
    # elif request.method == 'POST':
    #     return "THIS IS A POST REQUEST"
    text = "This example of Filter"
    return render_template('index.html', text=text)

@app.template_filter('repeats')
def repeat(string, n) :
    return string * n;

@app.route('/handle_url') 
def handle_urls() :
    if 'greeting' in request.args.keys and 'name' in request.args.keys :
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting} {name}"
    else : 
        return "<h1>YOU HAVE MISSING PARAMETERS</h1>"
    
# @app.route('/todo')
# def index():

#     return render_template('Todo.html')

if __name__ == '__main__':
 app.run(debug=True)
