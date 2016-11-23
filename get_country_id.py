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
    return cleanstr;


def get_odoo_country_id(_country):
    _country = _country.upper()
    _country = unicode(_country,"utf-8")
    _odoo_country_id = 0
    if _country == u'AUSTRALIA' or _country == u'AUSTRALIEN' or _country == u'AU':
        _odoo_country_id = 14
    if _country == u'AUSTRIA' or _country == u'ÖSTERREICH' or _country == u'AT':
        _odoo_country_id = 13
    if _country == u'BELGIUM' or _country == u'BELGIEN' or _country == u'BE':
        _odoo_country_id = 21
    if _country == u'BULGARIA' or _country == u'BULGARIEN' or _country == u'BG':
        _odoo_country_id = 23
    if _country == u'BRAZIL' or _country == u'BRASILIEN' or _country == u'BR':
        _odoo_country_id = 32
    if _country == u'CANADA' or _country == u'KANADA' or _country == u'CA':
        _odoo_country_id = 39
    if _country == u'CHINA' or _country == u'VOLKSREPUBLIK CHINA' or _country == u'CN':
        _odoo_country_id = 49
    if _country == u'CROATIA' or _country == u'KROATIEN' or _country == u'HR':
        _odoo_country_id = 98
    if _country == u'Czech Republic' or _country == u'TSCHECHISCHE REPUBLIK' or _country == u'CZ':
        _odoo_country_id = 57
    if _country == u'DENMARK' or _country == u'DÄNEMARK' or _country == u'DK':
        _odoo_country_id = 39
    if _country == u'ESTONIA' or _country == u'ESTLAND' or _country == u'EE':
        _odoo_country_id = 65
    if _country == u'FIJI' or _country == u'FIDSCHI' or _country == u'FJ':
        _odoo_country_id = 72
    if _country == u'FINLAND' or _country == u'FINNLAND' or _country == u'FI':
        _odoo_country_id = 71
    if _country == u'FRANCE' or _country == u'FRANKREICH' or _country == u'FR':
        _odoo_country_id = 76
    if _country == u'GERMANY' or _country == u'DEUTSCHLAND' or _country == u'DE':
        _odoo_country_id = 58
    if _country == u'GREECE' or _country == u'GRIECHENLAND' or _country == u'GR':
        _odoo_country_id = 89
    if _country == u'HONG KONG' or _country == u'HONG KONG' or _country == u'HK':
        _odoo_country_id = 95
    if _country == u'HUNGARY' or _country == u'UNGARN' or _country == u'HU':
        _odoo_country_id = 100
    if _country == u'ICELAND' or _country == u'ISLAND' or _country == u'IS':
        _odoo_country_id = 109
    if _country == u'INDIA' or _country == u'INDIEN' or _country == u'IN':
        _odoo_country_id = 105
    if _country == u'INDONESIA' or _country == u'INDONESIEN' or _country == u'ID':
        _odoo_country_id = 101
    if _country == u'IRELAND' or _country == u'IRLAND' or _country == u'IE':
        _odoo_country_id = 102
    if _country == u'ISRAAEL' or _country == u'ISRAEL' or _country == u'IL':
        _odoo_country_id = 103
    if _country == u'ITALY' or _country == u'ITALIEN' or _country == u'IT':
        _odoo_country_id = 110
    if _country == u'JAPAN' or _country == u'JAPAN' or _country == u'JP':
        _odoo_country_id = 114
    if _country == u'KUWAIT' or _country == u'KUWAIT' or _country == u'KW':
        _odoo_country_id = 123
    if _country == u'LIECHTENSTEIN' or _country == u'LIECHTENSTEIN' or _country == u'LI':
        _odoo_country_id = 129
    if _country == u'LITHUANIA' or _country == u'LITAUEN' or _country == u'LT':
        _odoo_country_id = 133
    if _country == u'LUXEMBOURG' or _country == u'LUXEMBURG' or _country == u'LU':
        _odoo_country_id = 134
    if _country == u'MALTA' or _country == u'MALTA' or _country == u'MT':
        _odoo_country_id = 153
    if _country == u'MEXIKO' or _country == u'MEXIKO' or _country == u'MX':
        _odoo_country_id = 157
    if _country == u'NETHERLANDS' or _country == u'NIEDERLANDE' or _country == u'NL' or _country == u'HOLAND':
        _odoo_country_id = 166
    if _country == u'NORWAY' or _country == u'NORWEGEN' or _country == u'NO':
        _odoo_country_id = 167
    if _country == u'POLAND' or _country == u'POLEN' or _country == u'PL':
        _odoo_country_id = 180
    if _country == u'PORTUGAL' or _country == u'PORTUGAL' or _country == u'PT':
        _odoo_country_id = 185
    if _country == u'REUNION (FRENCH)' or _country == u'RÉUNION' or _country == u'RE':
        _odoo_country_id = 189
    if _country == u'ROMANIA' or _country == u'RUMÄNIEN' or _country == u'RO':
        _odoo_country_id = 190
    if _country == u'RUSSIAN FEDERATION' or _country == u'RUSLAND' or _country == u'RU' or _country == u'RUSSIA':
        _odoo_country_id = 192
    if _country == u'SLOVAKIA' or _country == u'SLOWAKEI' or _country == u'SK':
        _odoo_country_id = 203
    if _country == u'SLOVENIA' or _country == u'SLOWENIEN' or _country == u'SE':
        _odoo_country_id = 201
    if _country == u'SPAIN' or _country == u'SPANIEN' or _country == u'ES':
        _odoo_country_id = 69
    if _country == u'SWEDEN' or _country == u'SCHWEDEN' or _country == u'SE':
        _odoo_country_id = 198
    if _country == u'SWITZERLAND' or _country == u'SCHWEIZ' or _country == u'CH':
        _odoo_country_id = 44
    if _country == u'SINGAPORE' or _country == u'SINGAPUR' or _country == u'SG':
        _odoo_country_id = 199
    if _country == u'SAINT MARTIN (FRENCH PART)' or _country == u'ST. MARTIN-INSELN (FRANZ.)' or _country == u'MF':
        _odoo_country_id = 141
    if _country == u'SOUTH AFRICA' or _country == u'SÜDAFRIKA' or _country == u'ZA':
        _odoo_country_id = 250
    if _country == u'SOUTH KOREA' or _country == u'SÜDKOREA' or _country == u'KR':
        _odoo_country_id = 122
    if _country == u'TAIWAN' or _country == u'TAIWAN' or _country == u'TW':
        _odoo_country_id = 229
    if _country == u'TURKEY' or _country == u'TÜRKEI' or _country == u'TR':
        _odoo_country_id = 226
    if _country == u'UNITED KINGDOM' or _country == u'GROSSBRITANIEN' or _country == u'UK':
        _odoo_country_id = 233
    if _country == u'UNITED STATES' or _country == u'VEREINIGTE STAATEN VON AMERIKA' or _country == u'US' or _country == u'USA':
        _odoo_country_id = 235
    return _odoo_country_id
