import pathlib

cur_path = pathlib.Path(__file__).parent.resolve()
fallback_icon = "internet-services"

prefix_data = [
    {
      "code": "+7 840",
      "iso": "",
      "name": "Abkhazia"
    },
    {
      "code": "+93",
      "iso": "af",
      "name": "Afghanistan"
    },
    {
      "code": "+355",
      "iso": "al",
      "name": "Albania"
    },
    {
      "code": "+213",
      "iso": "dz",
      "name": "Algeria"
    },
    {
      "code": "+1 684",
      "iso": "as",
      "name": "American Samoa"
    },
    {
      "code": "+376",
      "iso": "ad",
      "name": "Andorra"
    },
    {
      "code": "+244",
      "iso": "ao",
      "name": "Angola"
    },
    {
      "code": "+1 264",
      "iso": "ai",
      "name": "Anguilla"
    },
    {
      "code": "+1 268",
      "iso": "ag",
      "name": "Antigua and Barbuda"
    },
    {
      "code": "+54",
      "iso": "ag",
      "name": "Argentina"
    },
    {
      "code": "+374",
      "iso": "am",
      "name": "Armenia"
    },
    {
      "code": "+297",
      "iso": "aw",
      "name": "Aruba"
    },
    {
      "code": "+247",
      "iso": "",
      "name": "Ascension"
    },
    {
      "code": "+61",
      "iso": "au",
      "name": "Australia"
    },
    {
      "code": "+672",
      "iso": "",
      "name": "Australian External Territories"
    },
    {
      "code": "+43",
      "iso": "at",
      "name": "Austria"
    },
    {
      "code": "+994",
      "iso": "az",
      "name": "Azerbaijan"
    },
    {
      "code": "+1 242",
      "iso": "bs",
      "name": "Bahamas"
    },
    {
      "code": "+973",
      "iso": "ah",
      "name": "Bahrain"
    },
    {
      "code": "+880",
      "iso": "ad",
      "name": "Bangladesh"
    },
    {
      "code": "+1 246",
      "iso": "bb",
      "name": "Barbados"
    },
    {
      "code": "+1 268",
      "iso": "ag",
      "name": "Barbuda"
    },
    {
      "code": "+375",
      "iso": "by",
      "name": "Belarus"
    },
    {
      "code": "+32",
      "iso": "be",
      "name": "Belgium"
    },
    {
      "code": "+501",
      "iso": "bz",
      "name": "Belize"
    },
    {
      "code": "+229",
      "iso": "bj",
      "name": "Benin"
    },
    {
      "code": "+1 441",
      "iso": "bm",
      "name": "Bermuda"
    },
    {
      "code": "+975",
      "iso": "bt",
      "name": "Bhutan"
    },
    {
      "code": "+591",
      "iso": "bo",
      "name": "Bolivia"
    },
    {
      "code": "+387",
      "iso": "ba",
      "name": "Bosnia and Herzegovina"
    },
    {
      "code": "+267",
      "iso": "bw",
      "name": "Botswana"
    },
    {
      "code": "+55",
      "iso": "br",
      "name": "Brazil"
    },
    {
      "code": "+246",
      "iso": "io",
      "name": "British Indian Ocean Territory"
    },
    {
      "code": "+1 284",
      "iso": "vg",
      "name": "British Virgin Islands"
    },
    {
      "code": "+673",
      "iso": "bn",
      "name": "Brunei"
    },
    {
      "code": "+359",
      "iso": "bg",
      "name": "Bulgaria"
    },
    {
      "code": "+226",
      "iso": "bf",
      "name": "Burkina Faso"
    },
    {
      "code": "+257",
      "iso": "bi",
      "name": "Burundi"
    },
    {
      "code": "+855",
      "iso": "kh",
      "name": "Cambodia"
    },
    {
      "code": "+237",
      "iso": "cm",
      "name": "Cameroon"
    },
    {
      "code": "+1",
      "iso": "ca",
      "name": "Canada"
    },
    {
      "code": "+238",
      "iso": "cv",
      "name": "Cape Verde"
    },
    {
      "code": "+ 345",
      "iso": "ky",
      "name": "Cayman Islands"
    },
    {
      "code": "+236",
      "iso": "td",
      "name": "Central African Republic"
    },
    {
      "code": "+235",
      "iso": "td",
      "name": "Chad"
    },
    {
      "code": "+56",
      "iso": "cl",
      "name": "Chile"
    },
    {
      "code": "+86",
      "iso": "cn",
      "name": "China"
    },
    {
      "code": "+61",
      "iso": "cx",
      "name": "Christmas Island"
    },
    {
      "code": "+61",
      "iso": "cc",
      "name": "Cocos-Keeling Islands"
    },
    {
      "code": "+57",
      "iso": "co",
      "name": "Colombia"
    },
    {
      "code": "+269",
      "iso": "km",
      "name": "Comoros"
    },
    {
      "code": "+242",
      "iso": "cg",
      "name": "Congo"
    },
    {
      "code": "+243",
      "iso": "cd",
      "name": "The Democractic Republic of Congo"
    },
    {
      "code": "+682",
      "iso": "ck",
      "name": "Cook Islands"
    },
    {
      "code": "+506",
      "iso": "cr",
      "name": "Costa Rica"
    },
    {
      "code": "+385",
      "iso": "hr",
      "name": "Croatia"
    },
    {
      "code": "+53",
      "iso": "cu",
      "name": "Cuba"
    },
    {
      "code": "+599",
      "iso": "cw",
      "name": "Curacao"
    },
    {
      "code": "+537",
      "iso": "cy",
      "name": "Cyprus"
    },
    {
      "code": "+420",
      "iso": "cz",
      "name": "Czech Republic"
    },
    {
      "code": "+45",
      "iso": "dk",
      "name": "Denmark"
    },
    {
      "code": "+246",
      "iso": "io",
      "name": "Diego Garcia"
    },
    {
      "code": "+253",
      "iso": "dj",
      "name": "Djibouti"
    },
    {
      "code": "+1 767",
      "iso": "dm",
      "name": "Dominica"
    },
    {
      "code": "+1 809",
      "iso": "do",
      "name": "Dominican Republic"
    },
    {
      "code": "+670",
      "iso": "tl",
      "name": "East Timor"
    },
    {
      "code": "+56",
      "iso": "",
      "name": "Easter Island"
    },
    {
      "code": "+593",
      "iso": "ec",
      "name": "Ecuador"
    },
    {
      "code": "+20",
      "iso": "eg",
      "name": "Egypt"
    },
    {
      "code": "+503",
      "iso": "sv",
      "name": "El Salvador"
    },
    {
      "code": "+240",
      "iso": "gq",
      "name": "Equatorial Guinea"
    },
    {
      "code": "+291",
      "iso": "er",
      "name": "Eritrea"
    },
    {
      "code": "+372",
      "iso": "ee",
      "name": "Estonia"
    },
    {
      "code": "+251",
      "iso": "et",
      "name": "Ethiopia"
    },
    {
      "code": "+500",
      "iso": "fk",
      "name": "Falkland Islands"
    },
    {
      "code": "+298",
      "iso": "fo",
      "name": "Faroe Islands"
    },
    {
      "code": "+679",
      "iso": "fj",
      "name": "Fiji"
    },
    {
      "code": "+358",
      "iso": "fi",
      "name": "Finland"
    },
    {
      "code": "+33",
      "iso": "fr",
      "name": "France"
    },
    {
      "code": "+596",
      "iso": "",
      "name": "French Antilles"
    },
    {
      "code": "+594",
      "iso": "",
      "name": "French Guiana"
    },
    {
      "code": "+689",
      "iso": "pf",
      "name": "French Polynesia"
    },
    {
      "code": "+241",
      "iso": "ga",
      "name": "Gabon"
    },
    {
      "code": "+220",
      "iso": "gm",
      "name": "Gambia"
    },
    {
      "code": "+995",
      "iso": "ge",
      "name": "Georgia"
    },
    {
      "code": "+49",
      "iso": "de",
      "name": "Germany"
    },
    {
      "code": "+233",
      "iso": "gh",
      "name": "Ghana"
    },
    {
      "code": "+350",
      "iso": "gi",
      "name": "Gibraltar"
    },
    {
      "code": "+30",
      "iso": "gr",
      "name": "Greece"
    },
    {
      "code": "+299",
      "iso": "gl",
      "name": "Greenland"
    },
    {
      "code": "+1 473",
      "iso": "gd",
      "name": "Grenada"
    },
    {
      "code": "+590",
      "iso": "gp",
      "name": "Guadeloupe"
    },
    {
      "code": "+1 671",
      "iso": "gu",
      "name": "Guam"
    },
    {
      "code": "+502",
      "iso": "gt",
      "name": "Guatemala"
    },
    {
      "code": "+224",
      "iso": "gn",
      "name": "Guinea"
    },
    {
      "code": "+245",
      "iso": "gw",
      "name": "Guinea-Bissau"
    },
    {
      "code": "+595",
      "iso": "gy",
      "name": "Guyana"
    },
    {
      "code": "+509",
      "iso": "ht",
      "name": "Haiti"
    },
    {
      "code": "+504",
      "iso": "hn",
      "name": "Honduras"
    },
    {
      "code": "+852",
      "iso": "hk",
      "name": "Hong Kong"
    },
    {
      "code": "+36",
      "iso": "hu",
      "name": "Hungary"
    },
    {
      "code": "+354",
      "iso": "is",
      "name": "Iceland"
    },
    {
      "code": "+91",
      "iso": "in",
      "name": "India"
    },
    {
      "code": "+62",
      "iso": "id",
      "name": "Indonesia"
    },
    {
      "code": "+98",
      "iso": "ir",
      "name": "Iran"
    },
    {
      "code": "+964",
      "iso": "iq",
      "name": "Iraq"
    },
    {
      "code": "+353",
      "iso": "ie",
      "name": "Ireland"
    },
    {
      "code": "+972",
      "iso": "il",
      "name": "Israel"
    },
    {
      "code": "+39",
      "iso": "it",
      "name": "Italy"
    },
    {
      "code": "+225",
      "iso": "ci",
      "name": "Ivory Coast"
    },
    {
      "code": "+1 876",
      "iso": "jm",
      "name": "Jamaica"
    },
    {
      "code": "+81",
      "iso": "jp",
      "name": "Japan"
    },
    {
      "code": "+962",
      "iso": "jo",
      "name": "Jordan"
    },
    {
      "code": "+7 7",
      "iso": "kz",
      "name": "Kazakhstan"
    },
    {
      "code": "+254",
      "iso": "ke",
      "name": "Kenya"
    },
    {
      "code": "+686",
      "iso": "ki",
      "name": "Kiribati"
    },
    {
      "code": "+965",
      "iso": "kw",
      "name": "Kuwait"
    },
    {
      "code": "+996",
      "iso": "kg",
      "name": "Kyrgyzstan"
    },
    {
      "code": "+856",
      "iso": "la",
      "name": "Laos"
    },
    {
      "code": "+371",
      "iso": "lv",
      "name": "Latvia"
    },
    {
      "code": "+961",
      "iso": "lb",
      "name": "Lebanon"
    },
    {
      "code": "+266",
      "iso": "ls",
      "name": "Lesotho"
    },
    {
      "code": "+231",
      "iso": "lr",
      "name": "Liberia"
    },
    {
      "code": "+218",
      "iso": "ly",
      "name": "Libya"
    },
    {
      "code": "+423",
      "iso": "li",
      "name": "Liechtenstein"
    },
    {
      "code": "+370",
      "iso": "lt",
      "name": "Lithuania"
    },
    {
      "code": "+352",
      "iso": "lu",
      "name": "Luxembourg"
    },
    {
      "code": "+853",
      "iso": "mo",
      "name": "Macau"
    },
    {
      "code": "+389",
      "iso": "mk",
      "name": "Macedonia"
    },
    {
      "code": "+261",
      "iso": "mg",
      "name": "Madagascar"
    },
    {
      "code": "+265",
      "iso": "mw",
      "name": "Malawi"
    },
    {
      "code": "+60",
      "iso": "my",
      "name": "Malaysia"
    },
    {
      "code": "+960",
      "iso": "mv",
      "name": "Maldives"
    },
    {
      "code": "+223",
      "iso": "ml",
      "name": "Mali"
    },
    {
      "code": "+356",
      "iso": "mt",
      "name": "Malta"
    },
    {
      "code": "+692",
      "iso": "mh",
      "name": "Marshall Islands"
    },
    {
      "code": "+596",
      "iso": "mq",
      "name": "Martinique"
    },
    {
      "code": "+222",
      "iso": "mr",
      "name": "Mauritania"
    },
    {
      "code": "+230",
      "iso": "mu",
      "name": "Mauritius"
    },
    {
      "code": "+262",
      "iso": "yt",
      "name": "Mayotte"
    },
    {
      "code": "+52",
      "iso": "mx",
      "name": "Mexico"
    },
    {
      "code": "+691",
      "iso": "fm",
      "name": "Micronesia"
    },
    {
      "code": "+1 808",
      "iso": "us",
      "name": "Midway Island"
    },
    {
      "code": "+373",
      "iso": "md",
      "name": "Moldova"
    },
    {
      "code": "+377",
      "iso": "mc",
      "name": "Monaco"
    },
    {
      "code": "+976",
      "iso": "mn",
      "name": "Mongolia"
    },
    {
      "code": "+382",
      "iso": "me",
      "name": "Montenegro"
    },
    {
      "code": "+1664",
      "iso": "ms",
      "name": "Montserrat"
    },
    {
      "code": "+212",
      "iso": "ma",
      "name": "Morocco"
    },
    {
      "code": "+95",
      "iso": "mm",
      "name": "Myanmar"
    },
    {
      "code": "+264",
      "iso": "na",
      "name": "Namibia"
    },
    {
      "code": "+674",
      "iso": "nr",
      "name": "Nauru"
    },
    {
      "code": "+977",
      "iso": "np",
      "name": "Nepal"
    },
    {
      "code": "+31",
      "iso": "nl",
      "name": "Netherlands"
    },
    {
      "code": "+599",
      "iso": "an",
      "name": "Netherlands Antilles"
    },
    {
      "code": "+1 869",
      "iso": "",
      "name": "Nevis"
    },
    {
      "code": "+687",
      "iso": "nc",
      "name": "New Caledonia"
    },
    {
      "code": "+64",
      "iso": "nz",
      "name": "New Zealand"
    },
    {
      "code": "+505",
      "iso": "ni",
      "name": "Nicaragua"
    },
    {
      "code": "+227",
      "iso": "ne",
      "name": "Niger"
    },
    {
      "code": "+234",
      "iso": "ng",
      "name": "Nigeria"
    },
    {
      "code": "+683",
      "iso": "nu",
      "name": "Niue"
    },
    {
      "code": "+672",
      "iso": "nf",
      "name": "Norfolk Island"
    },
    {
      "code": "+850",
      "iso": "kp",
      "name": "North Korea"
    },
    {
      "code": "+1 670",
      "iso": "mp",
      "name": "Northern Mariana Islands"
    },
    {
      "code": "+47",
      "iso": "no",
      "name": "Norway"
    },
    {
      "code": "+968",
      "iso": "om",
      "name": "Oman"
    },
    {
      "code": "+92",
      "iso": "pk",
      "name": "Pakistan"
    },
    {
      "code": "+680",
      "iso": "pw",
      "name": "Palau"
    },
    {
      "code": "+970",
      "iso": "ps",
      "name": "Palestinian Territory"
    },
    {
      "code": "+507",
      "iso": "pa",
      "name": "Panama"
    },
    {
      "code": "+675",
      "iso": "pg",
      "name": "Papua New Guinea"
    },
    {
      "code": "+595",
      "iso": "pg",
      "name": "Paraguay"
    },
    {
      "code": "+51",
      "iso": "pe",
      "name": "Peru"
    },
    {
      "code": "+63",
      "iso": "ph",
      "name": "Philippines"
    },
    {
      "code": "+48",
      "iso": "pl",
      "name": "Poland"
    },
    {
      "code": "+351",
      "iso": "pt",
      "name": "Portugal"
    },
    {
      "code": "+1 787",
      "iso": "pr",
      "name": "Puerto Rico"
    },
    {
      "code": "+974",
      "iso": "qa",
      "name": "Qatar"
    },
    {
      "code": "+262",
      "iso": "re",
      "name": "Reunion"
    },
    {
      "code": "+40",
      "iso": "ro",
      "name": "Romania"
    },
    {
      "code": "+7",
      "iso": "ru",
      "name": "Russia"
    },
    {
      "code": "+250",
      "iso": "rw",
      "name": "Rwanda"
    },
    {
      "code": "+685",
      "iso": "ws",
      "name": "Samoa"
    },
    {
      "code": "+378",
      "iso": "sm",
      "name": "San Marino"
    },
    {
      "code": "+966",
      "iso": "sa",
      "name": "Saudi Arabia"
    },
    {
      "code": "+221",
      "iso": "sn",
      "name": "Senegal"
    },
    {
      "code": "+381",
      "iso": "rs",
      "name": "Serbia"
    },
    {
      "code": "+248",
      "iso": "sc",
      "name": "Seychelles"
    },
    {
      "code": "+232",
      "iso": "sl",
      "name": "Sierra Leone"
    },
    {
      "code": "+65",
      "iso": "sg",
      "name": "Singapore"
    },
    {
      "code": "+421",
      "iso": "sk",
      "name": "Slovakia"
    },
    {
      "code": "+386",
      "iso": "si",
      "name": "Slovenia"
    },
    {
      "code": "+677",
      "iso": "sb",
      "name": "Solomon Islands"
    },
    {
      "code": "+27",
      "iso": "za",
      "name": "South Africa"
    },
    {
      "code": "+500",
      "iso": "gs",
      "name": "South Georgia and the South Sandwich Islands"
    },
    {
      "code": "+82",
      "iso": "kr",
      "name": "South Korea"
    },
    {
      "code": "+34",
      "iso": "es",
      "name": "Spain"
    },
    {
      "code": "+94",
      "iso": "lk",
      "name": "Sri Lanka"
    },
    {
      "code": "+249",
      "iso": "sd",
      "name": "Sudan"
    },
    {
      "code": "+597",
      "iso": "sr",
      "name": "Suriname"
    },
    {
      "code": "+268",
      "iso": "",
      "name": "Swaziland"
    },
    {
      "code": "+46",
      "iso": "se",
      "name": "Sweden"
    },
    {
      "code": "+41",
      "iso": "ch",
      "name": "Switzerland"
    },
    {
      "code": "+963",
      "iso": "sy",
      "name": "Syria"
    },
    {
      "code": "+886",
      "iso": "tw",
      "name": "Taiwan"
    },
    {
      "code": "+992",
      "iso": "tj",
      "name": "Tajikistan"
    },
    {
      "code": "+255",
      "iso": "tz",
      "name": "Tanzania"
    },
    {
      "code": "+66",
      "iso": "th",
      "name": "Thailand"
    },
    {
      "code": "+670",
      "iso": "tl",
      "name": "Timor Leste"
    },
    {
      "code": "+228",
      "iso": "tg",
      "name": "Togo"
    },
    {
      "code": "+690",
      "iso": "tk",
      "name": "Tokelau"
    },
    {
      "code": "+676",
      "iso": "to",
      "name": "Tonga"
    },
    {
      "code": "+1 868",
      "iso": "tt",
      "name": "Trinidad and Tobago"
    },
    {
      "code": "+216",
      "iso": "tn",
      "name": "Tunisia"
    },
    {
      "code": "+90",
      "iso": "tr",
      "name": "Turkey"
    },
    {
      "code": "+993",
      "iso": "tm",
      "name": "Turkmenistan"
    },
    {
      "code": "+1 649",
      "iso": "tc",
      "name": "Turks and Caicos Islands"
    },
    {
      "code": "+688",
      "iso": "tv",
      "name": "Tuvalu"
    },
    {
      "code": "+1 340",
      "iso": "",
      "name": "U.S. Virgin Islands"
    },
    {
      "code": "+256",
      "iso": "ug",
      "name": "Uganda"
    },
    {
      "code": "+380",
      "iso": "ua",
      "name": "Ukraine"
    },
    {
      "code": "+971",
      "iso": "ae",
      "name": "United Arab Emirates"
    },
    {
      "code": "+44",
      "iso": "gb",
      "name": "United Kingdom"
    },
    {
      "code": "+1",
      "iso": "us",
      "name": "United States"
    },
    {
      "code": "+598",
      "iso": "uy",
      "name": "Uruguay"
    },
    {
      "code": "+998",
      "iso": "uz",
      "name": "Uzbekistan"
    },
    {
      "code": "+678",
      "iso": "vu",
      "name": "Vanuatu"
    },
    {
      "code": "+58",
      "iso": "ve",
      "name": "Venezuela"
    },
    {
      "code": "+84",
      "iso": "vn",
      "name": "Vietnam"
    },
    {
      "code": "+1 808",
      "iso": "",
      "name": "Wake Island"
    },
    {
      "code": "+681",
      "iso": "wf",
      "name": "Wallis and Futuna"
    },
    {
      "code": "+967",
      "iso": "ye",
      "name": "Yemen"
    },
    {
      "code": "+260",
      "iso": "zm",
      "name": "Zambia"
    },
    {
      "code": "+255",
      "name": "Zanzibar"
    },
    {
      "code": "+263",
      "iso": "zw",
      "name": "Zimbabwe"
    }
]

def get_flag_path(path_str):
    if path_str:
      path = cur_path.joinpath("icons").joinpath(path_str + ".svg")

      if path.exists():
        return str(path)
    return fallback_icon
