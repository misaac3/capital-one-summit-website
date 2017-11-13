function get_distance_between_geolocations(lat1, long1){

var averageGeolocation = [
    ["Bayview",
        37.72897909177132,
        -122.39037215876513
    ],
    ["Bernal Heights",
        37.7418426067524,
        -122.41621994967791
    ],
    ["Castro/Upper Market",
        37.76253372103045,
        -122.43451560740377
    ],
    ["Chinatown",
        37.791897441620854,
        -122.4067313429551
    ],
    ["Crocker Amazon",
        37.71040731685269,
        -122.43932836520828
    ],
    ["Diamond Heights",
        37.74304506999425,
        -122.44125102980082
    ],
    ["Downtown/Civic Center",
        37.78560143572433,
        -122.41395224396892
    ],
    ["Excelsior",
        37.7254153490687,
        -122.42375799245458
    ],
    ["Financial District",
        37.790164671583234,
        -122.40008680887165
    ],
    ["Glen Park",
        37.73775177240531,
        -122.43144318649968
    ],
    ["Golden Gate Park",
        37.76873031253758,
        -122.47950012542148
    ],
    ["Haight Ashbury",
        37.770057553641045,
        -122.44599979350366
    ],
    ["Inner Richmond",
        37.77913486021979,
        -122.46386416260964
    ],
    ["Inner Sunset",
        37.76044626890579,
        -122.46571425847957
    ],
    ["Lakeshore",
        37.7202812447874,
        -122.48186651856248
    ],
    ["Marina",
        37.80082494704437,
        -122.43486273706766
    ],
    ["Mission",
        37.75837549504547,
        -122.41716062889334
    ],
    ["Nob Hill",
        37.792982547302664,
        -122.4157895579223
    ],
    ["Noe Valley",
        37.74978122253156,
        -122.4320677026198
    ],
    ["North Beach",
        37.80195992368156,
        -122.4082846068969
    ],
    ["Ocean View",
        37.71763189395111,
        -122.4610276172388
    ],
    ["Outer Mission",
        37.72757105748836,
        -122.44146423619247
    ],
    ["Outer Richmond",
        37.77733891057393,
        -122.49218853351627
    ],
    ["Outer Sunset",
        37.75643604285866,
        -122.49511354369056
    ],
    ["Pacific Heights",
        37.79234269701417,
        -122.43367885958396
    ],
    ["Parkside",
        37.74206020704652,
        -122.48704263997358
    ],
    ["Potrero Hill",
        37.75904519536651,
        -122.3976709316644
    ],
    ["Presidio",
        37.79968358024673,
        -122.45846648926234
    ],
    ["Presidio Heights",
        37.78477799121847,
        -122.45403477632928
    ],
    ["Russian Hill",
        37.801138401227604,
        -122.41850050286602
    ],
    ["Seacliff",
        37.78304688501543,
        -122.49724889226714
    ],
    ["South of Market",
        37.7783299914222,
        -122.40328221692424
    ],
    ["Treasure Island/YBI",
        37.823667304751304,
        -122.37399167438446
    ],
    ["Twin Peaks",
        37.753636259384066,
        -122.44715071108845
    ],
    ["Visitacion Valley",
        37.71607140500467,
        -122.40708167842531
    ],
    ["West of Twin Peaks",
        37.73550582716622,
        -122.45899343653116
    ],
    ["Western Addition",
        37.778278307620255,
        -122.43371534399753
    ]
];
var index = 0;
var min1 = "";
var min2 = "";
var min_distance1 = Number.MAX_VALUE;
var min_distance2 = Number.MAX_VALUE;



for(i = 0; i < averageGeolocation.length; i++){
	nhood = averageGeolocation[i][0];
	lat2 = averageGeolocation[i][1];
	long2 = averageGeolocation[i][2];

	var distance = Math.sqrt(Math.pow(lat2 - lat1, 2) + Math.pow(long2 - long1, 2));

	if (distance < min_distance1) {
		min_distance2 =  min_distance1;
		min_distance1 = distance;
		min1 = nhood;
	}
	else if (distance < min_distance2) {
		min_distance2 = distance;
		min2 = nhood;
	}


}
// document.write("min1 = " + min1 + ", min2 = " + min2);
var minArray = [min1, min_distance1, min2, min_distance2];
// document.write("<br/>" + minArray);
return minArray;
}


