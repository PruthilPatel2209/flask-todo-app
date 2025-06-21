from flask import Flask,request,render_template,session, make_response,redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mysecretkey'

bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class TODO(db.Model) : 

    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str :
       return f'{self.srno} - {self.title}'    
  
@app.route('/', methods=['GET', 'POST'])
def todo():

    if request.method=="POST" :
        title = request.form.get('title')
        desc = request.form.get('desc')
        todo = TODO(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    alltodos = TODO.query.all()

    return render_template('Todo.html', todos=alltodos)

@app.route('/delete/<int:srno>')
def delete(srno):

    task = TODO.query.filter_by(srno=srno).first()
    db.session.delete(task)
    db.session.commit()

    return redirect('/')

@app.route('/update/<int:srno>', methods=['GET', 'POST'])
def update(srno):
    
    task = TODO.query.filter_by(srno=srno).first()
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.desc = request.form.get('desc')
        db.session.commit()
        return redirect('/')
    
    return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)
