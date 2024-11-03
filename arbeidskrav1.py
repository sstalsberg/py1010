"""
Lite program som beregner årlige kostnader
mellom bensinbil og elbil basert på antall kjørte km

Steinar Stalsberg
2024 11 01
"""

# Årlige kostnader Bensinbil
b_insurance = 7500 # årlig forsikring bensinbil
b_fuel = 1.0 # driftstoff per km
b_toll = 0.3 # bomavgift per km

# Årlige kostnader Elbil
el_insurance = 5000 # årlig forsikring elbil
el_fuel = 0.2*2.00 # driftstoff per km (kWh)
el_toll = 0.1 # bomavgift per km

# Felleskostnader
tfa = 8.38 # trafikkforsikringsavgift per dag

# Input km
km = input("Skriv inn antall kjørte km per år eller trykk enter for å bruke standard på 10000km: ")
if not km: km = 10000
else: km = int(km)

# Beregnet kostnad ved bensinbil per år
b_cost = b_insurance + b_fuel*km + b_toll*km + tfa*365

# Beregnet kostnad ved elbil per år
el_cost = el_insurance + el_fuel*km + el_toll*km + tfa*365

# Beregnet differanse
diff = b_cost - el_cost

# Print i konsoll
print("Kostnad med bensinbil per år er:", round(b_cost), "kr")
print("Kostnad med elbil per år er:", round(el_cost), "kr")
print("Differansen mellom elbil og bensinbil er:", round(diff), "kr per år")