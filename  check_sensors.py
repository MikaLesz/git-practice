
import yaml #brukte kI til å hjelpe meg med hvordan jeg skulle laste ned modulen yaml: pip3 install pandas pyyaml openpyxl
import json #denne trengte jeg ikke å laste ned fordi den er i python pakken jeg lastet ned
import pandas as pd #brukte kI til å hjelpe meg med hvordan jeg skulle laste ned modulen pandas: pip3 install pandas pyyaml openpyxl

#denne åpner config.yml filen og laster inn konfigurasjonen
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)
    max_days_since_calibration = config['max_days_since_calibration']
    output_file = config['output_file']

#denne laster inn sensor data fra Excel filen
sensors_df = pd.read_excel('sensors.xlsx')
#denne laster inn kalibreringsdata fra CSV filen
calibrations_df = pd.read_csv('calibrations.csv')
#denne merger sensor og kalibreringsdata basert på sensor_id
merged_df = pd.merge(sensors_df, calibrations_df, on='sensor_id')

#denne filtrerer sensorene som er eldre enn maksimum antall dager siden kalibrering
overdue_sensors_df = merged_df[merged_df['days_since_calibration'] > max_days_since_calibration]

#denne velger kun de kolonnene som skal være med i output filen
overdue_sensor_df = overdue_sensors_df[['sensor_id', 'lab_room', 'owner', 'days_since_calibration']]

#denne skriver de filtrerte sensorene til en JSON fil
with open(output_file, 'w') as file:
    json.dump(overdue_sensor_df.to_dict(orient='records'), file, indent=2)

#brukte ikke KI til mer enn det jeg skrev jeg brukte KI til tidligere, men brukte recomendasjoner direkte fra VS Code for å lage koden.