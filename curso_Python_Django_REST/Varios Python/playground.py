# coding=utf-8
print("Hello World")

# Listas
fruits = ["Apple","Orange","Watermelon"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
from_2_to_6 = numbers[2:7]
print(from_2_to_6)
greater_than_4 = numbers[5:]
print(greater_than_4)
print(numbers[::2])
print(numbers[1::2])

print(4 in numbers)

# Diccionarios
fighter = { "name": "Chuck", "last_name": "Norris", "technique": "Karate" }
print fighter["name"] #NUNCA SE ACCEDE ASÍ A LAS CLAVES DE DICCIONARIO
print fighter.get("nombre")

# True, False, None ==> TRUE, FALSE, NULL

def print_fruits(fruits_list):

	for fruit in fruits_list:
		print(fruit)

print_fruits(fruits)
print("así")