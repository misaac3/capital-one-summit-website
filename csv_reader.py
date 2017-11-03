import csv
import json
import copy

filename = 'listings.csv'
file = open(filename, encoding="utf8")
reader = csv.DictReader(file)

price_neighbor_dict = {'Bayview': 0.0, 'Bernal Heights': 0.0, 'Castro/Upper Market': 0.0, 'Chinatown': 0.0,
                       'Crocker Amazon': 0.0, 'Diamond Heights': 0.0, 'Downtown/Civic Center': 0.0, 'Excelsior': 0.0,
                       'Financial District': 0.0, 'Glen Park': 0.0, 'Golden Gate Park': 0.0, 'Haight Ashbury': 0.0,
                       'Inner Richmond': 0.0, 'Inner Sunset': 0.0, 'Lakeshore': 0.0, 'Marina': 0.0, 'Mission': 0.0,
                       'Nob Hill': 0.0, 'Noe Valley': 0.0, 'North Beach': 0.0, 'Ocean View': 0.0, 'Outer Mission': 0.0,
                       'Outer Richmond': 0.0, 'Outer Sunset': 0.0, 'Pacific Heights': 0.0, 'Parkside': 0.0,
                       'Potrero Hill': 0.0, 'Presidio': 0.0, 'Presidio Heights': 0.0, 'Russian Hill': 0.0,
                       'Seacliff': 0.0, 'South of Market': 0.0, 'Treasure Island/YBI': 0.0, 'Twin Peaks': 0.0,
                       'Visitacion Valley': 0.0, 'West of Twin Peaks': 0.0, 'Western Addition': 0.0, }

nhood_count_dict = copy.deepcopy(price_neighbor_dict)

price_review_dict = copy.deepcopy(price_neighbor_dict)

review_neighbor_dict = copy.deepcopy(price_neighbor_dict)

neighbor_avg_price_dict = copy.deepcopy(price_neighbor_dict)

nhood_lat_dict = copy.deepcopy(price_neighbor_dict)
nhood_long_dict = copy.deepcopy(price_neighbor_dict)
nhood_avg_geolocation = copy.deepcopy(price_neighbor_dict)


price_list = []
count = 0

for line in reader:
    # print(num_neighbor_dict[line['neighbourhood_cleansed']])
    if line['review_scores_rating'] is '':
        review = False
    else:
        review = line['review_scores_rating']
    price = line['price']

    nhood = line['neighbourhood_cleansed']
    latitude = line['latitude']
    longitude = line['longitude']
    
    if "," in price:
        price = price.replace(",", "")

    price = int(price[1:-3])
    if price not in price_list:
        price_list.append(price)

    if price is not '' and price is not ' ':
        if nhood not in price_neighbor_dict.keys():
            price_neighbor_dict[nhood] += int(price)
        else:
            price_neighbor_dict[nhood] += int(price)
    
    nhood_lat_dict[nhood] += float(latitude)
    nhood_long_dict[nhood] += float(longitude)
    nhood_count_dict[nhood] += 1
    count += 1

for x in price_neighbor_dict.keys():
    #print(x, ':', nhood_count_dict[x])
    if nhood_count_dict[x] is not 0:
        neighbor_avg_price_dict[x] = (price_neighbor_dict[x] / nhood_count_dict[x])
    else:
        neighbor_avg_price_dict[x] = 0
    nhood_avg_geolocation[x] = [(nhood_lat_dict[x]/nhood_count_dict[x]), (nhood_long_dict[x]/nhood_count_dict[x])]

neighbourhood_list = []
avg_price_list = []


for x in neighbor_avg_price_dict:
    neighbourhood_list.append(x)
    avg_price_list.append(neighbor_avg_price_dict[x])

neighbourhood_avgPrice_dict = {'x': neighbourhood_list, 'y': avg_price_list, 'type': 'bar'}
AveragePricePerNeighbourhoodFileContent = json.dumps(neighbourhood_avgPrice_dict, sort_keys=True, indent=4)

AveragePricePerNeighbourhoodFile = open('AveragePricePerNeighbourhood.json', 'w')
AveragePricePerNeighbourhoodFile.write(AveragePricePerNeighbourhoodFileContent)
AveragePricePerNeighbourhoodFile.close()

nhood_avg_geolocation_file_content = json.dumps(nhood_avg_geolocation, sort_keys=True, indent=4)
nhood_avg_geolocation_file = open('AverageGeolocationPerNeighborhod.json', 'w')
nhood_avg_geolocation_file.write(nhood_avg_geolocation_file_content)
nhood_avg_geolocation_file.close()

price_list.sort()
print(price_list)
print('WE GUCCI MANE')

