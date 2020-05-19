import json
######################################################
# 1. Json dan Dictionary ye Çevirme İşlemi
######################################################

# örnek bir JSON verisi:
# 3 tırnak arasına çok sayıda satır yazabiliyoruz
# x =  """
#     {
#         "name":"John",
#         "age":30,
#         "city":"New York"
#     }
# """
#
# # json verisini alıp, dictionary veri tipine dönüştürür:
# dict = json.loads(x)
#
# # dictionary veri tipinin kullanımı:
# print(dict["name"])
# print(dict["age"])
# print(dict["city"])


##############################################################
# 2. Python objesinden Json a Çevirme İşlemi (dictionary örneği)
##############################################################
# import json
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)

##############################################################
# 3. Diğer Python objelerinden Json a Çevirme İşlemi
##############################################################
# print(json.dumps({"name": "John", "age": 30}))  # dict
# print(json.dumps(["apple", "bananas"]))         # list
# print(json.dumps(("apple", "bananas")))         # tuple
# print(json.dumps("hello"))                      # string
# print(json.dumps(42))                           # int
# print(json.dumps(31.76))                        # float
# print(json.dumps(True))                         # Boolean: True
# print(json.dumps(False))                        # Boolean: False
# print(json.dumps(None))                         # None

# Tüm Python objelerini içeren bir veriyi Json a çevirme
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))
# print(json.dumps(x, indent=4)) # sonucu formatlama
# print(json.dumps(x, indent=4, sort_keys=True)) # alfabetik sıra

# default seperatorler (", ", ": ") dir ancak değiştirilebilir
# print(json.dumps(x, indent=4, separators=(". ", " = ")))

