#classe responsavel pela conexao com o banco

import pyrebase 

config = {
		"apiKey": "",
	    "authDomain": "",
	    "databaseURL": "",
	    "projectId": "",
	    "storageBucket": "",
	    "messagingSenderId": "",
	    "appId": ""
}


#inicializando o app
firebase = pyrebase.initialize_app(config)

#campos email e senha que virao dos botoes 
def novo_usuario(email, password):
	global firebase
	#Criando autenticação
	auth = firebase.auth()
	try:
		#inserindo dados da autenticação
		user = auth.create_user_with_email_and_password(email, password)
		#validando o email
		auth.send_email_verification(user['idToken'])
		print("cadastro iniciado com sucesso entre no seu email ")
	except :
		print("esta conta ja foi cadastrada")
	Conexao()



def usuario_cadastrado():
	print("Usuario cadastrado")
	email = input("Please digite seu gmail \n")
	password = input ("Please enter your password\n")
	try:
		user = auth.sign_in_with_email_and_password(email, password)
		print("Login successful")
	except :
		print("ocorreu um erro ao se logar no sistema")
		usuario_cadastrado()
		#auth.send_password_reset_email(email)
		#print("Enviaremos um link para seu email para redefinir sua senha")
	Conexao()




def Conexao():
        print("Bem vindo ao programa ")
        chamada = int(input("1 - novo usuario \n2 - usuario cadastrado\n"))
        if chamada == 1:
                novo_usuario()
        elif chamada ==2:
                usuario_cadastrado()



#iniciando campo para codico dos livros
dados = firebase.database()
inc = 0
#dados.child().child('variavel').set({'cont':0}) criar contador
v = dados.child().child('variavel').get()
if v:
	inc = v.val()['cont']+1
	dados.child().child('variavel').update({'cont':inc})
else:
	dados.child().child('variavel').set({'cont':0})



#funçoes do livro
#cod=int(input("Digite o cod do livro"))
#a,b,c=input("Digite o nome do livro, autor, e numero de paginas separado por virgula ex: (A culpa é do programador,estagiario,123)").split(",")



#dados.child().child("biblioteca").child(inc).set({"Nome do Livro":a,"autor":b,"numero de paginas":c})

#dados.child().child("biblioteca").child(cod).update({"Nome do Livro":a,"autor":b,"numero de paginas":c})												

#dados.child().child("biblioteca").child(4).remove()
														
#informacoes=dados.child().child("biblioteca").child(3).get().each()  
#for i in informacoes:
#	print(i.key(),i.val())			