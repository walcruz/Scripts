from datetime import datetime
import pytz

def get_time_in_timezone(timezone):
    tz = pytz.timezone(timezone)
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

timezones = {
    'Argentina': 'America/Argentina/Buenos_Aires',
    'Colombia': 'America/Bogota',
    'Italia': 'Europe/Rome'
}

for country, tz in timezones.items():
    print(f'La hora en {country} es: {get_time_in_timezone(tz)}')
    print('Finish!')