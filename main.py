
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
        ['Id_stacji','Miasto', 'Godzna_pomiaru', 'Temperatura','Cisnienie','Suma_opadu','predkosc_wiatru','kierynek_wiatru','wiglotnosc']   # enter parameters which you want to know(your names)
    ]
    for row in loads(response.text):
        if row['stacja'] in CITTIES:
          rows.append([                     # In this list enter original names of parameters which are from IMGW site
              row['id_stacji'],
              row['stacja'],
              row['godzina_pomiaru'],
              row['temperatura'],
              row['cisnienie'],
              row['suma_opadu'],
              row['predkosc_wiatru'],
              row['kierunek_wiatru'],
              row['wilgotnosc_wzgledna']
          ])

    #
    table = AsciiTable(rows)
    print(table.table)
    df = pd.DataFrame(rows)
    print(df)

    # Alternative method of saving data to csv file( save data as string)

    # with open('/home/bartosz/Dokumenty/weather.csv', 'a') as csv_file:
    #      csv_writer = csv.writer(csv_file, delimiter=',')
    #      csv_writer.writerow(rows)

    # Enter path where file will be save
    df.to_csv('/home/bartosz/Dokumenty/weather.csv',mode= 'a', index= False)


if __name__ == '__main__':
    print('Data are saved')
    main()

# Scheduler starts every hour at xx.05
schedule.every().hour.at(":05").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)




#####new comment
