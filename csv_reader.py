import csv
import json
import copy

filename = 'listings.csv'
file = open(filename, encoding="utf8")
reader = csv.DictReader(file)


price_count_dict = {'between $0 and $50': 0, 'between $51 and $100': 0, 'between $101 and $150': 0,
                    'between $151 and $200': 0, 'between $201 and $250': 0, 'between $251 and $300': 0,
                    'between $301 and $350': 0, 'between $351 and $400': 0, 'between $401 and $450': 0,
                    'between $451 and $500': 0, 'between $501 and $600': 0, 'between $601 and $700': 0,
                    'between $701 and $800': 0, 'between $801 and $900': 0, 'between $901 and $1000': 0,
                    'between $1000 and $2000': 0, 'between $2001 and $10000': 0}

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
price_review_dict = {}
price_count_dict_test = {49: 0, 220: 0, 100: 0, 117: 0, 200: 0, 162: 0, 230: 0, 173: 0, 600: 0, 250: 0, 300: 0, 189: 0, 130: 0, 90: 0, 95: 0, 325: 0, 119: 0, 134: 0, 490: 0, 140: 0, 185: 0, 550: 0, 113: 0, 115: 0, 155: 0, 45: 0, 169: 0, 186: 0, 77: 0, 235: 0, 80: 0, 125: 0, 40: 0, 500: 0, 79: 0, 575: 0, 65: 0, 2000: 0, 51: 0, 159: 0, 120: 0, 50: 0, 75: 0, 55: 0, 450: 0, 150: 0, 170: 0, 190: 0, 350: 0, 4000: 0, 349: 0, 133: 0, 232: 0, 99: 0, 145: 0, 215: 0, 175: 0, 165: 0, 149: 0, 240: 0, 206: 0, 74: 0, 105: 0, 59: 0, 299: 0, 68: 0, 211: 0, 85: 0, 97: 0, 318: 0, 285: 0, 375: 0, 89: 0, 127: 0, 1500: 0, 139: 0, 69: 0, 110: 0, 148: 0, 158: 0, 194: 0, 800: 0, 400: 0, 135: 0, 70: 0, 180: 0, 1750: 0, 126: 0, 255: 0, 700: 0, 34: 0, 275: 0, 42: 0, 225: 0, 108: 0, 650: 0, 341: 0, 199: 0, 33: 0, 151: 0, 76: 0, 98: 0, 52: 0, 1000: 0, 78: 0, 399: 0, 207: 0, 320: 0, 101: 0, 202: 0, 71: 0, 107: 0, 196: 0, 463: 0, 195: 0, 138: 0, 239: 0, 160: 0, 129: 0, 260: 0, 168: 0, 295: 0, 219: 0, 109: 0, 1200: 0, 245: 0, 118: 0, 327: 0, 61: 0, 60: 0, 290: 0, 66: 0, 249: 0, 950: 0, 182: 0, 425: 0, 224: 0, 780: 0, 305: 0, 360: 0, 24: 0, 128: 0, 599: 0, 210: 0, 315: 0, 449: 0, 272: 0, 58: 0, 289: 0, 499: 0, 214: 0, 690: 0, 84: 0, 172: 0, 1400: 0, 462: 0, 122: 0, 147: 0, 72: 0, 1666: 0, 198: 0, 209: 0, 163: 0, 116: 0, 93: 0, 188: 0, 154: 0, 83: 0, 279: 0, 124: 0, 153: 0, 103: 0, 505: 0, 208: 0, 197: 0, 82: 0, 205: 0, 30: 0, 380: 0, 53: 0, 204: 0, 545: 0, 228: 0, 259: 0, 395: 0, 64: 0, 3200: 0, 102: 0, 167: 0, 539: 0, 254: 0, 385: 0, 179: 0, 728: 0, 265: 0, 88: 0, 114: 0, 495: 0, 345: 0, 280: 0, 123: 0, 1150: 0, 39: 0, 1595: 0, 270: 0, 92: 0, 86: 0, 274: 0, 346: 0, 36: 0, 174: 0, 229: 0, 329: 0, 177: 0, 10: 0, 699: 0, 178: 0, 67: 0, 725: 0, 685: 0, 48: 0, 143: 0, 164: 0, 900: 0, 355: 0, 1076: 0, 56: 0, 181: 0, 62: 0, 157: 0, 38: 0, 489: 0, 1800: 0, 381: 0, 750: 0, 1599: 0, 850: 0, 570: 0, 144: 0, 238: 0, 319: 0, 244: 0, 420: 0, 261: 0, 595: 0, 440: 0, 131: 0, 475: 0, 397: 0, 212: 0, 1425: 0, 670: 0, 2200: 0, 949: 0, 334: 0, 1250: 0, 264: 0, 695: 0, 585: 0, 217: 0, 201: 0, 2100: 0, 298: 0, 1285: 0, 142: 0, 112: 0, 106: 0, 73: 0, 184: 0, 54: 0, 136: 0, 35: 0, 227: 0, 527: 0, 5000: 0, 516: 0, 323: 0, 995: 0, 213: 0, 306: 0, 91: 0, 445: 0, 525: 0, 1300: 0, 870: 0, 191: 0, 291: 0, 267: 0, 63: 0, 498: 0, 857: 0, 358: 0, 540: 0, 975: 0, 999: 0, 3350: 0, 121: 0, 455: 0, 111: 0, 243: 0, 895: 0, 625: 0, 1040: 0, 3500: 0, 365: 0, 7000: 0, 10000: 0, 988: 0, 0: 0, 9809: 0, 688: 0, 388: 0, 459: 0, 37: 0, 161: 0, 985: 0, 87: 0, 252: 0, 333: 0, 269: 0, 9999: 0, 193: 0, 1450: 0, 2149: 0, 339: 0, 324: 0, 529: 0, 984: 0, 81: 0, 1299: 0, 795: 0, 288: 0, 389: 0, 104: 0, 152: 0, 311: 0, 340: 0, 515: 0, 166: 0, 982: 0, 322: 0, 9996: 0, 2500: 0, 390: 0, 379: 0, 94: 0, 344: 0, 520: 0, 1495: 0, 480: 0, 549: 0, 277: 0, 394: 0, 675: 0, 370: 0, 429: 0, 132: 0, 146: 0, 759: 0, 396: 0, 855: 0, 565: 0, 405: 0, 156: 0, 348: 0, 374: 0, 137: 0, 415: 0, 460: 0, 469: 0, 246: 0, 430: 0, 192: 0, 465: 0, 297: 0, 171: 0, 176: 0, 314: 0, 624: 0, 1050: 0, 347: 0, 282: 0, 248: 0, 410: 0, 330: 0, 301: 0, 187: 0, 29: 0, 22: 0, 19: 0, 1350: 0, 369: 0, 310: 0, 268: 0, 183: 0, 799: 0, 1100: 0, 258: 0, 218: 0, 1199: 0, 2250: 0, 57: 0, 2699: 0, 359: 0, 590: 0, 47: 0, 32: 0, 96: 0, 43: 0, 281: 0, 335: 0, 8500: 0, 25: 0, 3050: 0, 7500: 0, 141: 0, 367: 0, 1230: 0, 237: 0, 1700: 0, 294: 0, 1600: 0, 559: 0, 3000: 0, 1999: 0, 321: 0, 756: 0, 630: 0, 1850: 0, 5500: 0, 889: 0, 432: 0, 1395: 0, 775: 0, 223: 0, 383: 0, 485: 0, 1178: 0, 649: 0, 825: 0, 221: 0, 534: 0, 373: 0, 720: 0, 665: 0, 998: 0, 20: 0, 317: 0, 26: 0, 283: 0, 437: 0, 6000: 0, 925: 0, 1099: 0, 588: 0, 920: 0, 2800: 0, 556: 0, 1270: 0, 271: 0, 531: 0, 247: 0, 947: 0, 1024: 0, 987: 0, 414: 0, 46: 0, 233: 0, 308: 0, 1060: 0, 371: 0, 44: 0, 1785: 0, 276: 0, 8000: 0, 980: 0, 328: 0, 899: 0, 419: 0, 41: 0, 689: 0, 309: 0, 234: 0, 326: 0, 790: 0, 253: 0, }

