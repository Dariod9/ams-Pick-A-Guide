from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
general_user=0

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    g= db.Column(db.Integer, nullable=False)

@app.route('/', methods=['POST', 'GET'])
def index():
    global general_user
    

    if request.method == 'POST':
        emailPut = request.form['emailIn']
        passwordPut = request.form['passIn']

        try:
            utilizador = User.query.filter_by(email=emailPut).first()
            passV=utilizador.password

            if passV==passwordPut:

                general_user = User.query.filter_by(email=emailPut).first()
                return redirect('/homepage')

            else:
                return redirect('/')

        except:
            print("EXCEPTION!")
            return redirect('/')


    else:
        return render_template('index.html')

@app.route('/escolher')
def escolher():
    global general_user

    return render_template('escolher_guia.html', general_user=general_user)

@app.route('/homepage')
def homepage():
    global general_user
    return render_template('pagina_inicial.html', general_user=general_user)


@app.route('/horarios')
def horarios():
    global general_user
    return render_template('horarios.html', general_user=general_user)


@app.route('/visitaMoliceiros')
def visitaMoliceiros():
    global general_user
    return render_template('visitaMoliceiros.html', general_user=general_user)



@app.route('/praias')
def praias():
    global general_user
    return render_template('visitaPraias.html', general_user=general_user)


@app.route('/details')
def praias():
    global general_user
    return render_template('contaDetails.html', general_user=general_user)


@app.route('/changepw')
def praias():
    global general_user
    return render_template('changePw.html', general_user=general_user)


@app.route('/guia')
def praias():
    global general_user
    return render_template('guiaDetalhes.html', general_user=general_user)



@app.route('/historico')
def praias():
    global general_user
    return render_template('historico.html', general_user=general_user)



@app.route('/historicoV')
def praias():
    global general_user
    return render_template('histVisitas.html', general_user=general_user)


@app.route('/pagamentos')
def praias():
    global general_user
    return render_template('pagamentos.html', general_user=general_user)



@app.route('/conclusao')
def praias():
    global general_user
    return render_template('conclusao_proposta.html', general_user=general_user)



@app.route('/criar', methods=['POST','GET'])
def criar():
    global general_user
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        password= request.form['pass']
        pass_check= request.form['passAgain']

        if password == pass_check:

            new = User(name= nome, email = email, password = password)
            db.session.add(new)
            db.session.commit()
            return redirect('/')

        else:
            return redirect('/criar')


    else:
        return render_template('criar_conta.html')


if __name__ == "__main__":    
    app.run(debug=True)

