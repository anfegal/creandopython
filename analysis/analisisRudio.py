import pandas as pd

from generators.generadorDecibelios import generarDatosRuido

def construirDataRuido():
   
    datosRuido=generarDatosRuido()
    dataFrameRuido=pd.DataFrame(datosRuido,columns=["id","Nivel ruido","Comuna"])

    dataFrameRuido.to_csv("datosruido.csv",index=False)
        
    
construirDataRuido()   