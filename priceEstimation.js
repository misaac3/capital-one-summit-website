function estimatePrice() {
    var geolocationArray = document.getElementById("optimizationForm");

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
    var averageAvailability =  [
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

    var minArray =  get_distance_between_geolocations(lat, long);

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

    var estimatedRevenue = estimatedAvailability * estimatedAveragePrice;

    str += "<br/>estimatedRevenue = " + estimatedRevenue;

    var div = document.getElementById("optimizationDiv");
    div.innerHTML = str;

    return estimatedAveragePrice;
}