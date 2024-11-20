from flask import Flask, render_template

app_Luiz = Flask(__name__)                   

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
if __name__ == "__main__":  
    
    app_Luiz.run() 