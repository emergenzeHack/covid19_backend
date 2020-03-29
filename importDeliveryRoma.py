# Importa i dati di https://github.com/emergenzeHack/covid19italia/issues/320

import csv
from server import process_report
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Covid19Italia.help")

with open('output-1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for payload in csv_reader:
        if "Indirizzo" in list(payload) and "Posizione" not in list(payload):
            location_geo = None
            tries = 0
            while location_geo is None:
                tries += 1
                if tries < 10:
                    try:
                        print("Getting coordinates. (%s)" % (tries))
                        location_input = payload["Indirizzo"]
                        location_geo = geolocator.geocode(location_input)
                    except:
                        pass
                else:
                    location_geo = 0
            if location_geo is not 0:
                payload["Posizione"] = str(location_geo.latitude) +" "+str(location_geo.longitude)
                #payload.pop("location")
        print(payload)
        
        payload["Titolo"] = "Negozio a Roma " + payload.pop("Nome")

        headers = {
            'Label':"Consegne e commissioni"
        }
        payload2 = {k: v for k, v in payload.items() if v is not None and v is not ""}

        process_report(payload2, headers, ["Servizi e iniziative solidali private", "Posizione da verificare"])