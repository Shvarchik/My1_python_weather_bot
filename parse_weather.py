import xml.etree.ElementTree as et
import get_xml as gx

from dataclasses import dataclass
from datetime import datetime

@dataclass
class WeatherReport:
    town: str
    date: datetime
    minTemp: int
    maxTemp: int

def parse_date_temp(arg):
    root = et.fromstring(gx.import_xml(arg))
    forecasts = []
    for report in root:
        for town in report:
            for forecast in town:
                forecasts.append(WeatherReport(
                    town=town.attrib['index'],
                    date=datetime(int(forecast.attrib['year']),
                                  int(forecast.attrib['month']),
                                  int(forecast.attrib['day']),
                                  int(forecast.attrib['hour'])),
                    minTemp=forecast[2].attrib['min'],
                    maxTemp=forecast[2].attrib['max']
                ))
    rezult = []
    for fc in forecasts:
        rezult.append(f"на {fc.date.strftime('%H:%M')}: мин {fc.minTemp}\xb0C , макс {fc.maxTemp}\xb0C\n")
    return ''.join(rezult)

# import xml.etree.ElementTree as et
# import get_xml as gx

# def parse_date_temp(arg):
#     # tree = et.parse('moscow_weather.xml')  #если из файла
#     # root = tree.getroot()

#     root = et.fromstring(gx.import_xml(arg))
#     list_time = []
#     list_temperature=[]
#     for report in root:
#         for town in report:
#             for forecast in town:
#                 time = forecast.attrib ['hour']
#                 time_string = f'на {time}.00'
#                 list_time.append(time_string)
#                 temperature = forecast[2].attrib
#                 temp = ''
#                 for item in temperature:
#                     temp = f'{temp} {item} {temperature[item]}'
#                 list_temperature.append(temp)
#     date_temperature = []
#     for i in range (0,len(list_time)):
#         date_temperature.append(f'{list_time[i]}{list_temperature[i]}\n')
#     return ''.join(date_temperature)