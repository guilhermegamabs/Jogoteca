from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria = categoria
        self.console = console
        
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogos_lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'fiap'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos_lista)

@app.route('/novo')
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    
    return render_template('novo_jogo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos_lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if 'pitoco' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Logout efetuado com sucesso!')
    return redirect('/login')
    
app.run(debug=True)