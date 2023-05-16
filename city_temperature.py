#задание 1
from pprint import pprint
city_temperature = {"city": "Москва", #Создайте словарь
                    "temperature": "20"
}
print(city_temperature['city']) #Выведите на экран значение ключа city
#Уменьшите значение "temperature" на 5
city_temperature['temperature'] = str(int(city_temperature["temperature"])- 5)
pprint(city_temperature) #Выведите на экран весь словарь

#задание 2
#Проверьте, есть ли в словаре ключ country
print(city_temperature.get('country')) 
#Выведите значение по-умолчанию "Россия" для ключа country
print(city_temperature.get('country','Россия'))
#Добавьте в словарь элемент date со значением "27.05.2019"
city_temperature['date'] = '27.05.2019'
print(len(city_temperature)) #Выведите на экран длину словаря