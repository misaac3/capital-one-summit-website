import csv
import json

filename = 'listings.csv'
file = open(filename, encoding="utf8")
reader = csv.DictReader(file)

# l = []
# for line in reader:
#     if line['neighbourhood_cleansed'] in l:
#         continue
#     else:
#         l.append(line['neighbourhood_cleansed'])
# l.sort()
# st = '{'
# for x in l:
#     st += "\'" + x + "\'" + ': 0, '
# st += '}'
#
# print(st)
num = 2
worst_score = 100
ws_num = 0

price_neighbor_dict = {'Bayview': 0, 'Bernal Heights': 0, 'Castro/Upper Market': 0, 'Chinatown': 0,
                       'Crocker Amazon': 0, 'Diamond Heights': 0, 'Downtown/Civic Center': 0, 'Excelsior': 0,
                       'Financial District': 0, 'Glen Park': 0, 'Golden Gate Park': 0, 'Haight Ashbury': 0,
                       'Inner Richmond': 0, 'Inner Sunset': 0, 'Lakeshore': 0, 'Marina': 0, 'Mission': 0,
                       'Nob Hill': 0, 'Noe Valley': 0, 'North Beach': 0, 'Ocean View': 0, 'Outer Mission': 0,
                       'Outer Richmond': 0, 'Outer Sunset': 0, 'Pacific Heights': 0, 'Parkside': 0,
                       'Potrero Hill': 0, 'Presidio': 0, 'Presidio Heights': 0, 'Russian Hill': 0, 'Seacliff': 0,
                       'South of Market': 0, 'Treasure Island/YBI': 0, 'Twin Peaks': 0, 'Visitacion Valley': 0,
                       'West of Twin Peaks': 0, 'Western Addition': 0, }


num_neighbor_dict = {'Bayview': 0, 'Bernal Heights': 0, 'Castro/Upper Market': 0, 'Chinatown': 0,
                       'Crocker Amazon': 0, 'Diamond Heights': 0, 'Downtown/Civic Center': 0, 'Excelsior': 0,
                       'Financial District': 0, 'Glen Park': 0, 'Golden Gate Park': 0, 'Haight Ashbury': 0,
                       'Inner Richmond': 0, 'Inner Sunset': 0, 'Lakeshore': 0, 'Marina': 0, 'Mission': 0,
                       'Nob Hill': 0, 'Noe Valley': 0, 'North Beach': 0, 'Ocean View': 0, 'Outer Mission': 0,
                       'Outer Richmond': 0, 'Outer Sunset': 0, 'Pacific Heights': 0, 'Parkside': 0,
                       'Potrero Hill': 0, 'Presidio': 0, 'Presidio Heights': 0, 'Russian Hill': 0, 'Seacliff': 0,
                       'South of Market': 0, 'Treasure Island/YBI': 0, 'Twin Peaks': 0, 'Visitacion Valley': 0,
                       'West of Twin Peaks': 0, 'Western Addition': 0, }

price_review_dict = {}
review_neighbor_dict = {}

count = 0

for line in reader:
    # print(num_neighbor_dict[line['neighbourhood_cleansed']])

    price = line['price']
    if "," in price:
        price = price.replace(",", "")

    price = int(price[1:-3])
    if price is not '' and price is not ' ':
        #print(price, "AHHHHH ")
        neighbourhood = line['neighbourhood_cleansed']
        if neighbourhood not in price_neighbor_dict.keys():
            price_neighbor_dict[neighbourhood] += int(price)
            num_neighbor_dict[neighbourhood] += 1
            count += 1
        else:
            price_neighbor_dict[neighbourhood] += int(price)
            num_neighbor_dict[neighbourhood] += 1
            count += 1

neighbor_avg_price_dict = {'Bayview': 0, 'Bernal Heights': 0, 'Castro/Upper Market': 0, 'Chinatown': 0,
                       'Crocker Amazon': 0, 'Diamond Heights': 0, 'Downtown/Civic Center': 0, 'Excelsior': 0,
                       'Financial District': 0, 'Glen Park': 0, 'Golden Gate Park': 0, 'Haight Ashbury': 0,
                       'Inner Richmond': 0, 'Inner Sunset': 0, 'Lakeshore': 0, 'Marina': 0, 'Mission': 0,
                       'Nob Hill': 0, 'Noe Valley': 0, 'North Beach': 0, 'Ocean View': 0, 'Outer Mission': 0,
                       'Outer Richmond': 0, 'Outer Sunset': 0, 'Pacific Heights': 0, 'Parkside': 0,
                       'Potrero Hill': 0, 'Presidio': 0, 'Presidio Heights': 0, 'Russian Hill': 0, 'Seacliff': 0,
                       'South of Market': 0, 'Treasure Island/YBI': 0, 'Twin Peaks': 0, 'Visitacion Valley': 0,
                       'West of Twin Peaks': 0, 'Western Addition': 0, }

for x in price_neighbor_dict.keys():
    print(x, ':', num_neighbor_dict[x])
    if num_neighbor_dict[x] is not 0:
        neighbor_avg_price_dict[x] = (price_neighbor_dict[x] / num_neighbor_dict[x])
    else:
        neighbor_avg_price_dict[x] = 0
print(neighbor_avg_price_dict.items())

fileContent = json.dumps(neighbor_avg_price_dict, sort_keys=True, indent=4)
print(fileContent)

newFile = open('AveragePricePerNeighbourhood.json', 'w')
newFile.write(fileContent)
newFile.close()

# print('\nthe worst score is', worst_score, 'at line', ws_num)
