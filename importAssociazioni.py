import csv
from server import process_report

with open('associazionimi-cultura.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    i = 0
    for payload in csv_reader:
    	if i in range(1):
	        print(payload)
	        
	        #payload["Titolo"] = "Negozio a Roma " + payload.pop("Nome")
	        payload["Descrizione"] = payload.pop("Azioni")
	        payload["Titolo"] = "Progetto " + payload.pop("Nome progetto") + " - " + payload.pop("Nome associazione")


	        headers = {
	            'Label':"Servizi e iniziative solidali private"
	        }
	        payload2 = {k: v for k, v in payload.items() if v != None and v != ""}

	        process_report(payload2, headers, ["Servizi e iniziative solidali private", "Posizione mancante"], issue_title=payload["Titolo"])
	        i += 1