function determineEstimatedRevenueFromGeolocation(){
	var geolocationArray = document.getElementById("optimizationForm");

	if(geolocationArray.elements[0].value === '' || geolocationArray.elements[1].value === ''){

    }
    else {
        var lat = parseFloat(geolocationArray.elements[0].value);
        var long = parseFloat(geolocationArray.elements[1].value);

        var neighborhoods = [
            "Bayview",
            "Bernal Heights",
            "Castro/Upper Market",
            "Chinatown",
            "Crocker Amazon",
            "Diamond Heights",
            "Downtown/Civic Center",
            "Excelsior",
            "Financial District",
            "Glen Park",
            "Golden Gate Park",
            "Haight Ashbury",
            "Inner Richmond",
            "Inner Sunset",
            "Lakeshore",
            "Marina",
            "Mission",
            "Nob Hill",
            "Noe Valley",
            "North Beach",
            "Ocean View",
            "Outer Mission",
            "Outer Richmond",
            "Outer Sunset",
            "Pacific Heights",
            "Parkside",
            "Potrero Hill",
            "Presidio",
            "Presidio Heights",
            "Russian Hill",
            "Seacliff",
            "South of Market",
            "Treasure Island/YBI",
            "Twin Peaks",
            "Visitacion Valley",
            "West of Twin Peaks",
            "Western Addition"
        ];
        var averagePrice = [
            120.57142857142857,
            177.72727272727272,
            248.66287878787878,
            177.35211267605635,
            118.69565217391305,
            185.28571428571428,
            153.23824451410658,
            133.75,
            228.43373493975903,
            185.0,
            267.8333333333333,
            209.36563876651982,
            187.32876712328766,
            177.9787234042553,
            157.03571428571428,
            268.4347826086956,
            199.503861003861,
            217.43506493506493,
            242.17748917748918,
            311.0877192982456,
            135.49333333333334,
            163.23,
            182.1551724137931,
            151.625,
            291.92913385826773,
            256.5285714285714,
            263.05625,
            481.25,
            247.72727272727272,
            315.01869158878503,
            179.14285714285714,
            297.5933734939759,
            85.11111111111111,
            185.55737704918033,
            115.46153846153847,
            164.5421686746988,
            274.5135135135135
        ];
        var averageAvailability = [
            18.071428571428573,
            14.987012987012987,
            14.306818181818182,
            22.309859154929576,
            21.608695652173914,
            16.785714285714285,
            17.934169278996865,
            15.041666666666666,
            20.265060240963855,
            14.066666666666666,
            18.166666666666668,
            16.422907488986784,
            16.506849315068493,
            13.74468085106383,
            18.678571428571427,
            16.211180124223603,
            13.90926640926641,
            14.266233766233766,
            15.744588744588745,
            18.973684210526315,
            18.30666666666667,
            17.12,
            14.89655172413793,
            15.488636363636363,
            14.960629921259843,
            18.857142857142858,
            15.69375,
            25.75,
            17.40909090909091,
            16.934579439252335,
            12.5,
            16.44277108433735,
            19.333333333333332,
            17.491803278688526,
            16.192307692307693,
            17.795180722891565,
            15.027027027027026
        ]

        var str = "";

        var minArray = get_distance_between_geolocations(lat, long);

        str += "min1 : " + minArray[0] + " = " + minArray[1] + ", <br/>min2 : " + minArray[2] + " = " + minArray[3];

        var nhood1 = minArray[0];
        var nhood2 = minArray[2];
        var totalDistance = minArray[1] + minArray[3];
        var percentOfNhood1 = 1 - (minArray[1] / totalDistance);
        var percentOfNhood2 = 1 - percentOfNhood1;
        str += "<br/>percentOfNhood1 = " + percentOfNhood1;
        str += "<br/>percentOfNhood2 = " + percentOfNhood2;

        var indexOfMin1 = neighborhoods.indexOf(minArray[0]);
        var indexOfMin2 = neighborhoods.indexOf(minArray[2]);

        var estimatedAveragePrice = (percentOfNhood1 * averagePrice[indexOfMin1]) + (percentOfNhood2 * averagePrice[indexOfMin2]);
        str += "<br/>estimatedAveragePrice = " + estimatedAveragePrice;

        var estimatedAvailability = (percentOfNhood1 * averageAvailability[indexOfMin1]) + (percentOfNhood2 * averageAvailability[indexOfMin2]);
        str += "<br/>estimatedAvailability = " + estimatedAvailability;

        var estimatedRevenueFor30days = estimatedAvailability * estimatedAveragePrice;

        str += "<br/>estimatedRevenueFor30days = " + estimatedRevenueFor30days;

        var estimatedWeeklyRevenue = estimatedRevenueFor30days / 30 * 7;
        var weeklyAvail = estimatedAvailability / 30 * 7;

        str += "<br/>estimatedWeeklyRevenue = " + estimatedWeeklyRevenue;

        var div = document.getElementById("estimateDiv");

        var real_str = "";
        if(percentOfNhood1 > 0.75){
            real_str += "This location is between " + nhood1 + " and " + nhood2 + ", but is much closer to " + nhood1;
        }
        else{
            real_str += "This location is between " + nhood1 + " and " + nhood2;
        }
        real_str += "<br/>Based on average price and availability of other listings in the area, this listing " +
        "could expect a weekly income of $<b>" + estimatedWeeklyRevenue.toFixed(2) + "</b> from a nightly rate of $" +
        estimatedAveragePrice.toFixed(2) + " and around " + weeklyAvail.toFixed(2) + " bookings a week.";


        div.innerHTML = real_str;

        return estimatedAveragePrice;


    }
}

