import authentification
import os, base64, requests, urllib, time, json, numpy as np, pylab as pl, datetime

class CatalogFunction():

    """HEART"""
    def WriteFile(self, userName):
        
        dataHeart = authentification.mainAuthentification(1)

        date = time.localtime()
        date2 = str(date.tm_mday)+"-"+str(date.tm_mon)+"-"+str(date.tm_year)
        nomFichier = userName+"_"+date2+".json"

        with open("testData.json", 'w') as f:
            data = {}
            data["contenu"]= dataHeart['activities-heart-intraday']['dataset']
            json.dump(data, f, indent=4)


    def GetArrayTimes(self, json):
        t = []
        for n in range (0, len(json['activities-heart-intraday']['dataset']),1):
            heure = json['activities-heart-intraday']['dataset'][n]['time']
            heureFinale = heure[0]+heure[1]+heure[2]+heure[3]+heure[4]+heure[5]+heure[6]+heure[7]
            t.append(heureFinale)
        return t
        
    def GetArrayHR(self, json):
        t = []
        for n in range (0, len(json['activities-heart-intraday']['dataset']),1):
            t.append(json['activities-heart-intraday']['dataset'][n]['value'])
        return t

    def GetTimestamp(self, time):
        return int(time[0]+time[1])*3600+int(time[3]+time[4])*60+int(time[6]+time[7])
        
    def SaveGraph(self, arrayTimes, arrayHR, nom):

            try:
                debut = self.GetTimestamp(arrayTimes[0])
                fin = self.GetTimestamp(arrayTimes[len(arrayTimes)-1])
                pas = int((fin-debut)/5)
                axeX = []
                palier = debut
                for i in range (0,len(arrayTimes)):
                    ts = self.GetTimestamp(arrayTimes[i])
                    if(ts>=palier):
                        axeX.append(arrayTimes[i])
                        palier = ts + pas
                    else:
                        axeX.append('')

                x=np.arange(len(axeX))
                pl.figure(figsize=(10,4))
                pl.xticks(pl.arange(len(axeX)), axeX)
                pl.plot(x, arrayHR)
                date = time.localtime()
                date2 = str(date.tm_mday)+"-"+str(date.tm_mon)+"-"+str(date.tm_year)
                nomFichier = nom+"_"+date2+"_Heart.png"
                pl.savefig(nomFichier)
            except:
                return None;

            return nomFichier

    def DisplayGraphHeart(self, userName):

        dataHeart = authentification.mainAuthentification(1)
        
        arrayTimes = self.GetArrayTimes(dataHeart)
        arrayHR = self.GetArrayHR(dataHeart)
        nameGraph = self.SaveGraph(arrayTimes, arrayHR, userName)            
                        
        return nameGraph


    def GetDate(self):
        date = time.localtime()
        tDay = date.tm_mday
        tMonth = date.tm_mon
        tYear = date.tm_year
        return "%s/%s/%s" % (tDay, tMonth, tYear)

    """def GetMoyennesDate(self, nom):
        try:
            json_data = open('moyennes_'+nom+'.json', 'r')
        except:
            with open('moyennes_'+nom+'.json', 'x', encoding='utf-8') as f:
                data = {}
                data["moyennes"]=[]
                json.dump(data, f, indent=4)
            json_data = open('moyennes_'+nom+'.json', 'r')
        data = json.load(json_data)
        tabHier = []
        tabAvantHier = []
        tabFinal = []
        for var in range(0, len(data["moyennes"])):
            date = data["moyennes"][var]["date"]
            dt = datetime.datetime.strptime(date, "%d/%m/%Y")
            ajd1 = self.GetDate()
            ajd2 = datetime.datetime.strptime(ajd1, "%d/%m/%Y")
            d1 = datetime.timedelta(days=1)
            d2 = datetime.timedelta(days=2)
            hier = ajd2-d1
            avantHier = ajd2-d2
            if(dt==hier):
                tabHier.append(var)
            if(dt==avantHier):
                tabAvantHier.append(var)
        sHier = 0
        sAvantHier = 0
        for var in range(0, len(tabHier)):
            sHier+= data["moyennes"][tabHier[var]]["moyenne"]
        try:
            tabFinal.append(sHier/len(tabHier))
        except:
            tabFinal.append(0)
        for var in range(0, len(tabAvantHier)):
            sAvantHier+= data["moyennes"][tabAvantHier[var]]["moyenne"]
        try:
            tabFinal.append(sAvantHier/len(tabAvantHier))
        except:
            tabFinal.append(0)
        return tabFinal"""

    """def GetMoyenneListe(self, Groupe):
        s = 0
        for n in range(0,len(Groupe)):
            s = s + int(Groupe[n])
        return s/len(Groupe)"""


    """STEP"""

    #def DisplayGraphHeartMonth(self, userName):

        
        

    def GetArrayDay(self, json):
        t = []
        for n in range (0, len(json['activities-steps']),1):
            t.append(json['activities-steps'][n]['dateTime'])
        return t
        
    def GetArrayStep(self, json):
        t = []
        for n in range (0, len(json['activities-steps']),1):
            t.append(json['activities-steps'][n]['value'])
        return t

    def SaveGraphStep(self, arrayDay, arrayStep, userName):

        debut = 0
        fin = len(arrayDay)
        pas = int((fin-debut)/5)
        axeX = []
        palier = debut
        for i in range(0,len(arrayDay)):
            if(i>=palier):
                axeX.append(arrayDay[i])
                palier = i + pas
            else:
                axeX.append('')

        x=np.arange(len(axeX))
        pl.figure(figsize=(10,4))
        pl.xticks(pl.arange(len(axeX)), axeX)
        pl.plot(x, arrayStep)
        date = time.localtime()
        date2 = str(date.tm_mday)+"-"+str(date.tm_mon)+"-"+str(date.tm_year)
        nomFichier = userName+"_"+date2+"_Steps.png"
        pl.savefig(nomFichier)

        return nomFichier

    def DisplayGraphStep(self, userName):

        dataStep = authentification.mainAuthentification(2)

        arrayDay = self.GetArrayDay(dataStep)
        arrayStep = self.GetArrayStep(dataStep)
        nameGraph = self.SaveGraphStep(arrayDay, arrayStep, userName)
     
        return nameGraph
    
    
    
