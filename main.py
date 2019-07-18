import sys


clients = 'pablo,ricardo,'


def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('el cliente ya se encuentra en el listado de clientes')
		

def list_clients():
	global clients

	print(clients)   

def update_client(client_name, updated_client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', updated_client_name + ',')
	else:
		_print_usernotfound()


def delete_client(client_name):
	global clients
	
	if client_name in clients:
		clients= clients.replace(client_name + ',', '')
	else:
		_print_usernotfound()
		
def search_client(client_name):
	client_list = clients.split(',')
	
	for client in client_list:
		 if client != client_name:
			 continue
		 else:
			 return True


def _add_comma():
	global clients
	
	clients += ','


def _print_welcome():
	print('Bienvenido a platzi ventas')
	print('*'*50)
	print('¿Que le gustaria hacer hoy?')
	print('[C]reate cliente')
	print('[L]ist')
	print('[U]pdate')            
	print('[D]elete cliente')
	print('[S]earch cliente')


def _print_usernotfound():
	print('Este cliente no se encuentra en la lista')


def _get_client_name():
	client_name = None

	while not client_name:
		client_name = input('¿cuál es el nombre del cliente?')
		
		if client_name == 'exit':
			client_name = None
			break
        
	if not client_name:
			sys.exit()

	return client_name  


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if command =='C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	
	elif command == 'D':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
	
	elif command == 'L':
		list_clients()

	elif command == 'U':
		client_name = _get_client_name()
		updated_client_name = input('¿Cuál es el nuevo nombre?')
		update_client(client_name, updated_client_name)
		list_clients()
	
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found:
			print('El nombre del cliente se encuentra registrado')
		else:
			print('El cliente: {} no esta en nuestra lista'.format(client_name))
	
	else: 
		print('Comando Inválido')
