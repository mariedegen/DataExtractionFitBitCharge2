
import imageViewerSamsung
import server_network

def mainAppSamsung():
    
    #reception tableau donnée
    data = server_network.serverNetwork(8888, "B8-81-98-D4-F2-78")

    #Open the application
    windowSamsung = imageViewerSamsung.mainInterface(data)


