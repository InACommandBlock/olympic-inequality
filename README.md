# Olympic Medalists -- A Contest Between Humans or Countries?


## Test & Run

If the CSV/XML files are still zip-compressed, please extract them directly below `data/`.
While the parsers use built-in modules, we use `matplotlib` and `numpy` for the generation of results. You can enter the virtual environment and run the code:

**On Windows**
```ps
cd src/
./Scripts/Activate
py results.py
```
**On Linux**
```linux
cd src/
source ./bin/activate
py results.py
```
Alternatively, you can install them globally with `pip install matplotlib numpy`. Please make sure you're running the code from inside the `src/` directory.

The program will show results for 2022 by default. You can add any olympic year 1962 - 2022 as a parameter when executing.

The console output will show the individual data points in addition to the graphic representation. Close the window to move on to the next statistic. All graphs will also be output as a PNG to `results/`.


## Sources

| Data              | Source        | Format     | Years       | Notes                          |
| ----------------- | ------------- | ---------- | ----------- | ------------------------------ |
| Olympic Medals    | Kaggle.com    |  CSV       | 1896 - 2022 | Alice                          |
| GDP per Capita    | World Bank    |  XML       | 1960 - 2025 | Dennis                         |
| Population        | OECD          |  CSV       | 1961 - 2025 | Dominic                        |


[WorldBank.org](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)

