
from os import system
from time import sleep

# Funções 
def adicionar_contato(nome_contato, telefone, email):
    try:
        print("**** Adicionar Contatos ****")
        contato = {'nome' : nome_contato, 'telefone': telefone, 'email': email, 'favorito': False }
        lista_contatos.append(contato)
        system("cls")
        print(f'{contato['nome']} foi adicionado aos contatos.')
        sleep(1.5)
        system("cls")
    except Exception as e:
        print(f" ERRO {e}")

def ver_contatos(lista_contatos):
    try:
        print("**** LISTA DE CONTATOS ****")
        for indice, contato in enumerate(lista_contatos, start= 1):  
            favorito = "✓" if contato['favorito'] else " "  
            print(f"{indice} - Nome: {contato['nome']} | Telefone: {contato['telefone']} | E_mail: {contato['email']} | Favorito[{favorito}]")
        sleep(1)
    except Exception as e:
        print(f" ERRO {e}")
   
def editar_contato(indice, novo_nome, novo_tel, novo_email, lista_contatos):
    try:
        ver_contatos(lista_contatos)
        print("**** EDITAR CONTATOS ****")
        lista_contatos[indice]["nome"] = novo_nome
        lista_contatos[indice]["telefone"] = novo_tel
        lista_contatos[indice]["email"] = novo_email
        system("cls")
        print(f"O contato {lista_contatos[indice]["nome"]} foi atualizado!")
        sleep(1)
    except Exception as e:
        print(f" ERRO {e}")

def marca_favorito(lista_contatos, indice):
    try:
        if lista_contatos[indice]["favorito"] == False:
            lista_contatos[indice]["favorito"] = True 
            favoritos.append(lista_contatos[indice])
            system("cls")
            print(f"{lista_contatos[indice]['nome']} foi adicionado aos favoritos!")
        else:
            lista_contatos[indice]["favorito"] = False
            del favoritos[indice]
    except Exception as e:
        print(f"ERRO {e}")          

def ver_favoritos(favoritos):
    print("**** LISTA DE FAVORITOS ****")
    for indice, contato in enumerate(favoritos, start= 1):
        print(f"{indice} - Nome: {contato['nome']} | Telefone: {contato['telefone']} | E_mail: {contato['email']}")
        sleep(1)

def apagar_contato(indice_contato, lista_contatos):
    try:
        print(f"{lista_contatos[indice_contato]['nome']} foi deletado com sucesso!")
        lista_contatos.pop(indice_contato)        
        sleep(1)
        system("cls")
    except Exception as e:
        print(f"ERRO {e}")

def apagar_favorito(indice_favorito, favoritos):
    try:
        print(f"{favoritos[indice_favorito]['nome']} foi deletado com sucesso!")
        favoritos.pop(indice_favorito)
        sleep(1)
        system("cls")
    except Exception as e:
        print(f"ERRO {e}")   


# Variaveis
lista_contatos = []
favoritos = []

while True:
    print("**** AGENDA  DE CONTATOS ****")
    print("""1 - Adicionar Contato
2 - Lista de Contatos
3 - Editar Contato
4 - Adinionar Contato aos Favoritos
5 - Lista de Favoritos
6 - Apagar Contato
7 - Fechar Agenda""")
    try:
        opcao = int(input("Informe a Opção desejada: "))
    except Exception as e:
        print(f"Erro: {e}! ")
    system("cls") # limpa tela do terminal


    if opcao == 1:  
        try:
            adicionar_contato(
                nome_contato= str(input("nome: ")),
                telefone= int(input('telefone: ')),
                email= str(input('email: '))
            )
        except Exception as e:
            print(f"ERRO {e}")

    elif opcao == 2:
        ver_contatos(lista_contatos)

    elif opcao == 3:    
        try:
            ver_contatos(lista_contatos)    
            indice = int(input("Informe o indice do contato a ser Editado: ")) -1  # mais é para equipara com a mudança do indice no for para iniciar em 1
            novo_nome = str(input("Informe nome atual: "))
            novo_tel = int(input('Informe o telefone atual: '))
            novo_email = str(input("Informe novo E-mail: "))
            editar_contato(indice, novo_nome, novo_tel, novo_email, lista_contatos)
        except Exception as e:
            print(f"ERRO {e}")

    elif opcao == 4:
        ver_contatos(lista_contatos)
        indice = int(input("Informe o indice do contato para marcar como favorito: ")) - 1
        marca_favorito(lista_contatos, indice)
    
    elif opcao == 5:
        ver_favoritos(favoritos)
    
    elif opcao == 6:
        escolha_lista = int(input("""1 - Deletar contato da lista de contatos
2 - Deletar contato da lista de Favoritos
Informe uma opção: """))
        if escolha_lista == 1:
            ver_contatos(lista_contatos)
            indice_contato = int(input("Informe o indice do contato a ser deletado: ")) -1
            apagar_contato(indice_contato, lista_contatos)
        elif escolha_lista == 2:
            ver_contatos(lista_contatos)
            indice_favorito = int(input("Informe o indice do contato a ser deletado: ")) -1
            apagar_favorito(indice_favorito, favoritos)

    elif opcao == 7:
        break