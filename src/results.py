from gdp_per_capita import read as read_gdp
from population import read as read_population
from medals import read as read_medals
from gdp_per_capita import GdpData
from population import PopulationData
from medals import MedalData

import math

import matplotlib.pyplot as plt
import numpy as np

def scatter(title: str, points: list[tuple[int, int]], x_axis: str, y_axis: str, filename: str|None, do_avg: bool = False):
    x, y = zip(*points)
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    if do_avg:
        slope, intercept = np.polyfit(x, y, 1)
        ax.plot(x, np.array(x) * slope + intercept,
                color="green", label="Average")
        ax.legend()
    mng = fig.canvas.manager
    if mng is not None:
        mng.set_window_title(title)
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    if filename is not None:
        fig.savefig(filename, dpi=300, bbox_inches="tight")
    plt.show()

def wealth_to_medals(medal_data: MedalData, relgdp_data: GdpData, year=2022):
    print(f"\n\nGDP/p to Medals for {year}")
    points = []
    for country in relgdp_data.by_year[year]:
        gdp = relgdp_data.by_year[year][country]
        all_medals = medal_data.by_country.get(country, None)
        if all_medals == None:
            continue # ignore unregistered countries
        medals_in_year = [medal for medal in all_medals if medal.year == year]
        num_medals = len(medals_in_year)
        print(f"{country} : GDP/p = {gdp}$ ; ∑medals = {num_medals}")
        points.append((gdp, num_medals))
    scatter(f"GDP/p to Medals {year}", points, x_axis="GDP/p", y_axis="# Medals", filename=f"../results/gdp_to_medals_{year}.png", do_avg=True)

def population_to_medals(medal_data: MedalData, population_data: PopulationData, year=2022):
    print(f"\n\nPopulation to Medals for {year}")
    points = []
    for country in population_data.by_year[year]:
        population = population_data.by_year[year][country]
        all_medals = medal_data.by_country.get(country, None)
        if all_medals == None:
            continue # ignore unregistered countries
        medals_in_year = [medal for medal in all_medals if medal.year == year]
        num_medals = len(medals_in_year)
        print(f"{country} : population = {population} ; ∑medals = {num_medals}")
        points.append((population, num_medals))
    scatter(f"Population to Medals {year}", points, x_axis="Population", y_axis="# Medals", filename=f"../results/population_to_medals_{year}.png", do_avg=True)

def total_gdp_to_medals(medal_data: MedalData, relgdp_data: GdpData, population_data: PopulationData, year=2022):
    print(f"\n\nTotal GDP to Medals for {year}")
    points = []
    for country, gdp_per_capita in relgdp_data.by_year[year].items():
        population = population_data.by_year[year].get(country, None)
        if population is None:
            continue # no population data for this country
        all_medals = medal_data.by_country.get(country, None)
        if all_medals == None:
            continue # ignore unregistered countries
        total_gdp = gdp_per_capita * population
        if total_gdp <= 0:
            continue # log scale is undefined
        gdp_db = 10 * math.log10(total_gdp)
        medals_in_year = [medal for medal in all_medals if medal.year == year]
        num_medals = len(medals_in_year)
        print(f"{country} : GDP = {total_gdp:.0f}$ ({gdp_db:.1f} dB$) ; ∑medals = {num_medals}")
        points.append((gdp_db, num_medals))
    scatter(f"Total GDP to Medals {year}", points, x_axis="GDP (dB$)", y_axis="# Medals", filename=f"../results/total_gdp_to_medals_{year}.png", do_avg=True)

if __name__ == '__main__':
    relgdp = read_gdp()
    population = read_population()
    medals = read_medals()

    wealth_to_medals(medals, relgdp)
    population_to_medals(medals, population)
    total_gdp_to_medals(medals, relgdp, population)
