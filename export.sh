#!/bin/bash
# comandi per esportare i dati in csv
echo "exporting data "

mongoexport -h 127.0.0.1:27017 -c Movies -d Domain_Data --type=csv --out Data/Movies --fields=id,title,release_date,genres,popularity

mongoexport -h 127.0.0.1:27017  -c TvSeries -d Domain_Data --type=csv --out Data/TvSeries --fields=id_tv_series,name_tv_series,first_air_date,genres,popularity,origin_country,original_language

echo "Export Done"