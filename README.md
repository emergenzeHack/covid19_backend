# covid19italia_form

## frontend

Form in XLSform hostati su https://kobo.humanitarianresponse.info

Moduli già attivi:

- [Chiedi Aiuto](https://ee.humanitarianresponse.info/x/#aozLp5mz)
- [Segnala contatti utili](https://ee.humanitarianresponse.info/x/#TTWdM1cJ)

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