review_neighbor_dict = copy.deepcopy(price_neighbor_dict)

neighbor_avg_price_dict = copy.deepcopy(price_neighbor_dict)

nhood_lat_dict = copy.deepcopy(price_neighbor_dict)
nhood_long_dict = copy.deepcopy(price_neighbor_dict)
nhood_avg_geolocation = copy.deepcopy(price_neighbor_dict)

s = '{'

# num_less_than_50 = 0
num_less_than_150 = 0
num_less_than_300 = 0
num_greater_than_300 = 0

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
        s += str(price) + ": 0,"
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

    price_count_dict_test[price] += 1;


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

# AveragePricePerNeighbourhoodFile = open('AveragePricePerNeighbourhood.json', 'w')
# AveragePricePerNeighbourhoodFile.write(AveragePricePerNeighbourhoodFileContent)
# AveragePricePerNeighbourhoodFile.close()
#
# nhood_avg_geolocation_file_content = json.dumps(nhood_avg_geolocation, sort_keys=True, indent=4)
# nhood_avg_geolocation_file = open('AverageGeolocationPerNeighborhod.json', 'w')
# nhood_avg_geolocation_file.write(nhood_avg_geolocation_file_content)
# nhood_avg_geolocation_file.close()

price_list.sort()
print(price_list)
s += '}'
print(s)
print(price_count_dict_test)
print('< 150:', num_less_than_150, '\n<300:', num_less_than_300,  '\n>300:', num_greater_than_300)
print('WE GUCCI MANE')

