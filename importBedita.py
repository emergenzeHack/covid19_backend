from server import process_report
import json
from bs4 import BeautifulSoup

# Importa i dati di https://gitlab.com/bedita/covid19/supporto-psicologico-covid-19/-/raw/master/static/list.json

with open('bedita_psicologico.json') as json_file:
    data = json.load(json_file)
    for row in data:
    	row["Fasce orarie"] = row.pop("time")
    	
    	row["Link"] = row.pop("www")
    	row["Telefono"] = row.pop("tel")
    	row["location"] = row.pop("location").replace('?', '')
    	
    	row.pop("id")

    	row["Titolo"] = row.pop("title")
    	row.pop("uname")

    	html_str = row.pop("note")
    	soup = BeautifulSoup()
    	row["Descrizione"] = soup.get_text()

    	row_values = {k: v for k, v in row.items() if v is not None and v is not ""}

    	print(row_values)

    	headers = {
    	'Label':"Supporto Psicologico"
    	}

    	process_report(row_values, headers)
    	#print(row["location"])
