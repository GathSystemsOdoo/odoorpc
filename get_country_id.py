#!/usr/bin/python
# -*- coding: UTF-8 -*-
##############################################################################
#
#    Python Script for Odoo, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


def cleanup(to_clean, searchfield):
    cleanstr = to_clean
    cleanstr = cleanstr.replace("'", "")
    cleanstr = cleanstr.replace("{", "")
    cleanstr = cleanstr.replace('"', "")
    cleanstr = cleanstr.replace(",", "")
    cleanstr = cleanstr.replace(":", "")
    cleanstr = cleanstr.replace(searchfield, "")
    cleanstr = cleanstr.rstrip("\n")
    cleanstr = cleanstr.rstrip()
    cleanstr = cleanstr.lstrip()
    return cleanstr


def get_odoo_country_id(_country):
    _country = _country.upper()
    _country = unicode(_country, "utf-8")
    _odoo_country_id = 0
    if _country == u'ANDORRA, PRINCIPALITY OF' or _country == u'FÜRSTENTUM ANDORRA' or _country == u'AD':
        _odoo_country_id = 1
    if _country == u'UNITED ARAB EMIRATES' or _country == u'VEREINIGTE ARABISCHE EMIRATE' or _country == u'AE':
        _odoo_country_id = 2
    if _country == u'AFGHANISTAN, ISLAMIC STATE OF' or _country == u'AFGHANISTAN, ISLAMISCHER STAAT VON' or _country == u'AF':
        _odoo_country_id = 3
    if _country == u'ANTIGUA AND BARBUDA' or _country == u'ANTIGUA UND BARBUDA' or _country == u'AG':
        _odoo_country_id = 4
    if _country == u'ANGUILLA' or _country == u'ANGUILLA' or _country == u'AI':
        _odoo_country_id = 5
    if _country == u'ALBANIA' or _country == u'ALBANIEN' or _country == u'AL':
        _odoo_country_id = 6
    if _country == u'ARMENIA' or _country == u'ARMENIEN' or _country == u'AM':
        _odoo_country_id = 7
    if _country == u'NETHERLANDS ANTILLES' or _country == u'NIEDERLÄNDISCHE ANTILLEN' or _country == u'AN':
        _odoo_country_id = 8
    if _country == u'ANGOLA' or _country == u'ANGOLA' or _country == u'AO':
        _odoo_country_id = 9
    if _country == u'ANTARCTICA' or _country == u'ANTARKTIK' or _country == u'AQ':
        _odoo_country_id = 10
    if _country == u'ARGENTINA' or _country == u'ARGENTINIEN' or _country == u'AR':
        _odoo_country_id = 11
    if _country == u'AMERICAN SAMOA' or _country == u'AMERIKANISCHEN SAMOA-INSELN' or _country == u'AS':
        _odoo_country_id = 12
    if _country == u'AUSTRIA' or _country == u'ÖSTERREICH' or _country == u'AT':
        _odoo_country_id = 13
    if _country == u'AUSTRALIA' or _country == u'AUSTRALIEN' or _country == u'AU':
        _odoo_country_id = 14
    if _country == u'ARUBA' or _country == u'ARUBA' or _country == u'AW':
        _odoo_country_id = 15
    if _country == u'ÅLAND ISLANDS' or _country == u'ALAND ISLANDS' or _country == u'AX':
        _odoo_country_id = 16
    if _country == u'AZERBAIJAN' or _country == u'ASERBAIDSCHAN' or _country == u'AZ':
        _odoo_country_id = 17
    if _country == u'BOSNIA-HERZEGOVINA' or _country == u'BOSNIEN-HERZEGOWINA' or _country == u'BA':
        _odoo_country_id = 18
    if _country == u'BARBADOS' or _country == u'BARBADOS' or _country == u'BB':
        _odoo_country_id = 19
    if _country == u'BANGLADESH' or _country == u'BANGLADESCH' or _country == u'BD':
        _odoo_country_id = 20
    if _country == u'BELGIUM' or _country == u'BELGIEN' or _country == u'BE':
        _odoo_country_id = 21
    if _country == u'BURKINA FASO' or _country == u'BURKINA FASO' or _country == u'BF':
        _odoo_country_id = 22
    if _country == u'BULGARIA' or _country == u'BULGARIEN' or _country == u'BG':
        _odoo_country_id = 23
    if _country == u'BAHRAIN' or _country == u'BAHRAIN' or _country == u'BH':
        _odoo_country_id = 24
    if _country == u'BURUNDI' or _country == u'BURUNDI' or _country == u'BI':
        _odoo_country_id = 25
    if _country == u'BENIN' or _country == u'BENIN' or _country == u'BJ':
        _odoo_country_id = 26
    if _country == u'SAINT BARTHÉLÉMY' or _country == u'SAINT BARTHÉLÉMY' or _country == u'BL':
        _odoo_country_id = 27
    if _country == u'BERMUDA' or _country == u'BERMUDA' or _country == u'BM':
        _odoo_country_id = 28
    if _country == u'BRUNEI DARUSSALAM' or _country == u'BRUNEI DARUSSALAM' or _country == u'BN':
        _odoo_country_id = 29
    if _country == u'BOLIVIA' or _country == u'BOLIVIEN' or _country == u'BO':
        _odoo_country_id = 30
    if _country == u'BONAIRE, SINT EUSTATIUS AND SABA' or _country == u'BONAIRE, SINT EUSTATIUS UND SABA' or _country == u'BQ':
        _odoo_country_id = 31
    if _country == u'BRAZIL' or _country == u'BRASILIEN' or _country == u'BR':
        _odoo_country_id = 32
    if _country == u'BAHAMAS' or _country == u'BAHAMAS' or _country == u'BS':
        _odoo_country_id = 33
    if _country == u'BHUTAN' or _country == u'BHUTAN' or _country == u'BT':
        _odoo_country_id = 34
    if _country == u'BOUVET ISLAND' or _country == u'BOUVET-INSEL' or _country == u'BV':
        _odoo_country_id = 35
    if _country == u'BOTSWANA' or _country == u'BOTSWANA' or _country == u'BW':
        _odoo_country_id = 36
    if _country == u'BELARUS' or _country == u'WEISSRUSSLAND' or _country == u'BY':
        _odoo_country_id = 37
    if _country == u'BELIZE' or _country == u'BELIZE' or _country == u'BZ':
        _odoo_country_id = 38
    if _country == u'CANADA' or _country == u'KANADA' or _country == u'CA':
        _odoo_country_id = 39
    if _country == u'COCOS (KEELING) ISLANDS' or _country == u'COCOS (KEELING) INSELN' or _country == u'CC':
        _odoo_country_id = 40
    if _country == u'CENTRAL AFRICAN REPUBLIC' or _country == u'ZENTRALAFRIKANISCHE REPUBLIK' or _country == u'CF':
        _odoo_country_id = 41
    if _country == u'CONGO, DEMOCRATIC REPUBLIC OF THE' or _country == u'KONGO, DEMOKRATISCHE REPUBLIK DER' or _country == u'CD':
        _odoo_country_id = 42
    if _country == u'CONGO' or _country == u'KONGO' or _country == u'CG':
        _odoo_country_id = 43
    if _country == u'SWITZERLAND' or _country == u'SCHWEIZ' or _country == u'CH':
        _odoo_country_id = 44
    if _country == u'IVORY COAST (COTE D IVOIRE)' or _country == u'IVORY-KÜSTE (COTE D IVOIRE)' or _country == u'CI':
        _odoo_country_id = 45
    if _country == u'COOK ISLANDS' or _country == u'COOKINSELN' or _country == u'CK':
        _odoo_country_id = 46
    if _country == u'CHILE' or _country == u'CHILE' or _country == u'CL':
        _odoo_country_id = 47
    if _country == u'CAMEROON' or _country == u'KAMERUNE' or _country == u'CM':
        _odoo_country_id = 48
    if _country == u'CHINA' or _country == u'CHINA' or _country == u'CN':
        _odoo_country_id = 49
    if _country == u'COLOMBIA' or _country == u'KOLUMBIEN' or _country == u'CO':
        _odoo_country_id = 50
    if _country == u'COSTA RICA' or _country == u'COSTA RICA' or _country == u'CR':
        _odoo_country_id = 51
    if _country == u'CUBA' or _country == u'KUBA' or _country == u'CU':
        _odoo_country_id = 52
    if _country == u'CAPE VERDE' or _country == u'KAP VERDE' or _country == u'CV':
        _odoo_country_id = 53
    if _country == u'CURAÇAO' or _country == u'CURACAO' or _country == u'CW':
        _odoo_country_id = 54
    if _country == u'CHRISTMAS ISLAND' or _country == u'WEIHNACHTSINSEL' or _country == u'CX':
        _odoo_country_id = 55
    if _country == u'CYPRUS' or _country == u'ZYPERN' or _country == u'CY':
        _odoo_country_id = 56
    if _country == u'CZECH REPUBLIC' or _country == u'TSCHECHIEN' or _country == u'CZ':
        _odoo_country_id = 57
    if _country == u'GERMANY' or _country == u'DEUTSCHLAND' or _country == u'DE':
        _odoo_country_id = 58
    if _country == u'DJIBOUTI' or _country == u'DJIBOUTI' or _country == u'DJ':
        _odoo_country_id = 59
    if _country == u'DENMARK' or _country == u'DÄNEMARK' or _country == u'DK':
        _odoo_country_id = 60
    if _country == u'DOMINICA' or _country == u'DOMINIKA' or _country == u'DM':
        _odoo_country_id = 61
    if _country == u'DOMINICAN REPUBLIC' or _country == u'DOMINIKANISCHE REPUBLIK' or _country == u'DO':
        _odoo_country_id = 62
    if _country == u'ALGERIA' or _country == u'ALGERIEN' or _country == u'DZ':
        _odoo_country_id = 63
    if _country == u'ECUADOR' or _country == u'ECUADOR' or _country == u'EC':
        _odoo_country_id = 64
    if _country == u'ESTONIA' or _country == u'ESTLAND' or _country == u'EE':
        _odoo_country_id = 65
    if _country == u'EGYPT' or _country == u'ÄGYPTEN' or _country == u'EG':
        _odoo_country_id = 66
    if _country == u'WESTERN SAHARA' or _country == u'WESTSAHARA' or _country == u'EH':
        _odoo_country_id = 67
    if _country == u'ERITREA' or _country == u'ERITREA' or _country == u'ER':
        _odoo_country_id = 68
    if _country == u'SPAIN' or _country == u'SPANIEN' or _country == u'ES':
        _odoo_country_id = 69
    if _country == u'ETHIOPIA' or _country == u'ÄTHIOPIEN' or _country == u'ET':
        _odoo_country_id = 70
    if _country == u'FINLAND' or _country == u'FINNLAND' or _country == u'FI':
        _odoo_country_id = 71
    if _country == u'FIJI' or _country == u'FIJI' or _country == u'FJ':
        _odoo_country_id = 72
    if _country == u'FALKLAND ISLANDS' or _country == u'FALKLAND INSELN' or _country == u'FK':
        _odoo_country_id = 73
    if _country == u'MICRONESIA' or _country == u'MIKRONESIEN' or _country == u'FM':
        _odoo_country_id = 74
    if _country == u'FAROE ISLANDS' or _country == u'FÄRÖER INSELN' or _country == u'FO':
        _odoo_country_id = 75
    if _country == u'FRANCE' or _country == u'FRANKREICH' or _country == u'FR':
        _odoo_country_id = 76
    if _country == u'GABON' or _country == u'GABON' or _country == u'GA':
        _odoo_country_id = 77
    if _country == u'GRENADA' or _country == u'GRENADA' or _country == u'GD':
        _odoo_country_id = 78
    if _country == u'GEORGIA' or _country == u'GEORGIA' or _country == u'GE':
        _odoo_country_id = 79
    if _country == u'FRENCH GUYANA' or _country == u'FRANZÖSISCHE GUYANA' or _country == u'GF':
        _odoo_country_id = 80
    if _country == u'GHANA' or _country == u'GHANA' or _country == u'GH':
        _odoo_country_id = 81
    if _country == u'GIBRALTAR' or _country == u'GIBRALTAR' or _country == u'GI':
        _odoo_country_id = 82
    if _country == u'GUERNSEY' or _country == u'GUERNSEY' or _country == u'GG':
        _odoo_country_id = 83
    if _country == u'GREENLAND' or _country == u'GRÖNLAND' or _country == u'GL':
        _odoo_country_id = 84
    if _country == u'GAMBIA' or _country == u'GAMBIA' or _country == u'GM':
        _odoo_country_id = 85
    if _country == u'GUINEA' or _country == u'GUINEA' or _country == u'GN':
        _odoo_country_id = 86
    if _country == u'GUADELOUPE (FRENCH)' or _country == u'GUADELOUPE (FRANZÖSISCH)' or _country == u'GP':
        _odoo_country_id = 87
    if _country == u'EQUATORIAL GUINEA' or _country == u'ÄQUATORIALGUINEA' or _country == u'GQ':
        _odoo_country_id = 88
    if _country == u'GREECE' or _country == u'GRIECHENLAND' or _country == u'GR':
        _odoo_country_id = 89
    if _country == u'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS' or _country == u'SÜDGEORGIEN UND DIE SÜDSANDWICH-INSELN' or _country == u'GS':
        _odoo_country_id = 90
    if _country == u'GUATEMALA' or _country == u'GUATEMALA' or _country == u'GT':
        _odoo_country_id = 91
    if _country == u'GUAM (USA)' or _country == u'GUAM (USA)' or _country == u'GU':
        _odoo_country_id = 92
    if _country == u'GUINEA BISSAU' or _country == u'GUINEA BISSAU' or _country == u'GW':
        _odoo_country_id = 93
    if _country == u'GUYANA' or _country == u'GUYANA' or _country == u'GY':
        _odoo_country_id = 94
    if _country == u'HONG KONG' or _country == u'HONGKONG' or _country == u'HK':
        _odoo_country_id = 95
    if _country == u'HEARD AND MCDONALD ISLANDS' or _country == u'HÖREN UND MCDONALD INSELN' or _country == u'HM':
        _odoo_country_id = 96
    if _country == u'HONDURAS' or _country == u'HONDURAS' or _country == u'HN':
        _odoo_country_id = 97
    if _country == u'CROATIA' or _country == u'KROATIEN' or _country == u'HR':
        _odoo_country_id = 98
    if _country == u'HAITI' or _country == u'HAITI' or _country == u'HT':
        _odoo_country_id = 99
    if _country == u'HUNGARY' or _country == u'UNGARN' or _country == u'HU':
        _odoo_country_id = 100
    if _country == u'INDONESIA' or _country == u'INDONESIEN' or _country == u'ID':
        _odoo_country_id = 101
    if _country == u'IRELAND' or _country == u'IRLAND' or _country == u'IE':
        _odoo_country_id = 102
    if _country == u'ISRAEL' or _country == u'ISRAEL' or _country == u'IL':
        _odoo_country_id = 103
    if _country == u'ISLE OF MAN' or _country == u'ISLE OF MAN' or _country == u'IM':
        _odoo_country_id = 104
    if _country == u'INDIA' or _country == u'INDIEN' or _country == u'IN':
        _odoo_country_id = 105
    if _country == u'BRITISH INDIAN OCEAN TERRITORY' or _country == u'BRITISCHES TERRITORIUM DES INDISCHEN OZEANS' or _country == u'IO':
        _odoo_country_id = 106
    if _country == u'IRAQ' or _country == u'IRAK' or _country == u'IQ':
        _odoo_country_id = 107
    if _country == u'IRAN' or _country == u'ICH RANNTE' or _country == u'IR':
        _odoo_country_id = 108
    if _country == u'ICELAND' or _country == u'ISLAND' or _country == u'IS':
        _odoo_country_id = 109
    if _country == u'ITALY' or _country == u'ITALIEN' or _country == u'IT':
        _odoo_country_id = 110
    if _country == u'JERSEY' or _country == u'JERSEY' or _country == u'JE':
        _odoo_country_id = 111
    if _country == u'JAMAICA' or _country == u'JAMAIKA' or _country == u'JM':
        _odoo_country_id = 112
    if _country == u'JORDAN' or _country == u'JORDANIEN' or _country == u'JO':
        _odoo_country_id = 113
    if _country == u'JAPAN' or _country == u'JAPAN' or _country == u'JP':
        _odoo_country_id = 114
    if _country == u'KENYA' or _country == u'KENIA' or _country == u'KE':
        _odoo_country_id = 115
    if _country == u'KYRGYZ REPUBLIC (KYRGYZSTAN)' or _country == u'KYRGYZ-REPUBLIK (KYRGYZSTAN)' or _country == u'KG':
        _odoo_country_id = 116
    if _country == u'CAMBODIA, KINGDOM OF' or _country == u'KAMBODSCHA, KÖNIGREICH' or _country == u'KH':
        _odoo_country_id = 117
    if _country == u'KIRIBATI' or _country == u'KIRIBATI' or _country == u'KI':
        _odoo_country_id = 118
    if _country == u'COMOROS' or _country == u'COMOROS' or _country == u'KM':
        _odoo_country_id = 119
    if _country == u'SAINT KITTS & NEVIS ANGUILLA' or _country == u'SAINT KITTS & NEVIS ANGUILLA' or _country == u'KN':
        _odoo_country_id = 120
    if _country == u'NORTH KOREA' or _country == u'NORD KOREA' or _country == u'KP':
        _odoo_country_id = 121
    if _country == u'SOUTH KOREA' or _country == u'SÜDKOREA' or _country == u'KR':
        _odoo_country_id = 122
    if _country == u'KUWAIT' or _country == u'KUWAIT' or _country == u'KW':
        _odoo_country_id = 123
    if _country == u'CAYMAN ISLANDS' or _country == u'CAYMAN INSELN' or _country == u'KY':
        _odoo_country_id = 124
    if _country == u'KAZAKHSTAN' or _country == u'Kasachstan' or _country == u'KZ':
        _odoo_country_id = 125
    if _country == u'LAOS' or _country == u'LAOS' or _country == u'LA':
        _odoo_country_id = 126
    if _country == u'LEBANON' or _country == u'LIBANON' or _country == u'LB':
        _odoo_country_id = 127
    if _country == u'SAINT LUCIA' or _country == u'SAINT LUCIA' or _country == u'LC':
        _odoo_country_id = 128
    if _country == u'LIECHTENSTEIN' or _country == u'LIECHTENSTEIN' or _country == u'LI':
        _odoo_country_id = 129
    if _country == u'SRI LANKA' or _country == u'SRI LANKA' or _country == u'LK':
        _odoo_country_id = 130
    if _country == u'LIBERIA' or _country == u'LIBERIA' or _country == u'LR':
        _odoo_country_id = 131
    if _country == u'LESOTHO' or _country == u'LESOTHO' or _country == u'LS':
        _odoo_country_id = 132
    if _country == u'LITHUANIA' or _country == u'LITAUEN' or _country == u'LT':
        _odoo_country_id = 133
    if _country == u'LUXEMBOURG' or _country == u'LUXEMBURG' or _country == u'LU':
        _odoo_country_id = 134
    if _country == u'LATVIA' or _country == u'LETTLAND' or _country == u'LV':
        _odoo_country_id = 135
    if _country == u'LIBYA' or _country == u'LIBYEN' or _country == u'LY':
        _odoo_country_id = 136
    if _country == u'MOROCCO' or _country == u'MAROKKO' or _country == u'MA':
        _odoo_country_id = 137
    if _country == u'MONACO' or _country == u'MONACO' or _country == u'MC':
        _odoo_country_id = 138
    if _country == u'MOLDAVIA' or _country == u'MOLDAU' or _country == u'MD':
        _odoo_country_id = 139
    if _country == u'MONTENEGRO' or _country == u'MONTENEGRO' or _country == u'ME':
        _odoo_country_id = 140
    if _country == u'SAINT MARTIN (FRENCH PART)' or _country == u'SAINT MARTIN (FRANZÖSISCHES TEIL)' or _country == u'MF':
        _odoo_country_id = 141
    if _country == u'MADAGASCAR' or _country == u'MADAGASKAR' or _country == u'MG':
        _odoo_country_id = 142
    if _country == u'MARSHALL ISLANDS' or _country == u'MARSHALLINSELN' or _country == u'MH':
        _odoo_country_id = 143
    if _country == u'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF' or _country == u'MAZEDONIEN, DIE EHEMALIGE JUGOSLAWISCHE REPUBLIK' or _country == u'MK':
        _odoo_country_id = 144
    if _country == u'MALI' or _country == u'MALI' or _country == u'ML':
        _odoo_country_id = 145
    if _country == u'MYANMAR' or _country == u'MYANMAR' or _country == u'MM':
        _odoo_country_id = 146
    if _country == u'MONGOLIA' or _country == u'MONGOLEI' or _country == u'MN':
        _odoo_country_id = 147
    if _country == u'MACAU' or _country == u'MACAU' or _country == u'MO':
        _odoo_country_id = 148
    if _country == u'NORTHERN MARIANA ISLANDS' or _country == u'NÖRDLICHE MARIANNENINSELN' or _country == u'MP':
        _odoo_country_id = 149
    if _country == u'MARTINIQUE (FRENCH)' or _country == u'MARTINIQUE (FRANZÖSISCH)' or _country == u'MQ':
        _odoo_country_id = 150
    if _country == u'MAURITANIA' or _country == u'MAURETANIEN' or _country == u'MR':
        _odoo_country_id = 151
    if _country == u'MONTSERRAT' or _country == u'MONTSERRAT' or _country == u'MS':
        _odoo_country_id = 152
    if _country == u'MALTA' or _country == u'MALTA' or _country == u'MT':
        _odoo_country_id = 153
    if _country == u'MAURITIUS' or _country == u'MAURITIUS' or _country == u'MU':
        _odoo_country_id = 154
    if _country == u'MALDIVES' or _country == u'MALEDIVEN' or _country == u'MV':
        _odoo_country_id = 155
    if _country == u'MALAWI' or _country == u'MALAWI' or _country == u'MW':
        _odoo_country_id = 156
    if _country == u'MEXICO' or _country == u'MEXIKO' or _country == u'MX':
        _odoo_country_id = 157
    if _country == u'MALAYSIA' or _country == u'MALAYSIA' or _country == u'MY':
        _odoo_country_id = 158
    if _country == u'MOZAMBIQUE' or _country == u'MOZAMBIQUE' or _country == u'MZ':
        _odoo_country_id = 159
    if _country == u'NAMIBIA' or _country == u'NAMIBIA' or _country == u'NA':
        _odoo_country_id = 160
    if _country == u'NEW CALEDONIA (FRENCH)' or _country == u'NEUE KALEDONIEN (FRANZÖSISCH)' or _country == u'NC':
        _odoo_country_id = 161
    if _country == u'NIGER' or _country == u'NIGER' or _country == u'NE':
        _odoo_country_id = 162
    if _country == u'NORFOLK ISLAND' or _country == u'NORFOLK-INSEL' or _country == u'NF':
        _odoo_country_id = 163
    if _country == u'NIGERIA' or _country == u'NIGERIA' or _country == u'NG':
        _odoo_country_id = 164
    if _country == u'NICARAGUA' or _country == u'NICARAGUA' or _country == u'NI':
        _odoo_country_id = 165
    if _country == u'NETHERLANDS' or _country == u'NIEDERLANDE' or _country == u'NL':
        _odoo_country_id = 166
    if _country == u'NORWAY' or _country == u'NORWEGEN' or _country == u'NO':
        _odoo_country_id = 167
    if _country == u'NEPAL' or _country == u'NEPAL' or _country == u'NP':
        _odoo_country_id = 168
    if _country == u'NAURU' or _country == u'NAURU' or _country == u'NR':
        _odoo_country_id = 169
    if _country == u'NEUTRAL ZONE' or _country == u'NEUTRAL ZONE' or _country == u'NT':
        _odoo_country_id = 170
    if _country == u'NIUE' or _country == u'NIUE' or _country == u'NU':
        _odoo_country_id = 171
    if _country == u'NEW ZEALAND' or _country == u'NEUSEELAND' or _country == u'NZ':
        _odoo_country_id = 172
    if _country == u'OMAN' or _country == u'OMAN' or _country == u'OM':
        _odoo_country_id = 173
    if _country == u'PANAMA' or _country == u'PANAMA' or _country == u'PA':
        _odoo_country_id = 174
    if _country == u'PERU' or _country == u'PERU' or _country == u'PE':
        _odoo_country_id = 175
    if _country == u'POLYNESIA (FRENCH)' or _country == u'POLYNESIEN (FRANZÖSISCH)' or _country == u'PF':
        _odoo_country_id = 176
    if _country == u'PAPUA NEW GUINEA' or _country == u'PAPUA-NEUGUINEA' or _country == u'PG':
        _odoo_country_id = 177
    if _country == u'PHILIPPINES' or _country == u'PHILIPPINEN' or _country == u'PH':
        _odoo_country_id = 178
    if _country == u'PAKISTAN' or _country == u'PAKISTAN' or _country == u'PK':
        _odoo_country_id = 179
    if _country == u'POLAND' or _country == u'POLEN' or _country == u'PL':
        _odoo_country_id = 180
    if _country == u'SAINT PIERRE AND MIQUELON' or _country == u'SAINT PIERRE UND MIQUELON' or _country == u'PM':
        _odoo_country_id = 181
    if _country == u'PITCAIRN ISLAND' or _country == u'PITCAIRN INSEL' or _country == u'PN':
        _odoo_country_id = 182
    if _country == u'PUERTO RICO' or _country == u'PUERTO RICO' or _country == u'PR':
        _odoo_country_id = 183
    if _country == u'PALESTINIAN TERRITORY, OCCUPIED' or _country == u'PALÄSTINENISCHES TERRITORIUM, BESETZT' or _country == u'PS':
        _odoo_country_id = 184
    if _country == u'PORTUGAL' or _country == u'PORTUGAL' or _country == u'PT':
        _odoo_country_id = 185
    if _country == u'PALAU' or _country == u'PALAU' or _country == u'PW':
        _odoo_country_id = 186
    if _country == u'PARAGUAY' or _country == u'PARAGUAY' or _country == u'PY':
        _odoo_country_id = 187
    if _country == u'QATAR' or _country == u'KATAR' or _country == u'QA':
        _odoo_country_id = 188
    if _country == u'REUNION (FRENCH)' or _country == u'REUNION (FRANZÖSISCH)' or _country == u'RE':
        _odoo_country_id = 189
    if _country == u'ROMANIA' or _country == u'RUMÄNIEN' or _country == u'RO':
        _odoo_country_id = 190
    if _country == u'SERBIA' or _country == u'SERBIEN' or _country == u'RS':
        _odoo_country_id = 191
    if _country == u'RUSSIAN FEDERATION' or _country == u'RUSSISCHE FÖDERATION' or _country == u'RU':
        _odoo_country_id = 192
    if _country == u'RWANDA' or _country == u'RWANDA' or _country == u'RW':
        _odoo_country_id = 193
    if _country == u'SAUDI ARABIA' or _country == u'SAUDI ARABIEN' or _country == u'SA':
        _odoo_country_id = 194
    if _country == u'SOLOMON ISLANDS' or _country == u'SALOMON-INSELN' or _country == u'SB':
        _odoo_country_id = 195
    if _country == u'SEYCHELLES' or _country == u'SEYCHELLEN' or _country == u'SC':
        _odoo_country_id = 196
    if _country == u'SUDAN' or _country == u'SUDAN' or _country == u'SD':
        _odoo_country_id = 197
    if _country == u'SWEDEN' or _country == u'SCHWEDEN' or _country == u'SE':
        _odoo_country_id = 198
    if _country == u'SINGAPORE' or _country == u'SINGAPUR' or _country == u'SG':
        _odoo_country_id = 199
    if _country == u'SAINT HELENA' or _country == u'SAINT HELENA' or _country == u'SH':
        _odoo_country_id = 200
    if _country == u'SLOVENIA' or _country == u'SLOWENIEN' or _country == u'SI':
        _odoo_country_id = 201
    if _country == u'SVALBARD AND JAN MAYEN ISLANDS' or _country == u'SVALBARD UND JAN MAYEN INSELN' or _country == u'SJ':
        _odoo_country_id = 202
    if _country == u'SLOVAKIA' or _country == u'SLOWAKEI' or _country == u'SK':
        _odoo_country_id = 203
    if _country == u'SIERRA LEONE' or _country == u'SIERRA LEONE' or _country == u'SL':
        _odoo_country_id = 204
    if _country == u'SAN MARINO' or _country == u'SAN MARINO' or _country == u'SM':
        _odoo_country_id = 205
    if _country == u'SENEGAL' or _country == u'SENEGAL' or _country == u'SN':
        _odoo_country_id = 206
    if _country == u'SOMALIA' or _country == u'SOMALIA' or _country == u'SO':
        _odoo_country_id = 207
    if _country == u'SURINAME' or _country == u'SURINAME' or _country == u'SR':
        _odoo_country_id = 208
    if _country == u'SOUTH SUDAN' or _country == u'SÜDSUDAN' or _country == u'SS':
        _odoo_country_id = 209
    if _country == u'SAINT TOME (SAO TOME) AND PRINCIPE' or _country == u'SAINT TOME (SAO TOME) UND PRINZIP' or _country == u'ST':
        _odoo_country_id = 210
    if _country == u'EL SALVADOR' or _country == u'EL SALVADOR' or _country == u'SV':
        _odoo_country_id = 211
    if _country == u'SINT MAARTEN (DUTCH PART)' or _country == u'SINT MAARTEN (DUTCH TEIL)' or _country == u'SX':
        _odoo_country_id = 212
    if _country == u'SYRIA' or _country == u'SYRIEN' or _country == u'SY':
        _odoo_country_id = 213
    if _country == u'SWAZILAND' or _country == u'Swaziland' or _country == u'SZ':
        _odoo_country_id = 214
    if _country == u'TURKS AND CAICOS ISLANDS' or _country == u'TURKS UND CAICOS INSELN' or _country == u'TC':
        _odoo_country_id = 215
    if _country == u'CHAD' or _country == u'TSCHAD' or _country == u'TD':
        _odoo_country_id = 216
    if _country == u'FRENCH SOUTHERN TERRITORIES' or _country == u'SÜDFRANZÖSISCHE TERRITORIEN' or _country == u'TF':
        _odoo_country_id = 217
    if _country == u'TOGO' or _country == u'GEHEN' or _country == u'TG':
        _odoo_country_id = 218
    if _country == u'THAILAND' or _country == u'THAILAND' or _country == u'TH':
        _odoo_country_id = 219
    if _country == u'TAJIKISTAN' or _country == u'TAJIKISTAN' or _country == u'TJ':
        _odoo_country_id = 220
    if _country == u'TOKELAU' or _country == u'TOKELAU' or _country == u'TK':
        _odoo_country_id = 221
    if _country == u'TURKMENISTAN' or _country == u'TÜRKMENISTAN' or _country == u'TM':
        _odoo_country_id = 222
    if _country == u'TUNISIA' or _country == u'TUNESIEN' or _country == u'TN':
        _odoo_country_id = 223
    if _country == u'TONGA' or _country == u'TONGA' or _country == u'TO':
        _odoo_country_id = 224
    if _country == u'EAST TIMOR' or _country == u'OSTTIMOR' or _country == u'TP':
        _odoo_country_id = 225
    if _country == u'TURKEY' or _country == u'TRUTHAHN' or _country == u'TR':
        _odoo_country_id = 226
    if _country == u'TRINIDAD AND TOBAGO' or _country == u'TRINIDAD UND TOBAGO' or _country == u'TT':
        _odoo_country_id = 227
    if _country == u'TUVALU' or _country == u'TUVALU' or _country == u'TV':
        _odoo_country_id = 228
    if _country == u'TAIWAN' or _country == u'TAIWAN' or _country == u'TW':
        _odoo_country_id = 229
    if _country == u'TANZANIA' or _country == u'TANSANIA' or _country == u'TZ':
        _odoo_country_id = 230
    if _country == u'UKRAINE' or _country == u'UKRAINE' or _country == u'UA':
        _odoo_country_id = 231
    if _country == u'UGANDA' or _country == u'UGANDA' or _country == u'UG':
        _odoo_country_id = 232
    if _country == u'UNITED KINGDOM' or _country == u'GROSSBRITANNIEN' or _country == u'GB':
        _odoo_country_id = 233
    if _country == u'USA MINOR OUTLYING ISLANDS' or _country == u'USA-MINOR-AUSGANGSINSELN' or _country == u'UM':
        _odoo_country_id = 234
    if _country == u'UNITED STATES' or _country == u'VEREINIGTE STAATEN' or _country == u'US':
        _odoo_country_id = 235
    if _country == u'URUGUAY' or _country == u'URUGUAY' or _country == u'UY':
        _odoo_country_id = 236
    if _country == u'UZBEKISTAN' or _country == u'USBEKISTAN' or _country == u'UZ':
        _odoo_country_id = 237
    if _country == u'HOLY SEE (VATICAN CITY STATE)' or _country == u'HEILIGE SEE (VATIKAN STADT)' or _country == u'VA':
        _odoo_country_id = 238
    if _country == u'SAINT VINCENT & GRENADINES' or _country == u'SAINT VINCENT UND GRENADINEN' or _country == u'VC':
        _odoo_country_id = 239
    if _country == u'VENEZUELA' or _country == u'VENEZUELA' or _country == u'VE':
        _odoo_country_id = 240
    if _country == u'VIRGIN ISLANDS (BRITISH)' or _country == u'VIRGIN ISLANDS (BRITISH)' or _country == u'VG':
        _odoo_country_id = 241
    if _country == u'VIRGIN ISLANDS (USA)' or _country == u'VIRGIN ISLANDS (USA)' or _country == u'VI':
        _odoo_country_id = 242
    if _country == u'VIETNAM' or _country == u'VIETNAM' or _country == u'VN':
        _odoo_country_id = 243
    if _country == u'VANUATU' or _country == u'VANUATU' or _country == u'VU':
        _odoo_country_id = 244
    if _country == u'WALLIS AND FUTUNA ISLANDS' or _country == u'WALLIS UND FUTUNA INSELN' or _country == u'WF':
        _odoo_country_id = 245
    if _country == u'SAMOA' or _country == u'SAMOA' or _country == u'WS':
        _odoo_country_id = 246
    if _country == u'YEMEN' or _country == u'JEMEN' or _country == u'YE':
        _odoo_country_id = 247
    if _country == u'MAYOTTE' or _country == u'MAYOTTE' or _country == u'YT':
        _odoo_country_id = 248
    if _country == u'YUGOSLAVIA' or _country == u'JUGOSLAWIEN' or _country == u'YU':
        _odoo_country_id = 249
    if _country == u'SOUTH AFRICA' or _country == u'SÜDAFRIKA' or _country == u'ZA':
        _odoo_country_id = 250
    if _country == u'ZAMBIA' or _country == u'SAMBIA' or _country == u'ZM':
        _odoo_country_id = 251
    if _country == u'ZAIRE' or _country == u'ZAIRE' or _country == u'ZR':
        _odoo_country_id = 252
    if _country == u'ZIMBABWE' or _country == u'SIMBABWE' or _country == u'ZW':
        _odoo_country_id = 253
    return _odoo_country_id
