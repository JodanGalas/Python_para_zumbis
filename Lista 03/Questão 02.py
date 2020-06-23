#02 -

usuario = input('Insira o seu usuário: ')
senha = input('Insira sua senha: ')
while usuario == senha:
    print('ERRO! Tente novamente.')
    usuário = input('Usuário: ')
    senha = input('Senha: ')
else:
    print('Login efetuado com sucesso.')