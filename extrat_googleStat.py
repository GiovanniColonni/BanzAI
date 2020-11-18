import datetime
from pytrends.request import TrendReq
import csv as cvs

class ExtractGoogleStat:

    def __init__(self,start_date):

        self.start_date = datetime.date.fromisoformat(start_date)
        self.film_list = ["Il trono di spade"]
        self.data_frame = 0
        self.time_frame = ""
        self.done = False
        self.geo = "IT"
        self.dbName ="film.cvs"
        self.file = open(self.dbName,"w",newline='')

    def writeToCVS(self): # write the payload of one time period
            file = cvs.writer(self.file)
            for i in range(0,self.data_frame.size):
                file.writerow([self.film_list[0],self.data_frame.index[i],self.data_frame.values[i],self.time_frame])
            return 1
    
    def setTimeFrame(self): # return time period from date : "2020-10-11 2020-11-11"
        
        if(self.start_date > datetime.date.today()):
            self.time_frame = -1 # arrivati alla data corrente
            return -1
        date_t =  str(self.start_date) + " "

        day_ = self.start_date.day
        month_ = self.start_date.month +1 # incremento di 1 mese
        year_ = self.start_date.year
        
        if(month_ > 12):
            month_ = 1
            year_ = year_ + 1

        next_date = datetime.date(year_,month_,day_)
        date_t = date_t + str(datetime.date(year_,month_,day_))
        
        print(f"time range {date_t}")
        
        self.start_date = next_date
        self.time_frame = date_t

    def collectByRegion(self): # send a request on a certain time period

        pyT = TrendReq(hl="it-IT") # stabilisce connessione
        pyT.build_payload(kw_list=self.film_list,timeframe=self.time_frame,geo=self.geo)
        self.data_frame = pyT.interest_by_region()
    
    def collectByCity(self): # il wrapper per le api ha un bug https://github.com/GeneralMills/pytrends/issues/417
        pyT = TrendReq(hl="it-IT") # stabilisce connessione
        pyT.build_payload(kw_list=self.film_list,timeframe=self.time_frame,geo=self.geo)
        self.data_frame = pyT.interest_by_region(resolution = 'CITY',inc_low_vol=True, inc_geo_code=False)
        print(self.data_frame)    

    def collectStat(self):

        # ciclare anche su lista film
        while(self.setTimeFrame() != -1):
            self.collectByCity()
            self.writeToCVS()
        
        pass
        self.closeFile()
    
    def closeFile(self):
        self.file.close()


if __name__ == "__main__":
    ex = ExtractGoogleStat("2020-06-01")
    ex.collectStat()