MULLVAD_CITIES = {
    "atl": (33.75375, -84.38633),   # Atlanta
    "chi": (41.8781, -87.6298),     # Chicago
    "dal": (32.89748, -97.04044),   # Dallas
    "den": (39.7392, -104.9903),    # Denver
    "hou": (29.74991, -95.35842),   # Houston
    "lax": (34.0522, -118.2437),    # Los Angeles
    "mia": (25.76168, -80.19179),   # Miami
    "mkc": (39.09972, -94.57857),   # Kansas City
    "nyc": (40.7128, -74.0060),     # New York
    "phx": (33.44838, -112.07404),  # Phoenix
    "qas": (39.04376, -77.48744),   # Ashburn VA
    "rag": (35.78774, -78.64426),   # Raleigh NC
    "sea": (47.60801, -122.33517),  # Seattle
    "sjc": (37.3382, -121.8863),    # San Jose
    "slc": (40.7587, -111.87618),   # Salt Lake City
    "txc": (26.20341, -98.23001),   # McAllen TX
    "uyk": (40.78954, -74.05650),   # Secaucus NJ
    "was": (38.88948, -77.03528),   # Washington DC
}

STATE_COORDS = {
    "Alabama": (32.806671, -86.791130),
    "Alaska": (61.3850, -152.2683),
    "Arizona": (33.5722, -112.0901),
    "Arkansas": (34.7519, -92.1315),
    "California": (38.5816, -121.4944),
    "Colorado": (39.7618, -104.8811),
    "Connecticut": (41.7640, -72.6823),
    "Delaware": (39.1582, -75.5244),
    "Florida": (27.994402, -81.760254),
    "Georgia": (33.7490, -84.3880),
    "Hawaii": (21.3043, -157.8550),
    "Idaho": (43.6178, -116.1996),
    "Illinois": (39.7980, -89.6440),
    "Indiana": (39.7684, -86.1580),
    "Iowa": (41.5908, -93.6208),
    "Kansas": (39.0481, -95.6780),
    "Kentucky": (38.1868, -84.8753),
    "Louisiana": (30.4571, -91.1874),
    "Maine": (44.3070, -69.7817),
    "Maryland": (38.9784, -76.4922),
    "Massachusetts": (42.3581, -71.0636),
    "Michigan": (42.7335, -84.5555),
    "Minnesota": (44.9551, -93.1022),
    "Mississippi": (32.2988, -90.1848),
    "Missouri": (38.5767, -92.1735),
    "Montana": (46.5851, -112.0184),
    "Nebraska": (40.8081, -96.6997),
    "Nevada": (39.3289, -116.6312),
    "New Hampshire": (43.2069, -71.5381),
    "New Jersey": (40.2206, -74.7597),
    "New Mexico": (35.6672, -105.9644),
    "New York": (42.6526, -73.7562),
    "North Carolina": (35.7804, -78.6391),
    "North Dakota": (47.4900, -100.8354),
    "Ohio": (40.417287, -82.907123),
    "Oklahoma": (35.4676, -97.5164),
    "Oregon": (44.5672, -122.1269),
    "Pennsylvania": (40.2644, -76.8665),
    "Rhode Island": (41.8231, -71.4188),
    "South Carolina": (33.9984, -81.0503),
    "South Dakota": (44.3670, -100.3464),
    "Tennessee": (36.1659, -86.7844),
    "Texas": (30.2672, -97.7431),
    "Utah": (40.7549, -111.8720),
    "Vermont": (44.0664, -72.6634),
    "Virginia": (37.5407, -77.4336),
    "Washington": (47.0352, -122.9006),
    "West Virginia": (38.3365, -81.6123),
    "Wisconsin": (43.0748, -89.3844),
    "Wyoming": (41.1403, -104.8202)
}

IANA_TO_WINDOWS = {
    "America/New_York": "Eastern Standard Time",
    "America/Detroit": "Eastern Standard Time",
    "America/Louisville": "Eastern Standard Time",
    "America/Indiana/Indianapolis": "Eastern Standard Time",
    "America/Indiana/Marengo": "Eastern Standard Time",
    "America/Indiana/Vevay": "Eastern Standard Time",

    "America/Chicago": "Central Standard Time",
    "America/Indiana/Knox": "Central Standard Time",
    "America/Indiana/Tell_City": "Central Standard Time",
    "America/Menominee": "Central Standard Time",
    "America/Matamoros": "Central Standard Time",

    "America/Denver": "Mountain Standard Time",
    "America/Boise": "Mountain Standard Time",

    "America/Phoenix": "US Mountain Standard Time",   # Arizona is different!

    "America/Los_Angeles": "Pacific Standard Time",
    "America/Anchorage": "Alaskan Standard Time",
    "America/Adak": "Aleutian Standard Time",
    "Pacific/Honolulu": "Hawaiian Standard Time"
}

STATE_TO_MULLVAD = {
    "Alabama": "us atl",
    "Alaska": None,
    "Arizona": "us phx", 
    "Arkansas": "us dal",
    "California": "us lax",
    "Colorado": "us den",
    "Connecticut": "us nyc",
    "Delaware": "us qas",
    "Florida": "us mia",
    "Georgia": "us atl",
    "Hawaii": None,
    "Idaho": "us sea",
    "Illinois": "us chi",
    "Indiana": "us chi",
    "Iowa": "us mkc",
    "Kansas": "us mkc",
    "Kentucky": "us atl",
    "Louisiana": "us hou",
    "Maine": "us nyc",
    "Maryland": "us was",
    "Massachusetts": "us nyc",
    "Michigan": "us chi",
    "Minnesota": "us chi",
    "Mississippi": "us atl",
    "Missouri": "us mkc",
    "Montana": "us sea",
    "Nebraska": "us mkc",
    "Nevada": "us lax",
    "New Hampshire": "us nyc",
    "New Jersey": "us uyk",
    "New Mexico": "us phx",
    "New York": "us nyc",
    "North Carolina": "us rag",
    "North Dakota": "us chi",
    "Ohio": "us chi",
    "Oklahoma": "us dal",
    "Oregon": "us sea",
    "Pennsylvania": "us nyc",
    "Rhode Island": "us nyc",
    "South Carolina": "us atl",
    "South Dakota": "us chi",
    "Tennessee": "us atl",
    "Texas": "us dal",
    "Utah": "us slc",
    "Vermont": "us nyc",
    "Virginia": "us qas",
    "Washington": "us sea",
    "West Virginia": "us atl",
    "Wisconsin": "us chi",
    "Wyoming": "us den",
}