categories = []
count = 0
values = []
countries = 0
with open('world_population.csv', 'r') as reader:
    for line in reader:
        data = line.split(',')
        if data[4] == 'South America':
            countries += 1
            values.append([data[2],data[3],data[5],data[7],data[8],data[9]])
        elif count == 0:
            categories.extend([data[2],data[3],data[5],data[7],data[8],data[9]])
            count += 1 
reader.close()

latam_countries = []

for i in range(countries):
    country_dict = {categories[j]: values[i][j] for j in range(len(categories))}
    latam_countries.append(country_dict)

print(latam_countries[2])
