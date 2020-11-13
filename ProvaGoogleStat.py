from pytrends.request  import TrendReq
import pandas as pd
from pandas import DataFrame
import csv as cvs
import datetime

film_list = ["Il trono di spade"]
time_frame = "2020-10-11 2020-11-11"
s_date = datetime.date.fromisoformat("2010-12-01") # data inizio per il rilevamento

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
        
def incMont():

        if(s_date == datetime.date.today()):
            return -1
        
        date_t =  str(s_date) + " "
        day_ = s_date.day
        month_ = s_date.month +1
        year_ = s_date.year
        if(month_ > 12):
            month_ = 1
            year_ = year_ + 1
        next_date = datetime.date(year_,month_,day_)
        s_date = next_date
        date_t = date_t + str(datetime.date(year_,month_,day_))
        return date_t


def main():
    pyT = TrendReq(hl="it-IT")
    time_frame = incMont()
    while(time_frame != -1):
        pyT.build_payload(kw_list=film_list,timeframe=time_frame,geo="IT")
        data_frame = pyT.interest_by_region()
        write_to_cvs(data_frame) 
        time_frame = incMont()
    
      

    
if __name__ == "__main__":
    main()