function findOptimalRevenue() {
    var geolocationArray = document.getElementById("optimizationForm");
    var div = document.getElementById("optimizationDiv");

        var lat = parseFloat(geolocationArray.elements[0].value);
        var long = parseFloat(geolocationArray.elements[1].value);
        var ref = {
            "bookings": [
                27.907748465239752,
                22.91631869049607,
                24.25681142364796,
                18.545775684427436,
                12.094297122965084,
                29.632280576183234,
                16.892484113651303,
                16.554553541302415,
                16.70654774853165,
                22.907900888265544,
                2.4126854339446324,
                20.3732912723449,
                28.89983579638752,
                24.44999075614716,
                21.886016451233843,
                20.02102800278399,
                27.135493782493015,
                30.81033867423033,
                25.143144493079923,
                10.538441346595542,
                15.794515793127385,
                22.11763040554887,
                20.452920143027413,
                27.792243387693574,
                17.0406958015677,
                40.14232278076818,
                17.875503229356735,
                14.949452401010952,
                15.266262170170734,
                13.487865588052273,
                21.733801510533986,
                10.954048275648374,
                39.148411829134716,
                19.823340471092077,
                15.631623569309028,
                26.5477329251961,
                11.176201307526144
            ],
            "price": [
                192.46723079475692,
                286.4539836312009,
                459.2065335028527,
                360.612304974978,
                84.6600798607556,
                283.9760221884227,
                160.18734935358995,
                260.51639520260113,
                626.4955405699369,
                204.53482935951376,
                41.01565237705876,
                789.4650368033649,
                1050.903119868637,
                531.5215381771121,
                326.10164512338423,
                308.015815427446,
                846.6274060137821,
                1027.0112891410108,
                1382.8729471193958,
                194.7320683610046,
                103.9805623047553,
                265.41156486658645,
                362.57449344457683,
                320.6797313964643,
                444.53989047567916,
                29194.416567831402,
                282.43295102383644,
                120.74557708508846,
                75.24086355298434,
                595.0528935905414,
                108.66900755266994,
                896.4062838905586,
                114.74534501642935,
                301.6595289079229,
                73.78126324713861,
                151.04744595370192,
                223.52402615052287
            ],
            "revenue": [
                5371.327064821323,
                6564.4707790547445,
                11138.886287685778,
                6687.834917110277,
                1023.9041602899307,
                8414.857166395777,
                2705.9622541634294,
                4312.73261276856,
                10466.5776627738,
                4685.463599166047,
                98.9578670538662,
                16084.00114412744,
                30370.927602114964,
                12995.69669512351,
                7137.065969944808,
                6166.793265973241,
                22973.652711975174,
                31642.56564069243,
                34769.77432499424,
                2052.1724807236806,
                1642.3226335007234,
                5870.274897077518,
                7415.707160320546,
                8912.409144470737,
                7575.269045258271,
                1171931.6932620946,
                5048.63112810334,
                1805.0802572661285,
                1148.6467489099027,
                8025.993446530794,
                2361.790640496447,
                9819.27770833174,
                4492.098022179327,
                5979.899547890998,
                1153.320933547366,
                4009.967254211871,
                2498.149513326982
            ]
        }
        var neighborhoods = [
            "Bayview",
            "Bernal Heights",
            "Castro/Upper Market",
            "Chinatown",
            "Crocker Amazon",
            "Diamond Heights",
            "Downtown/Civic Center",
            "Excelsior",
            "Financial District",
            "Glen Park",
            "Golden Gate Park",
            "Haight Ashbury",
            "Inner Richmond",
            "Inner Sunset",
            "Lakeshore",
            "Marina",
            "Mission",
            "Nob Hill",
            "Noe Valley",
            "North Beach",
            "Ocean View",
            "Outer Mission",
            "Outer Richmond",
            "Outer Sunset",
            "Pacific Heights",
            "Parkside",
            "Potrero Hill",
            "Presidio",
            "Presidio Heights",
            "Russian Hill",
            "Seacliff",
            "South of Market",
            "Treasure Island/YBI",
            "Twin Peaks",
            "Visitacion Valley",
            "West of Twin Peaks",
            "Western Addition"
        ];

        var str = "";

        var minArray = get_distance_between_geolocations(lat, long);

        str += "min1 : " + minArray[0] + " = " + minArray[1] + ", <br/>min2 : " + minArray[2] + " = " + minArray[3];

        var nhood1 = minArray[0];
        var nhood2 = minArray[2];
        var totalDistance = minArray[1] + minArray[3];
        var percentOfNhood1 = 1 - (minArray[1] / totalDistance);
        var percentOfNhood2 = 1 - percentOfNhood1;
        str += "<br/>percentOfNhood1 = " + percentOfNhood1;
        str += "<br/>percentOfNhood2 = " + percentOfNhood2;

        var indexOfMin1 = neighborhoods.indexOf(minArray[0]);
        var indexOfMin2 = neighborhoods.indexOf(minArray[2]);

        var estimatedAveragePrice = (percentOfNhood1 * ref.price[indexOfMin1]) + (percentOfNhood2 * ref.price[indexOfMin2]);
        str += "<br/>estimatedAveragePrice = " + estimatedAveragePrice;
        var roundedEstimatedPrice = estimatedAveragePrice.toFixed(2);

        var estimatedAvailability = (percentOfNhood1 * ref.bookings[indexOfMin1]) + (percentOfNhood2 * ref.bookings[indexOfMin2]);
        str += "<br/>estimatedAvailability = " + estimatedAvailability;

        var estimatedRevenueFor30days = estimatedAvailability * estimatedAveragePrice;
        var calcRev30 = (percentOfNhood1 * ref.revenue[indexOfMin1]) + (percentOfNhood2 * ref.revenue[indexOfMin2]);
        str += "<br/>estimatedRevenueFor30days = " + estimatedRevenueFor30days;
        str += "<br/>calculatedRevenue = " + calcRev30;

        var weeklyAvail = estimatedAvailability / 30 * 7;
        var weeklyAvailFloor = weeklyAvail.toFixed(0);
        var weeklyAvailCeiling = weeklyAvail.toFixed(0);
        weeklyAvailCeiling++;

        var estimatedWeeklyRevenue = estimatedRevenueFor30days / 30 * 7;

        str += "<br/>estimatedWeeklyRevenue = " + estimatedWeeklyRevenue;

        var real_str = "";
        if(percentOfNhood1 > 0.75){
            real_str += "This location is between " + nhood1 + " and " + nhood2 + ", but is much closer to " + nhood1;
        }
        else{
            real_str += "This location is between " + nhood1 + " and " + nhood2;
        }
        real_str += "<br/>Based on the best revenue generating listings in this area, setting the price at " +
            "<b>$" + roundedEstimatedPrice + "</b>"+ " per night would lead to optimal revenue. <br/>A listing at " +
            "this geolocation would expect to have  " + weeklyAvailFloor +" and " + weeklyAvailCeiling +
            " days booked a week generating around $" + estimatedAveragePrice.toFixed(2) * weeklyAvailFloor +
            " and $" + weeklyAvailCeiling * estimatedAveragePrice.toFixed(2) + " of revenue per week.";
        div.innerHTML = real_str;

        return estimatedAveragePrice;





}
