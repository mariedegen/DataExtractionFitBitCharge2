

def WriteGlobalJson(jsonFile, nom):
    date = time.localtime()
    date2 = str(date.tm_mday)+"-"+str(date.tm_mon)+"-"+str(date.tm_year)
    nomFichier = nom+"_"+date2+".json"
    with open(nomFichier, 'w', encoding='utf-8') as f:
        data = {}
        data["contenu"]= jsonFile['activities-heart-intraday']['dataset']
        json.dump(data, f, indent=4)
