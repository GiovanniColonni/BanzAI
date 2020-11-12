from pytrends.request  import TrendReq
import pandas as pd
from pandas import DataFrame
import csv as cvs

film_list = ["Il trono di spade"]
time_frame = "2020-10-11 2020-11-11"

## Dataset layout :
                                    #Regione1 #Regione2
            #<numero trimestre,Anno> 
    # FILM  #<numero trimestre,Anno>
            #<numero trimestre,Anno>

def write_to_cvs(data_frame):
    with open("film.cvs","w",newline='') as file:
        file = cvs.writer(file)
        for i in range(0,data_frame.size):
            file.writerow([film_list[0],data_frame.index[i],data_frame.values[i],time_frame])
        

def main():
    pyT = TrendReq(hl="it-IT")
    #pyT = TrendReq()
    pyT.build_payload(kw_list=film_list,timeframe=time_frame,geo="IT")
    data_frame = pyT.interest_by_region()
    write_to_cvs(data_frame)   

    
if __name__ == "__main__":
    main()