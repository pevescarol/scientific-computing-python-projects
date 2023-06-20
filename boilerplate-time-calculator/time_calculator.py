def add_time(start, duration, starting_day=None):
  
    # se guarda en un dict los dias de la semana
    weekdays = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}

    # se extraen los datos de las variables start y duration 
    startArr = start.split(' ')
    startTime = startArr[0].split(':')
    ampm = 'AM'
    durationTime = duration.split(':')

    # se suma las horas con la duracion
    tmpEndHour = (int(startTime[0]) + int(durationTime[0]))

    # se agrega 12 horas a la hora final temporal en caso de que se indique 'PM' en la hora de inicio (para poder trabajar con un formato de 24 horas antes de volver a formatearlo como 12 horas).
    if startArr[1] == 'PM':
        tmpEndHour += 12

    # se suma los minutos de inicio y duración
    tmpEndMinute = (int(startTime[1]) + int(durationTime[1]))

    # si la suma de los minutos es mayor que 59, agrega una hora a la hora final
    if(tmpEndMinute > 59):
        tmpEndHour += 1
    
    # se calcula la cantidad de días que habrán transcurrido después de la duración
    days = int(tmpEndHour//24) # redondeamos hacia abajo la división

    # se calcula la hora final utilizando el operador módulo en un formato de 24 horas.
    endHour = tmpEndHour % 24

    # se cambia 'AM' a 'PM' si se ha pasado la hora del mediodía (12 horas).
    if endHour > 11:
        ampm = 'PM'

    # se convierte de nuevo al formato de 12 horas.
    if endHour > 12:
        endHour -= 12
    elif endHour == 0:
        endHour = 12

    # se calcula los minutos finales utilizando el operador módulo
    endMinute = tmpEndMinute % 60

    # se concatena la primera parte de la cadena
    endTime = str(endHour) + ':' + str(endMinute).zfill(2) + ' ' + ampm

    # si nos dan el dia de la semana, se agrega el nuevo dia
    if starting_day is not None:
        starting_day = starting_day.lower()
        weekdayNum = weekdays[starting_day]
        newWeekdayNum = (days + weekdayNum) % 7
        newWeek = list(weekdays.keys())[list(weekdays.values()).index(newWeekdayNum)]
        endTime += ', ' + newWeek.capitalize()
    
    # si el día ha cambiado, se agrega una cadena de acuerdo a este
    if days > 1:
        endTime += ' (' + str(days) + ' days later)'
    elif days > 0:
        endTime += ' (next day)'

    return endTime