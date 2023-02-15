import datetime
DATEFROM=datetime.datetime.now().strftime("%d/%m/%Y")
DATETO=datetime.datetime.now()+datetime.timedelta(days=60)
DATE_TO=DATETO.strftime("%d/%m/%Y")
print(DATE_TO)
print(DATEFROM)
