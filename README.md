# covid19italia.help - Modulistica

## frontend

Form in XLSform hostati su https://kobo.humanitarianresponse.info

Moduli già attivi:

- [Chiedi Aiuto](https://ee.humanitarianresponse.info/x/#aozLp5mz)
- [Dona beni o servizi](https://ee.humanitarianresponse.info/x/#jc0dY8z7)
- [Segnala Iniziativa](https://ee.humanitarianresponse.info/x/#6KafBk33)
- [Segnala contatti utili](https://ee.humanitarianresponse.info/x/#TTWdM1cJ)
- [Segnala Bufala](https://ee.humanitarianresponse.info/x/#ecZ2zzjJ)
- [Segnala Dati ufficiali](https://ee.humanitarianresponse.info/x/#hy7sHGP3)
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
