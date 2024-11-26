from flask import Flask, render_template
from flask import request
from flask import flash
from flask import redirect

app_Luiz = Flask(__name__)      

app_Luiz.config['SECRET_KEY'] = "ifro"

@app_Luiz.route('/usuario')  

def dados_usuario():
    nome_usuario = "Luiz"
    dados_usu = {"profissao" : "Analista de Requisitos", "disciplina" : "TSI 2023"}
    return render_template('usuario.html', nome=nome_usuario, dados=dados_usu)
#----------------------------------------------------------------
@app_Luiz.route('/home')
def homepage():
    return render_template('home.html')
#----------------------------------------------------------------
@app_Luiz.route('/usuario2/<nome_usuario>;<nome_profissao>;<nome_disciplina>')
def usuario(nome_usuario, nome_profissao, nome_disciplina):
    
    dados_usu={"profissao":nome_profissao, "disciplina":nome_disciplina}

    return render_template('usuario2.html', nome=nome_usuario, dados=dados_usu)
#----------------------------------------------------------------

@app_Luiz.route('/usuarios/<nome_usuario>;<nome_profissao>')
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao" : nome_profissao, "disciplina": "TSI 2023"}
    return render_template('usuario.html', nome=nome_usuario, dados=dados_usu)
#----------------------------------------------------------------
@app_Luiz.route('/base')
def base():
    return render_template('base.html')
#----------------------------------------------------------------
@app_Luiz.route('/visualizar')
def visualizar():
    return render_template('visualizar.html')
#----------------------------------------------------------------
@app_Luiz.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('nome_senha')
    
    if usuario == 'admin' and senha == '123':
        flash('Autenticado com sucesso!')
        return redirect('/usuario')
    else:
        flash('Usuário ou senha inválidos!')
        return redirect('/login')
    # Aqui você pode validar o nome de usuário e senha
    # e redirecionar para a página de home, caso seja válida
    #return render_template('teste.html', usuario=usuario, senha=senha)
    #return f"usuario: {usuario} e senha: {senha}"
#----------------------------------------------------------------
@app_Luiz.route('/login')
def login():
    return render_template('login.html')
#----------------------------------------------------------------
if __name__ == "__main__":  
    
    app_Luiz.run() 