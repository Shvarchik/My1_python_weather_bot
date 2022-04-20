import requests

def import_xml (arg):
    if arg == 1:
        file_url = 'https://xml.meteoservice.ru/export/gismeteo/point/37.xml'
    elif arg == 2:
        file_url = 'https://xml.meteoservice.ru/export/gismeteo/point/69.xml'

    weather_xml = requests.get(file_url)
    return weather_xml.content

    # чтобы создать файл и записать туда содержимое: 
    # with open ('имя файла.xml', 'wb') as <имя файловой пременной>:
    #     <имя файловой пременной.write(weather_xml.content)

