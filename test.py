from flask import Flask, jsonify, request
import json


app = Flask(__name__)


states = [
  {
    "id": 0,
    "stateAbbr": "US",
    "stateName": "United States",
    "revenuePerCapita": 5768,
    "revenuePerCapitaRank": ""
  },
  {
    "id": 1,
    "stateAbbr": "AL",
    "stateName": "Alabama",
    "revenuePerCapita": 5068,
    "revenuePerCapitaRank": 37
  },
  {
    "id": 2,
    "stateAbbr": "AK",
    "stateName": "Alaska",
    "revenuePerCapita": 10418,
    "revenuePerCapitaRank": 2
  },
  {
    "id": 4,
    "stateAbbr": "AZ",
    "stateName": "Arizona",
    "revenuePerCapita": 4571,
    "revenuePerCapitaRank": 45
  },
  {
    "id": 5,
    "stateAbbr": "AR",
    "stateName": "Arkansas",
    "revenuePerCapita": 6507,
    "revenuePerCapitaRank": 17
  },
  {
    "id": 6,
    "stateAbbr": "CA",
    "stateName": "California",
    "revenuePerCapita": 6782,
    "revenuePerCapitaRank": 15
  },
  {
    "id": 8,
    "stateAbbr": "CO",
    "stateName": "Colorado",
    "revenuePerCapita": 5285,
    "revenuePerCapitaRank": 34
  },
  {
    "id": 9,
    "stateAbbr": "CT",
    "stateName": "Connecticut",
    "revenuePerCapita": 7418,
    "revenuePerCapitaRank": 10
  },
  {
    "id": 10,
    "stateAbbr": "DE",
    "stateName": "Delaware",
    "revenuePerCapita": 8006,
    "revenuePerCapitaRank": 7
  },
  {
    "id": 12,
    "stateAbbr": "FL",
    "stateName": "Florida",
    "revenuePerCapita": 3921,
    "revenuePerCapitaRank": 49
  },
  {
    "id": 13,
    "stateAbbr": "GA",
    "stateName": "Georgia",
    "revenuePerCapita": 3868,
    "revenuePerCapitaRank": 50
  },
  {
    "id": 15,
    "stateAbbr": "HI",
    "stateName": "Hawaii",
    "revenuePerCapita": 8252,
    "revenuePerCapitaRank": 6
  },
  {
    "id": 16,
    "stateAbbr": "ID",
    "stateName": "Idaho",
    "revenuePerCapita": 4789,
    "revenuePerCapitaRank": 43
  },
  {
    "id": 17,
    "stateAbbr": "IL",
    "stateName": "Illinois",
    "revenuePerCapita": 5443,
    "revenuePerCapitaRank": 31
  },
  {
    "id": 18,
    "stateAbbr": "IN",
    "stateName": "Indiana",
    "revenuePerCapita": 5293,
    "revenuePerCapitaRank": 32
  },
  {
    "id": 19,
    "stateAbbr": "IA",
    "stateName": "Iowa",
    "revenuePerCapita": 6504,
    "revenuePerCapitaRank": 18
  },
  {
    "id": 20,
    "stateAbbr": "KS",
    "stateName": "Kansas",
    "revenuePerCapita": 5537,
    "revenuePerCapitaRank": 29
  },
  {
    "id": 21,
    "stateAbbr": "KY",
    "stateName": "Kentucky",
    "revenuePerCapita": 6019,
    "revenuePerCapitaRank": 24
  },
  {
    "id": 22,
    "stateAbbr": "LA",
    "stateName": "Louisiana",
    "revenuePerCapita": 5014,
    "revenuePerCapitaRank": 39
  },
  {
    "id": 23,
    "stateAbbr": "ME",
    "stateName": "Maine",
    "revenuePerCapita": 6025,
    "revenuePerCapitaRank": 22
  },
  {
    "id": 24,
    "stateAbbr": "MD",
    "stateName": "Maryland",
    "revenuePerCapita": 6460,
    "revenuePerCapitaRank": 19
  },
  {
    "id": 25,
    "stateAbbr": "MA",
    "stateName": "Massachusetts",
    "revenuePerCapita": 7650,
    "revenuePerCapitaRank": 9
  },
  {
    "id": 26,
    "stateAbbr": "MI",
    "stateName": "Michigan",
    "revenuePerCapita": 6019,
    "revenuePerCapitaRank": 23
  },
  {
    "id": 27,
    "stateAbbr": "MN",
    "stateName": "Minnesota",
    "revenuePerCapita": 7372,
    "revenuePerCapitaRank": 11
  },
  {
    "id": 28,
    "stateAbbr": "MS",
    "stateName": "Mississippi",
    "revenuePerCapita": 6181,
    "revenuePerCapitaRank": 20
  },
  {
    "id": 29,
    "stateAbbr": "MO",
    "stateName": "Missouri",
    "revenuePerCapita": 4609,
    "revenuePerCapitaRank": 44
  },
  {
    "id": 30,
    "stateAbbr": "MT",
    "stateName": "Montana",
    "revenuePerCapita": 6076,
    "revenuePerCapitaRank": 21
  },
  {
    "id": 31,
    "stateAbbr": "NE",
    "stateName": "Nebraska",
    "revenuePerCapita": 5252,
    "revenuePerCapitaRank": 35
  },
  {
    "id": 32,
    "stateAbbr": "NV",
    "stateName": "Nevada",
    "revenuePerCapita": 4521,
    "revenuePerCapitaRank": 46
  },
  {
    "id": 33,
    "stateAbbr": "NH",
    "stateName": "New Hampshire",
    "revenuePerCapita": 4814,
    "revenuePerCapitaRank": 42
  },
  {
    "id": 34,
    "stateAbbr": "NJ",
    "stateName": "New Jersey",
    "revenuePerCapita": 6773,
    "revenuePerCapitaRank": 16
  },
  {
    "id": 35,
    "stateAbbr": "NM",
    "stateName": "New Mexico",
    "revenuePerCapita": 8316,
    "revenuePerCapitaRank": 5
  },
  {
    "id": 36,
    "stateAbbr": "NY",
    "stateName": "New York",
    "revenuePerCapita": 7921,
    "revenuePerCapitaRank": 8
  },
  {
    "id": 37,
    "stateAbbr": "NC",
    "stateName": "North Carolina",
    "revenuePerCapita": 4946,
    "revenuePerCapitaRank": 40
  },
  {
    "id": 38,
    "stateAbbr": "ND",
    "stateName": "North Dakota",
    "revenuePerCapita": 11627,
    "revenuePerCapitaRank": 1
  },
  {
    "id": 39,
    "stateAbbr": "OH",
    "stateName": "Ohio",
    "revenuePerCapita": 5630,
    "revenuePerCapitaRank": 28
  },
  {
    "id": 40,
    "stateAbbr": "OK",
    "stateName": "Oklahoma",
    "revenuePerCapita": 5515,
    "revenuePerCapitaRank": 30
  },
  {
    "id": 41,
    "stateAbbr": "OR",
    "stateName": "Oregon",
    "revenuePerCapita": 6990,
    "revenuePerCapitaRank": 13
  },
  {
    "id": 42,
    "stateAbbr": "PA",
    "stateName": "Pennsylvania",
    "revenuePerCapita": 5837,
    "revenuePerCapitaRank": 25
  },
  {
    "id": 44,
    "stateAbbr": "RI",
    "stateName": "Rhode Island",
    "revenuePerCapita": 6972,
    "revenuePerCapitaRank": 14
  },
  {
    "id": 45,
    "stateAbbr": "SC",
    "stateName": "South Carolina",
    "revenuePerCapita": 5044,
    "revenuePerCapitaRank": 38
  },
  {
    "id": 46,
    "stateAbbr": "SD",
    "stateName": "South Dakota",
    "revenuePerCapita": 4857,
    "revenuePerCapitaRank": 41
  },
  {
    "id": 47,
    "stateAbbr": "TN",
    "stateName": "Tennessee",
    "revenuePerCapita": 4187,
    "revenuePerCapitaRank": 48
  },
  {
    "id": 48,
    "stateAbbr": "TX",
    "stateName": "Texas",
    "revenuePerCapita": 4516,
    "revenuePerCapitaRank": 47
  },
  {
    "id": 49,
    "stateAbbr": "UT",
    "stateName": "Utah",
    "revenuePerCapita": 5229,
    "revenuePerCapitaRank": 36
  },
  {
    "id": 50,
    "stateAbbr": "VT",
    "stateName": "Vermont",
    "revenuePerCapita": 9598,
    "revenuePerCapitaRank": 4
  },
  {
    "id": 51,
    "stateAbbr": "VA",
    "stateName": "Virginia",
    "revenuePerCapita": 5287,
    "revenuePerCapitaRank": 33
  },
  {
    "id": 53,
    "stateAbbr": "WA",
    "stateName": "Washington",
    "revenuePerCapita": 5779,
    "revenuePerCapitaRank": 27
  },
  {
    "id": 54,
    "stateAbbr": "WV",
    "stateName": "West Virginia",
    "revenuePerCapita": 7090,
    "revenuePerCapitaRank": 12
  },
  {
    "id": 55,
    "stateAbbr": "WI",
    "stateName": "Wisconsin",
    "revenuePerCapita": 5800,
    "revenuePerCapitaRank": 26
  },
  {
    "id": 56,
    "stateAbbr": "WY",
    "stateName": "Wyoming",
    "revenuePerCapita": 10314,
    "revenuePerCapitaRank": 3
  }
]
@app.route('/')
def index():
    return 'Hello States!!!'

# GET /states/id
#GET /states

@app.route('/states')
def get_states():
    return jsonify({'states': states})

#POST /States

# {
#     "id": 56,
#     "stateAbbr": "WY",
#     "stateName": "Wyoming",
#     "revenuePerCapita": 10314,
#     "revenuePerCapitaRank": 3
#   }

def validStateObject(stateObject):
    if ("id" in stateObject and "stateAbbr" in stateObject and "stateName" in stateObject and "revenuePerCapita" in stateObject and "revenuePerCapitaRank" in stateObject):
        return True
    else:
        return False
        
        missing_stateName = {
            "id": 56,
            "stateAbbr": "WY",
            "revenuePerCapita": 10314,
            "revenuePerCapitaRank": 3

        }
@app.route('/states', methods=["POST"])
def add_state():
    return jsonify(request.get_json())


@app.route('/states/<int:id>')
def get_state_by_id(id):
    
    return_value ={}
    for state in states:
        if state['id']== id:
            return_value = {
                'stateAbbr': state["stateAbbr"],
                'stateName': state["stateName"],
                'revenuePerCapita': state["revenuePerCapita"],
                'revenuePerCapitaRank': state["revenuePerCapitaRank"]
            }
    return jsonify(return_value)

app.run(port=5000)