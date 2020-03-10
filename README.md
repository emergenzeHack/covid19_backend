# covid19italia_form

## frontend

Form in XLSform hostati su https://kobo.humanitarianresponse.info

Moduli già attivi:

- [Chiedi Aiuto](https://ee.humanitarianresponse.info/x/#aozLp5mz)
- [Segnala contatti utili](https://ee.humanitarianresponse.info/x/#TTWdM1cJ)
- [Dona beni o servizi](https://ee.humanitarianresponse.info/x/#jc0dY8z7)
- [Segnala Raccolta Fondi](https://ee.humanitarianresponse.info/x/#2glr4leb)
- [Segnala Bufala](https://ee.humanitarianresponse.info/x/#ecZ2zzjJ)
- [Segnala Smart working](https://ee.humanitarianresponse.info/x/#I63unfno)
- [Segnala Dati ufficiali](https://ee.humanitarianresponse.info/x/#hy7sHGP3)
- [Segnala Iniziative culturali e ricreative](https://ee.humanitarianresponse.info/x/#jdqjUBQV)
- [Segnala Iniziative solidali](https://ee.humanitarianresponse.info/x/#NsdBTg2O)
- [Segnala e-learning/didattica a distanza](https://ee.humanitarianresponse.info/x/#YJuj2y4k)
- [Segnala Notizia](https://ee.humanitarianresponse.info/x/#Vde7ElAa)


## backend

`server.py` si occupa di ricevere le risposte ai form ed inviarle come GitHub Issues al repository [covid19italia_segnalazioni](https://github.com/emergenzeHack/covid19italia_segnalazioni/)

Prerequisiti

```bash
apt install python3 python3-pip
pip install --user pipenv
```

Avvio

```bash
pipenv shell
pipenv install
```
