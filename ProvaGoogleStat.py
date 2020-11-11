from pytrends.request  import TrendReq
import pandas as pd
import csv

film_list = ["La Casa di Carta","Il trono di spade","La grande bellezza"]




def main():
    #pyT = TrendReq(hl="it-IT")
    pyT = TrendReq()
    pyT.build_payload(kw_list=["Il Trono di Spade"],timeframe="2020-11-11",geo="IT")
    data_frame = pyT.interest_by_region()
    print(data_frame)

    
if __name__ == "__main__":
    main()