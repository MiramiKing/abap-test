import requests
from datetime import datetime

time_format = f'%Y-%m-%d'
hours_format = '%H:%M:%S'

api_key = '14f2c641322081bec9023789c464203f'


def getMaxLengthDay():
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat=59.8944&lon=30.2642&appid={api_key}&units=metric'
    r = requests.post(url)
    r_dictionary = r.json()

    data = r_dictionary["daily"][0:6]
    max_length = 0
    max_hours = ""
    max_day = ""
    for d in data:
        sunset = int(d["sunset"])
        sunrise = int(d["sunrise"])
        difference = sunset-sunrise
        day = datetime.utcfromtimestamp(int(d["dt"])).strftime(time_format)
        day_length = datetime.utcfromtimestamp(
            difference).strftime(hours_format)

        if difference > max_length:
            max_length = difference
            max_hours = day_length
            max_day = day

    print(
        f'День c максимальной продолжительностью дня в Санкт Петербурге — {max_day}. Значение = {max_hours}.')


def getMinDifferFeelingTempature():
    url = f'https://api.openweathermap.org/data/2.5/forecast?id=498817&appid={api_key}&units=metric'
    r = requests.post(url)
    r_dictionary = r.json()

    data = r_dictionary["list"]
    res_col = {}
    for d in data:
        feeltempature = d["main"]["feels_like"]
        actual_temperature = d["main"]["temp"]
        day = d["dt_txt"]
        diff = abs(feeltempature-actual_temperature)
        res_col[day] = diff

    sorted_res_col = dict(sorted(res_col.items(), key=lambda k: k[1]))
    for day, value in sorted_res_col.items():
        if "00:00:00" in day or "03:00:00" in day:
            print(
                f'День c минимальной разницей в Санкт Петербурге — {day}. Разница = {value} градусов Цельсия.')
            return


getMaxLengthDay()
getMinDifferFeelingTempature()
