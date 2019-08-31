import matplotlib.pyplot as plt
import numpy as np

default_snow_amounts = [30, 10, 5, 60, 30, 10, 0, 0, 30, 30, 30, 30]
snow_amounts = default_snow_amounts
start_time = 1
snow_times = np.arange(start_time, len(snow_amounts) + 10)

arguments = np.array(snow_times)
melt_func = 1/(arguments)


def ints_to_hours():
    snow_times = []
    snow_time = timedelta(hours=1)

    for i in range(len(snow_amounts)):
        snow_times.append(str(snow_time))
        snow_time += timedelta(hours=1)

    return snow_times

# как раз формула свертки тупо
def get_snow_amount(pile_number: int, hour: int):  # n-ый час в смысле начинаем с 0го часа
    if hour < pile_number:
        return 0

    snow_amount = 0

    # for rec_pile_number in range(pile_number+1):
    #     snow_amount += snow_amounts[rec_pile_number] * melt_func[hour - rec_pile_number]

    return snow_amounts[pile_number] * melt_func[hour - pile_number]


def get_points_for_nth_snow_pile_plot(n: int):
    if snow_amounts[n] == 0:
        return [0] * len(snow_times)

    points = []
    for t in range(len(snow_times)):
        points.append(get_snow_amount(n, t))  # melt_func[t] * snow_amount)

    return points

pile_plots_points = []
for i in range(len(snow_amounts)):
    pile_plots_points.append(get_points_for_nth_snow_pile_plot(i))

x = snow_times
y = np.vstack(pile_plots_points)

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()

