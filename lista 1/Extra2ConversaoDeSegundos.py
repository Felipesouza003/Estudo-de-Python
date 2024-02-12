segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // (24*3600)
restoHoras = segundos % (24*3600)
horas = restoHoras // 3600
restoMinutos = restoHoras % 3600
minutos = restoMinutos // 60
restoSegundos = restoMinutos % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", restoSegundos, "segundos.")