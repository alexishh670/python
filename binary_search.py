import random
#en este programa se utiliza la recursion. que sigfica utilzar un algoritmo varias veces con pequeñas modificaciones a la vez
#para encontrar un resultado: en este caso el numero que estamos buscando.

#esta funcion recibe 4 parametros:
# 1.-datos
# 2.- objetivo o numero a encontrar
# 3.- el valor mas bajo.
# 4.-el valor mas alto.
def binary_search(data, target, low, high):
	if low > high:
		return False

	mid = (low + high) // 2	
	
	if target == data[mid]:
		return True

	elif target < data[mid]:
		return binary_search(data, target, low, mid-1)

	else:
		return binary_search(data, target, mid+1, high)


#primero debemos generar nuestro punto de ingreso:

if __name__ == '__main__':
	data = [random.randint(0,100) for i in range(10)]

	data.sort()

	print(data)

	target = int(input('what number would you like to find?'))
	found = binary_search(data, target, 0, len(data)-1)

	print(found)

