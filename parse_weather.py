import xml.etree.ElementTree as et
import get_xml as gx

def parse_date_temp():
    # tree = et.parse('moscow_weather.xml')  если из файла
    # root = tree.getroot()

    root = et.fromstring(gx.import_xml())
    list_time = []
    list_temperature=[]
    for report in root:
        for town in report:
            for forecast in town:
                time = forecast.attrib ['hour']
                time_string = f'на {time}.00'
                list_time.append(time_string)
                temperature = forecast[2].attrib
                temp = ''
                for item in temperature:
                    temp = f'{temp} {item} {temperature[item]}'
                list_temperature.append(temp)
    date_temperature = []
    for i in range (0,len(list_time)):
        date_temperature.append(f'{list_time[i]}{list_temperature[i]}\n')
    return ''.join(date_temperature)




