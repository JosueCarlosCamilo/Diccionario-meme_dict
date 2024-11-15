meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "aterrador, siniestro",
            "CHIDO": "Que esta muy bien",
            "CHAVALES": "Chicos o Todos",
            "ROFL": "una respuesta a una broma",
            }
user = input("Que palabra desea consultar").upper()
#upper() mayuscula convierte la letra que escribas en mayuscula
#lower() minuscula convierte la letra que escribas en minuscula
if user in meme_dict.keys():
    print(meme_dict[user])
else:
    print("La palabra no esta registrada")