[Kaggle.com](https://www.kaggle.com/datasets/cahyaalkahfi/olympic-medalist-dataset-18962024)

[OECD.org](https://data-explorer.oecd.org/vis?lc=en&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_POPULATION%40DF_POP_HIST&df%5Bag%5D=OECD.ELS.SAE&df%5Bvs%5D=1.0&dq=AUS..PS._T..&pd=2014,2024&to%5BTIME_PERIOD%5D=false)


## Concept

**These:** Wenn wir davon ausgehen, dass Talent und Genetik mehr oder weniger gleichmäßig verteilt sind, sollte die Bevölkerung eines Landes der entscheidende Faktor bei internationalem sportlichen Erfolg sein. Mehr Menschen = mehr Talent = mehr erfolgreiche Sportler*innen. Wir glauben jedoch, dass der Wohlstand eines Landes einen wesentlich stärkeren Einfluss auf dessen sportliche Erfolge hat. Unsere Vermutung ist dabei, dass eine arme Bevölkerung weniger Zeit für sportliche Aktivitäten, und weniger Chancen auf die benötigte Förderung hat.

**Methodik:** Im Internet haben wir drei Datensätze aus verlässlichen Quellen gefunden (siehe oben). Wir verwenden das BIP-pro-Person (auch _GDP per capita_ oder _GDP/p_) als Wohlstandsindikator (berechnet als `BIP~gesamt / Bevölkerungszahl`), und messen es gegen die Anzahl von olympischen Medaillen des jeweiligen Landes im Jahr 2022. Dasselbe machen wir auch mit der Bevölkerungszahl, um einen möglichen Vergleich zu schließen. Es wir dabei nicht im Rang unterschieden; Bronze, Silber und Gold werden immer als eine Medaille gewertet. Wir analysieren die Daten mithilfe eines [Scatter-Plots](https://en.wikipedia.org/wiki/Scatter_plot) und generieren eine Trendlinie durch [lineare Regression](https://en.wikipedia.org/wiki/Linear_regression).

## Results

**Ergebnisse 1:** Bei Bevölkerung-zu-Medaillen (Graph 1) sieht man bereits einen aufsteigenden Trend; Länder mit höherer Bevölkerung erreichen tendenziell mehr Medaillen. Diese Korrelation ist jedoch sichtbar schwach. Ein Großteil der Medaillen werden von Ländern unter 150 Millionen Einwohnern gewonnen, die zwei stärksten Länder (Norwegen;37;5.4mi / Canada;26;39mi) sind sogar unter 100 Millionen. Die zwei größten Länder (China;15;1425.2mi / Indien;0;1425.4mi) haben hingegen wenig Medaillen in Proportion zu ihrer Bevölkerung.
* Angaben in `Land;Anzahl Medaillen;Bevölkerung in Millionen`

**Ergebnisse 2:** Bei BIP-pro-Person-zu-Medaillen (Graph 2) sieht man ebenfalls einen aufsteigenden Trend; höherer Wohlstand führt zu mehr Medaillen. Der Trend ist hierbei schon deutlich stärker, teils auch weil die Verteilung entlang der X-Achse hier gleichmäßiger ist. Der Extremfall hier ist Lichtenstein mit 188055$ BIP pro Person und keiner Medaille. Dennoch sieht man hier eine deutliche Proportionalität; Länder mit höherem Wohlstand erreichen mehr Medaillen. Ein Großteil der Länder unter 25000$ (zum Vergleich, Deutschland hat aktuell 60496$) erreichen einzelne oder überhaupt keine Medaillen.

**Ergebnisse 3:** Nach der Auswertung der geplanten zwei Graphen entschieden wir uns einen dritten zu erstellen, in dem wir die Problematiken der anderen zu umgehen versuchten. Diese waren:
1. Die exponentielle Verteilung der Werte, zB. dass die meisten Länder zwischen 1-100 Millionen Einwohnern liegen, China und Indien jedoch mit 1,4 Milliarden Einwohnern die Skala verzerren. Dasselbe gilt auch für BIP-pro-Person, wo Werte von 301$ (Burundi) bis 188055$ (Lichtenstein) gehen.
2. Dass Bevölkerung und Wohlstand separat ausgewertet werden, obwohl sie häufig invers proportional sind. Dadurch stehen beim Wohlstand viele Länder vorne, die aber sehr wenige Einwohner haben, und ebenso stehen bei Bevölkerung viele Länder vorne, die aber sehr wenig Wohlstand haben.

Bei Dezibel-BIP (Graph 3) nutzen wir das BIP (berechnet durch `BIP/Person * Einwohnerzahl`) als kombinierten Wohlstands- und Bevölkerungsindex, und wenden zudem eine Dezibel-Skala (`y = log~10(x)`, also `x*10 -> y+1`) an, um die Werte besser zu verteilen. Im darausfolgenden Graph sieht man eine klare Tendenz; ein höheres BIP führt auch zu mehr olympischen Medaillen.

**Fazit:** Der Wohlstand eines Landes trägt deutlich zu dessen Erfolg bei den olympischen Spielen teil, noch wesentlich mehr als Einwohnerzahl. Ein Großteil der Medaillen geht meist an Länder mit mittlerem oder hohem BIP. Man sollte die Ergebnisse mit größeren Datenmengen und konkreteren Faktoren erweitern und überprüfen.

Auch wenn dieser Trend statistisch signifikant ist, ist er noch längst keine Garantie. Es gibt viele weitere Faktoren, die hier eine Rolle spielen könnten, zum Beispiel staatliche Investitionen in Sportangebote, Universitäten und Sporthochschulen, die Vermögensverteilung, uvm. Auch die bestimmten Sportarten machen vermutlich einen Unterschied, denn Sporte wie Tennis und Reiten sind oft weniger zugänglich zu niedrigen Einkommensschichten. Besonders interessant wäre eine Analyse inwiefern Siege in vorangegangenen Jahren auch zu weiteren Siegen führen, ob durch stärkere Förderungen, mehr Begeisterung, oder psychologische Einflüsse.

Weitere Forschung ist benötigt, um die gefundenen Ergebnisse zu verifizieren.

![Population to Medals 2022](https://github.com/InACommandBlock/olympic-inequality/blob/master/results/population_to_medals_2022.png)
![GDP-per-capita to Medals 2022](https://github.com/InACommandBlock/olympic-inequality/blob/master/results/gdp_to_medals_2022.png)
![GDP to Medals 2022](https://github.com/InACommandBlock/olympic-inequality/blob/master/results/total_gdp_to_medals_2022.png)
