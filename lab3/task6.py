stations = [120, 260, 410, 560, 730, 890, 1040, 1190, 1360, 1520, 1680, 1840, 2010, 2170, 2330, 2480, 2650, 2810, 2970, 3140, 3300, 3460, 3630, 3790, 3950, 4120, 4280, 4440, 4610, 4770, 4930, 5100, 5260, 5420, 5590, 5750, 5910, 6080, 6240, 6400, 6570, 6730, 6890, 7060, 7220, 7380, 7550, 7710, 7870, 8040, 8200, 8360, 8530, 8690, 8850, 9020, 9180, 9340, 9510, 9670, 9830, 10000, 10160, 10320]

def refueling(stations):
    total_distance = 10451
    max_path = 500
    current = 0
    selected_stations = []
    stations = [0] + stations + [total_distance]  # старт и финиш

    i = 0
    n = len(stations)

    while current < total_distance:
        last = current

        # ищем самую дальнюю достижимую станцию
        while i < n and stations[i] <= current + max_path:
            last = stations[i]
            i += 1

        # если не смогли продвинуться
        if last == current:
            return None

        # если это не финиш — заправляемся
        if last < total_distance:
            selected_stations.append(last)

        current = last

    return selected_stations


result = refueling(stations)

if result is None:
    print("Маршрут невозможен")
else:
    print(f"Кол-во остановок: {len(result)}")
    print("Остановки:", result)