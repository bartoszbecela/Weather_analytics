import csv
import pandas as pd
from requests import get
from json import loads
from terminaltables import AsciiTable
import schedule
import time

# enter names of cities
CITTIES = ['Wrocław', 'Opole']

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop/'
    response = get(url)
    rows = [
        ['Miasto', 'Godzna_pomiaru', 'Temperatura','Cisnienie','Suma_opadu']   # enter parameters which you want to know(your names)
    ]
    for row in loads(response.text):
        if row['stacja'] in CITTIES:
          rows.append([                     # In this list enter original names of parameters which are from IMGW site
              row['stacja'],
              row['godzina_pomiaru'],
              row['temperatura'],
              row['cisnienie'],
              row['suma_opadu']
          ])

    # print(rows)
    table = AsciiTable(rows)
    print(table.table)
    df = pd.DataFrame(rows)
    print(df)


    # with open('/home/bartosz/Dokumenty/weather.csv', 'a') as csv_file:
    #      csv_writer = csv.writer(csv_file, delimiter=',')
    #      csv_writer.writerow(rows)
    df.to_csv('/home/bartosz/Dokumenty/weather.csv',mode= 'a', index= False)                # Enter path where file will be save


if __name__ == '__main__':
    print('Everything is ok')
    main()

schedule.every().hour.at(":05").do(main)
a = 0
while True:
    schedule.run_pending()
    time.sleep(1)
    a += 1
    print(a)




