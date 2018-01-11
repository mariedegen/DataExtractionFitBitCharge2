"""@package fitbit
The catalog of graph and data functions
"""

import authentification
import os, base64, requests, urllib, time, json, numpy as np, pylab as pl, datetime

class CatalogFunction():
    """
        The catalog of functions
         - collects data
         - makes into a graph
         - exports data
    """

    """HEART"""
    def WriteFile(self, userName):
        """
            Write in a file data of the day
            :param self: the object
            :param userName: the name of the user
        """
        
        dataHeart = authentification.mainAuthentification(1)

        date = time.localtime()
        date2 = str(date.tm_mday)+"-"+str(date.tm_mon)+"-"+str(date.tm_year)
        nomFichier = userName+"_"+date2+".json"

        with open(nomFichier, 'w') as f:
            data = {}
            data["contenu"]= dataHeart['activities-heart-intraday']['dataset']
            json.dump(data, f, indent=4)


    def WriteFileSamsung(self, data):
        """
            Write in a file data of the day
            :param self: the object
            :param userName: the name of the user
        """
        date = time.localtime()
        date2 = str(date.tm_mday)+"-"+str(date.tm_mon)+"-"+str(date.tm_year)
        nomFichier = "Heart"+"_"+date2+".json"

        with open(nomFichier, 'w') as f:
            json.dump(data, f, indent=4)


    def GetArrayTimes(self, json):
        """
            Collect the data from json and get only times data
            :param self: the object
            :param json: the data
            :return t: array of times
        """
        t = []
        for n in range (0, len(json['activities-heart-intraday']['dataset']),1):
            heure = json['activities-heart-intraday']['dataset'][n]['time']
            heureFinale = heure[0]+heure[1]+heure[2]+heure[3]+heure[4]+heure[5]+heure[6]+heure[7]
            t.append(heureFinale)
        return t
        
    def GetArrayHR(self, json):
        """
            Collect the data from json and get only times heart rate
            :param self: the object
            :param json: the data
            :return t: array of heart rate
        """
        t = []
        for n in range (0, len(json['activities-heart-intraday']['dataset']),1):
            t.append(json['activities-heart-intraday']['dataset'][n]['value'])
        return t

    def GetTimestamp(self, time):
        """
            Calculate the end of the array
            :param self: the object
            :param time: an array of time
            :return t: the end of the array
        """
        return int(time[0]+time[1])*3600+int(time[3]+time[4])*60+int(time[6]+time[7])
        
    def SaveGraphHeart(self, arrayTimes, arrayHR, name):
        """
            Build a graph of heart rate and save it on a picture 
            :param self: the object
            :param arrayTimes: an array of times
            :param arrayHR: an ar ray of heart rate
            :param name: the name of the user
            :return nameFile: the name of the file

            .. note:: If there is an exception, the graph is not build
        """

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
            nameFile = name+"_"+date2+"_Heart.png"
            pl.savefig(nameFile)
        except:
            return None;

        return nameFile

    def GetGraphHeart(self, userName):
        """
            To get the graph of the heart rate
            :param self: the object
            :param userName: the name of the user
            :return nameGraph: the name of the graph
        """
        

        dataHeart = authentification.mainAuthentification(1)
        
        arrayTimes = self.GetArrayTimes(dataHeart)
        arrayHR = self.GetArrayHR(dataHeart)
        nameGraph = self.SaveGraphHeart(arrayTimes, arrayHR, userName)            
                        
        return nameGraph     
        

    def GetArrayX(self, json, activities):
        """
            To get the axe of X of the graph
            :param self: the object
            :param json: the data
            :param activities: the activities collect in the data
            :return t: the data of axe X
        """
        
        t = []
        for n in range (0, len(json[activities]),1):
            t.append(json[activities][n]['dateTime'])
        return t
        
    def GetArrayY(self, json, activities):
        """
            To get the axe of Y of the graph
            :param self: the object
            :param json: the data
            :param activities: the activities collect in the data
            :return t: the data of axe Y
        """
        t = []
        for n in range (0, len(json[activities]),1):
            t.append(json[activities][n]['value'])
        return t

    def SaveGraph(self, arrayX, arrayY, userName, activities):
        """
            Build a graph of the activities and save it on a picture 
            :param self: the object
            :param arrayX an array of axe X
            :param arrayY: an array of axe Y
            :param activities: the activities collect in the data
            :param userName: the name of the user
            :return nameFile: the name of the file
        """

        debut = 0
        fin = len(arrayX)
        pas = int((fin-debut)/5)
        axeX = []
        palier = debut
        for i in range(0,len(arrayX)):
            if(i>=palier):
                axeX.append(arrayX[i])
                palier = i + pas
            else:
                axeX.append('')

        x=np.arange(len(axeX))
        pl.figure(figsize=(10,4))
        pl.xticks(pl.arange(len(axeX)), axeX)
        pl.plot(x, arrayY)
        date = time.localtime()
        date2 = str(date.tm_mday)+"-"+str(date.tm_mon)+"-"+str(date.tm_year)
        nomFichier = userName+"_"+date2+"_"+activities+".png"
        pl.savefig(nomFichier)

        return nomFichier

    def GetGraphStep(self, userName):
        """
            To get the graph of the step
            :param self: the object
            :param userName: the name of the user
            :return nameGraph: the name of the graph
        """

        dataStep = authentification.mainAuthentification(2)

        arrayDay = self.GetArrayX(dataStep, 'activities-steps')
        arrayStep = self.GetArrayY(dataStep, 'activities-steps')
        nameGraph = self.SaveGraph(arrayDay, arrayStep, userName, "steps")
     
        return nameGraph
    
    def GetGraphCalories(self, userName):
        """
            To get the graph of the calories
            :param self: the object
            :param userName: the name of the user
            :return nameGraph: the name of the graph
        """

        dataCalories = authentification.mainAuthentification(4)
      
        arrayDay = self.GetArrayX(dataCalories, 'activities-calories')
        arrayCalorie = self.GetArrayY(dataCalories, 'activities-calories')
        nameGraph = self.SaveGraph(arrayDay, arrayCalorie, userName, "calories")

        return nameGraph

    def GetGraphFloor(self, userName):
        """
            To get the graph of the number of floor
            :param self: the object
            :param userName: the name of the user
            :return nameGraph: the name of the graph
        """

        dataFloor = authentification.mainAuthentification(3)

        arrayDay = self.GetArrayX(dataFloor, 'activities-floors')
        arrayFloor = self.GetArrayY(dataFloor, 'activities-floors')
        nameGraph = self.SaveGraph(arrayDay, arrayFloor, userName, "floors")

        return nameGraph

    def GetGraphActive(self, userName):
        """
            To get the graph of the active minute
            :param self: the object
            :param userName: the name of the user
            :return nameGraph: the name of the graph
        """

        dataActive = authentification.mainAuthentification(7)
      
        arrayDay = self.GetArrayX(dataActive, 'activities-minutesVeryActive')
        arrayActive = self.GetArrayY(dataActive, 'activities-minutesVeryActive')
        nameGraph = self.SaveGraph(arrayDay, arrayActive, userName, "minutesVeryActive")

        return nameGraph

    def GetGraphDistance(self, userName):
        """
            To get the graph of the distance
            :param self: the object
            :param userName: the name of the user
            :return nameGraph: the name of the graph
        """

        dataDistance = authentification.mainAuthentification(5)
      
        arrayDay = self.GetArrayX(dataDistance, 'activities-distance')
        arrayDistance = self.GetArrayY(dataDistance, 'activities-distance')
        nameGraph = self.SaveGraph(arrayDay, arrayDistance, userName, "distance")

        return nameGraph

    def GetGraphMinutes(self, userName):
        """
            To get the graph of the minutes
            :param self: the object
            :param userName: the name of the user
            :return nameGraph: the name of the graph
        """

        dataMinutes = authentification.mainAuthentification(6)
      
        arrayDay = self.GetArrayX(dataMinutes, 'activities-minutesSedentary')
        arrayMinutes = self.GetArrayY(dataMinutes, 'activities-minutesSedentary')
        nameGraph = self.SaveGraph(arrayDay, arrayMinutes, userName, "minutesSedentary")

        return nameGraph
    
   
