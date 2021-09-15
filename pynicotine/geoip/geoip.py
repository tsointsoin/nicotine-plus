# COPYRIGHT (C) 2020-2021 Nicotine+ Team
# COPYRIGHT (C) 2009 Quinox <quinox@users.sf.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class GeoIP:
    """ Country-related class """

    COUNTRY_LIST = {
        'ad': _('Andorra'),
        'ae': _('United Arab Emirates'),
        'af': _('Afghanistan'),
        'ag': _('Antigua & Barbuda'),
        'ai': _('Anguilla'),
        'al': _('Albania'),
        'am': _('Armenia'),
        'ao': _('Angola'),
        'aq': _('Antarctica'),
        'ar': _('Argentina'),
        'as': _('American Samoa'),
        'at': _('Austria'),
        'au': _('Australia'),
        'aw': _('Aruba'),
        'ax': _('Åland Islands'),
        'az': _('Azerbaijan'),
        'ba': _('Bosnia & Herzegovina'),
        'bb': _('Barbados'),
        'bd': _('Bangladesh'),
        'be': _('Belgium'),
        'bf': _('Burkina Faso'),
        'bg': _('Bulgaria'),
        'bh': _('Bahrain'),
        'bi': _('Burundi'),
        'bj': _('Benin'),
        'bl': _('Saint Barthelemy'),
        'bm': _('Bermuda'),
        'bn': _('Brunei Darussalam'),
        'bo': _('Bolivia'),
        'bq': _('Bonaire), Sint Eustatius and Saba'),
        'br': _('Brazil'),
        'bs': _('Bahamas'),
        'bt': _('Bhutan'),
        'bv': _('Bouvet Island'),
        'bw': _('Botswana'),
        'by': _('Belarus'),
        'bz': _('Belize'),
        'ca': _('Canada'),
        'cc': _('Cocos (Keeling) Islands'),
        'cd': _('Democratic Republic of Congo'),
        'cf': _('Central African Republic'),
        'cg': _('Congo'),
        'ch': _('Switzerland'),
        'ci': _('Ivory Coast'),
        'ck': _('Cook Islands'),
        'cl': _('Chile'),
        'cm': _('Cameroon'),
        'cn': _('China'),
        'co': _('Colombia'),
        'cr': _('Costa Rica'),
        'cu': _('Cuba'),
        'cv': _('Cabo Verde'),
        'cw': _('Curaçao'),
        'cx': _('Christmas Island'),
        'cy': _('Cyprus'),
        'cz': _('Czech Republic'),
        'de': _('Germany'),
        'dj': _('Djibouti'),
        'dk': _('Denmark'),
        'dm': _('Dominica'),
        'do': _('Dominican Republic'),
        'dz': _('Algeria'),
        'ec': _('Ecuador'),
        'ee': _('Estonia'),
        'eg': _('Egypt'),
        'eh': _('Western Sahara'),
        'er': _('Eritrea'),
        'es': _('Spain'),
        'et': _('Ethiopia'),
        'eu': _('Europe'),
        'fi': _('Finland'),
        'fj': _('Fiji'),
        'fk': _('Falkland Islands (Malvinas)'),
        'fm': _('Micronesia'),
        'fo': _('Faroe Islands'),
        'fr': _('France'),
        'ga': _('Gabon'),
        'gb': _('Great Britain'),
        'gd': _('Grenada'),
        'ge': _('Georgia'),
        'gf': _('French Guiana'),
        'gg': _('Guernsey'),
        'gh': _('Ghana'),
        'gi': _('Gibraltar'),
        'gl': _('Greenland'),
        'gm': _('Gambia'),
        'gn': _('Guinea'),
        'gp': _('Guadeloupe'),
        'gq': _('Equatorial Guinea'),
        'gr': _('Greece'),
        'gs': _('South Georgia & South Sandwich Islands'),
        'gt': _('Guatemala'),
        'gu': _('Guam'),
        'gw': _('Guinea-Bissau'),
        'gy': _('Guyana'),
        'hk': _('Hong Kong'),
        'hm': _('Heard & McDonald Islands'),
        'hn': _('Honduras'),
        'hr': _('Croatia'),
        'ht': _('Haiti'),
        'hu': _('Hungary'),
        'id': _('Indonesia'),
        'ie': _('Ireland'),
        'il': _('Israel'),
        'im': _('Isle of Man'),
        'in': _('India'),
        'io': _('British Indian Ocean Territory'),
        'iq': _('Iraq'),
        'ir': _('Iran'),
        'is': _('Iceland'),
        'it': _('Italy'),
        'je': _('Jersey'),
        'jm': _('Jamaica'),
        'jo': _('Jordan'),
        'jp': _('Japan'),
        'ke': _('Kenya'),
        'kg': _('Kyrgyzstan'),
        'kh': _('Cambodia'),
        'ki': _('Kiribati'),
        'km': _('Comoros'),
        'kn': _('Saint Kitts & Nevis'),
        'kp': _('North Korea'),
        'kr': _('South Korea'),
        'kw': _('Kuwait'),
        'ky': _('Cayman Islands'),
        'kz': _('Kazakhstan'),
        'la': _('Laos'),
        'lb': _('Lebanon'),
        'lc': _('Saint Lucia'),
        'li': _('Liechtenstein'),
        'lk': _('Sri Lanka'),
        'lr': _('Liberia'),
        'ls': _('Lesotho'),
        'lt': _('Lithuania'),
        'lu': _('Luxembourg'),
        'lv': _('Latvia'),
        'ly': _('Libya'),
        'ma': _('Morocco'),
        'mc': _('Monaco'),
        'md': _('Moldova'),
        'me': _('Montenegro'),
        'mf': _('Saint Martin'),
        'mg': _('Madagascar'),
        'mh': _('Marshall Islands'),
        'mk': _('North Macedonia'),
        'ml': _('Mali'),
        'mm': _('Myanmar'),
        'mn': _('Mongolia'),
        'mo': _('Macau'),
        'mp': _('Northern Mariana Islands'),
        'mq': _('Martinique'),
        'mr': _('Mauritania'),
        'ms': _('Montserrat'),
        'mt': _('Malta'),
        'mu': _('Mauritius'),
        'mv': _('Maldives'),
        'mw': _('Malawi'),
        'mx': _('Mexico'),
        'my': _('Malaysia'),
        'mz': _('Mozambique'),
        'na': _('Namibia'),
        'nc': _('New Caledonia'),
        'ne': _('Niger'),
        'nf': _('Norfolk Island'),
        'ng': _('Nigeria'),
        'ni': _('Nicaragua'),
        'nl': _('Netherlands'),
        'no': _('Norway'),
        'np': _('Nepal'),
        'nr': _('Nauru'),
        'nu': _('Niue'),
        'nz': _('New Zealand'),
        'om': _('Oman'),
        'pa': _('Panama'),
        'pe': _('Peru'),
        'pf': _('French Polynesia'),
        'pg': _('Papua New Guinea'),
        'ph': _('Philippines'),
        'pk': _('Pakistan'),
        'pl': _('Poland'),
        'pm': _('Saint Pierre & Miquelon'),
        'pn': _('Pitcairn'),
        'pr': _('Puerto Rico'),
        'ps': _('State of Palestine'),
        'pt': _('Portugal'),
        'pw': _('Palau'),
        'py': _('Paraguay'),
        'qa': _('Qatar'),
        're': _('Reunion'),
        'ro': _('Romania'),
        'rs': _('Serbia'),
        'ru': _('Russia'),
        'rw': _('Rwanda'),
        'sa': _('Saudi Arabia'),
        'sb': _('Solomon Islands'),
        'sc': _('Seychelles'),
        'sd': _('Sudan'),
        'se': _('Sweden'),
        'sg': _('Singapore'),
        'sh': _('Saint Helena'),
        'si': _('Slovenia'),
        'sj': _('Svalbard & Jan Mayen Islands'),
        'sk': _('Slovak Republic'),
        'sl': _('Sierra Leone'),
        'sm': _('San Marino'),
        'sn': _('Senegal'),
        'so': _('Somalia'),
        'sr': _('Suriname'),
        'ss': _('South Sudan'),
        'st': _('Sao Tome & Principe'),
        'sv': _('El Salvador'),
        'sx': _('Sint Maarten'),
        'sy': _('Syria'),
        'sz': _('Eswatini'),
        'tc': _('Turks & Caicos Islands'),
        'td': _('Chad'),
        'tf': _('French Southern Territories'),
        'tg': _('Togo'),
        'th': _('Thailand'),
        'tj': _('Tajikistan'),
        'tk': _('Tokelau'),
        'tl': _('Timor-Leste'),
        'tm': _('Turkmenistan'),
        'tn': _('Tunisia'),
        'to': _('Tonga'),
        'tr': _('Turkey'),
        'tt': _('Trinidad & Tobago'),
        'tv': _('Tuvalu'),
        'tw': _('Taiwan'),
        'tz': _('Tanzania'),
        'ua': _('Ukraine'),
        'ug': _('Uganda'),
        'um': _('U.S. Minor Outlying Islands'),
        'us': _('United States'),
        'uy': _('Uruguay'),
        'uz': _('Uzbekistan'),
        'va': _('Holy See (Vatican City State)'),
        'vc': _('Saint Vincent & The Grenadines'),
        've': _('Venezuela'),
        'vg': _('British Virgin Islands'),
        'vi': _('U.S. Virgin Islands'),
        'vn': _('Viet Nam'),
        'vu': _('Vanuatu'),
        'wf': _('Wallis & Futuna'),
        'ws': _('Samoa'),
        'xk': _('Kosovo'),
        'ye': _('Yemen'),
        'yt': _('Mayotte'),
        'za': _('South Africa'),
        'zm': _('Zambia'),
        'zw': _('Zimbabwe')
    }

    def __init__(self, filename):

        from pynicotine.geoip.ip2location import IP2Location
        self.ip2location = IP2Location(filename)

    @classmethod
    def country_code_to_name(cls, country_code):

        try:
            return cls.COUNTRY_LIST[country_code.lower()]

        except KeyError:
            return country_code

    def get_country_code(self, addr):

        country_code = self.ip2location.get_country_code(addr)

        if country_code == "-":
            country_code = ""

        return country_code
