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
import odoorpc
import sqlite3 as lite

import sys

import get_country_id

# Prepare the connection to the server
odoo = odoorpc.ODOO('192.168.x.x', port=8069)

# Login
odoo.login('dbname', 'admin', 'xxx')

RES_PARTNER = odoo.env['res.partner']
ACCOUNT_ACCOUNT = odoo.env['account.account']
RES_PARTNER_CATEGORY = odoo.env['res.partner.category']


# Debitoren-Grundparameter feststellen
_default_account_id = ACCOUNT_ACCOUNT.search([('code', '=', '10000')])  # Schweiz 1100 / 10000 Deutschland
_default_account_id = _default_account_id[0]
_default_account_data = ACCOUNT_ACCOUNT.browse(_default_account_id)
_parent_id = _default_account_data['parent_id'].id
_user_type_id = _default_account_data['user_type'].id


con = lite.connect('sourcedb.sqlite')
# Ansteuerung der Felder per Namen
con.row_factory = lite.Row

# Feld Info > Adressart
# Standardadresse
# Ansprechpartner
# Rechnungsadresse
# Lieferadresse
# Historische Adressen

with con:
    # Zunächst nur die Hauptadressen importieren
    cur = con.cursor()
    cur.execute("SELECT COUNT(DISTINCT Kundennummer) FROM Kunden WHERE Info='Standardadresse';")
    rows = cur.fetchall()
    for row in rows:
        gesamtzaehler = row[0]
        print "Gesamtpositionen: " + str(gesamtzaehler)

    _myQuery = """
               SELECT * FROM Kunden
               WHERE Info='Standardadresse'
               AND Kundennummer NOT IN ('10035','10176')
               ORDER BY Kundennummer;
               """
    cur.execute(_myQuery)

    zaehler = 0  # Zaehlvariable
    # print all the first cell of all the rows
    for row in cur.fetchall():

        _is_activ = row['_Inaktiv']

        _partner_data = {}

        _anrede = row['Anrede'].encode('utf-8').strip()
        if _anrede == "Company" or _anrede == "Conpany" or _anrede == "Firma":
            # Ist Unternehmen
            _partner_data['is_company'] = True
        else:
            _partner_data['is_company'] = False

        if _anrede == "Dr.":
            _partner_data['title'] = 7
        if _anrede == "Frau" or _anrede == "Miss" or _anrede[4:] == "Miss" or _anrede[3:] == "Mrs" or _anrede == "Ms.":
            _partner_data['title'] = 3
        if _anrede[4:] == "Herr" or _anrede == "Kerr" or _anrede == "Mr." or _anrede == "Mr" or _anrede == "Mister":
            _partner_data['title'] = 5

        _partner_data['customer'] = True
        _partner_data['supplier'] = False

        # Kundennummer
        _customerno = row['Kundennummer']
        if _customerno != None and _customerno != "":
            _partner_data['eq_customer_ref'] = _customerno

        _partner_id = RES_PARTNER.search([('eq_customer_ref', '=', _customerno)])


        # Name 1
        _customername1 = row['Name1'].encode('utf-8').strip()
        if _customername1 != None and _customername1 != "":
            _partner_data['name'] = _customername1

        # Name 2
        _customername2 = row['Name2'].encode('utf-8').strip()
        if _customername2 != None and _customername2 != "":
            _partner_data['eq_name2'] = _customername2

        # Name3
        # if row[x] != None and row[x] != "":
        #    _partner_data['eq_name3'] = row[x]

        # Land
        _land = row['Land'].encode('utf-8').strip()
        _land_id = get_country_id.get_odoo_country_id(_land)
        if _land_id == 0: _land_id = 44 # Ohne Land = Schweiz
        _partner_data['country_id'] = _land_id

        # Strasse
        _street = row['Strasse'].encode('utf-8').strip()
        _houseno = ""
        if _street != None and _street != "":
            # Hausnummer in der Schweiz und Deutschland separieren
            if _land_id == 58 or _land_id == 44:
                try:
                    _houseno = str(int(filter(str.isdigit, _street))).strip()
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                _len_no = len(_houseno)
                if _len_no > 0:
                    _street = _street.replace(_houseno, '').strip()
            _partner_data['street'] = _street

        # Hausnummer
        if _houseno != None and _houseno != "":
            _partner_data['eq_house_no'] = _houseno

        # PLZ
        _zipcode = row['PLZ'].encode('utf-8').strip()
        if _zipcode != None and _zipcode != "":
            _partner_data['zip'] = _zipcode

        # Ort
        _city = row['Ort'].encode('utf-8').strip()
        if _city != None and _city != "":
            _partner_data['city'] = _city

        # Telefon
        _phone = row['Telefon'].encode('utf-8').strip()
        if _phone != None and _phone != "":
            _partner_data['phone'] = _phone

        # Mobil
        _mobile = row['Mobiltel'].encode('utf-8').strip()
        if _mobile != None and _mobile != "":
            _partner_data['mobile'] = _mobile

        # Fax
        _fax = row['Fax'].encode('utf-8').strip()
        if _fax != None and _fax != "":
            _partner_data['fax'] = _fax

        # Email
        _email = row['EMail'].encode('utf-8').strip()
        if _email != None and _email != "":
            _partner_data['email'] = _email

        # Homepage
        _homepage = row['InternetAdresse'].encode('utf-8').strip()
        if _homepage != None and _homepage != "":
            _partner_data['homepage'] = _homepage


        # Funktion
        _function = row['Funktion'].encode('utf-8').strip()
        if _function != None and _function != "":
            _partner_data['function'] = _function

        # ---------------------------Schlagwoerter--------------------------------------------------
        _category_id = False
        _category_name = row['Gebiet'].encode('utf-8').strip()
        if len(_category_name) != 0 and _category_name != "NULL":
            _category_id = RES_PARTNER_CATEGORY.search([('name', '=', _category_name)])
            _partner_data['category_id'] = [(6, 0, [_category_id])]
        # ------------------------------------------------------------------------------------------

        # # Notizen
        # myNote = row[x] + '\r\n' + row[x]
        # myNote = myNote.strip()
        # if myNote != "":
        #     partner_data['comment'] = myNote

        # Brief Begrüßung
        # if row[x] != None and row[x] != "":
        #     _partner_data['eq_letter_salutation'] = row[x]

        # Vorname
        # if row[x] != None and row[x] != "":
        #     _partner_data['eq_firstname'] = row[x]

        # -----------------------------Debitorenkonten------------------------------------------------
        _account_data = {
                        'active': True,
                        'reconcile': True,
                        'code': _customerno,
                        'name': _customername1,
                        'parent_id': _parent_id,
                        'type': _default_account_data['type'],
                        'user_type': _user_type_id,
                         }
        _account_id_search = ACCOUNT_ACCOUNT.search([('code', '=', _customerno)])
        if len(_account_id_search) == 0:
            _account_account_id = ACCOUNT_ACCOUNT.create(_account_data)
            ACCOUNT_ACCOUNT.env.commit()
            _account_id_search = ACCOUNT_ACCOUNT.search([('code', '=', _customerno)])
            _account_id = _account_id_search[0]
        else:
            _account_id = _account_id_search[0]

        # Debitor auslesen
        if _account_id != None and _account_id != "":
            account_account = ACCOUNT_ACCOUNT.browse(_account_id)
            _partner_data['property_account_receivable'] = _account_id
        # ------------------------------------------------------------------------------------------



        if len(_partner_id) == 0:
            _res_partner_id = RES_PARTNER.create(_partner_data)
            _importtype = " importiert "
            RES_PARTNER.env.commit()
            _partner_id = RES_PARTNER.search([('eq_customer_ref', '=', _customerno)])
            _res_partner = RES_PARTNER.browse(_partner_id)
        else:
            _res_partner = RES_PARTNER.browse(_partner_id)
            _res_partner.write(_partner_data)
            _res_partner.env.commit()
            _importtype = " aktualisiert "

            # # Zahlungskonditionen
            # mypayid = 0
            # if row[x] == "0": mypayid = 2
            # if mypayid == -1: mypayid = 2
            #
            # partner_data['property_payment_term'] = mypayid
            # # print mypayid
            # # print row[x]


            # ------------------------------------------------------------------------------------------------
            # -----------------------------Zahlungsbedingungen------------------------------------------------
            #     payment_data ={
            #                     'name': row[16],
            #                     'active': True,
            #                     'note': row[16],
            #
            #                    }
            #     payment_name_mapping = {
            #                             'Sofortige Zahlung' : 'Immediate Payment',
            #                             '15 Tage' : '15 Days',
            #                             '30 Tage netto' :  '30 Net Days',
            #                             '30 Tage zum Monatsende' : '30 Days end of Month',
            #                             '30% Anzahlung, Rest in 30 Tagen' : '30% Advance End 30 Days',
            #                             }
            #
            #     Payment_Name = row[16]
            #
            #     if Payment_Name in payment_name_mapping:
            #         payment_id_search = sock.execute(dbname, uid, pwd, 'account.payment.term', 'search', [('name', '=', payment_name_mapping[row[16]])])
            #         if len(payment_id_search) == 0:
            #             payment_id = sock.execute(dbname, uid, pwd, 'account.payment.term', 'create', payment_data)
            #         else:
            #             payment_id = payment_id_search[0]
            #     else:
            #         payment_id = sock.execute(dbname, uid, pwd, 'account.payment.term', 'create', payment_data)
            #
            #     partner_data['property_payment_term'] = payment_id
            # -----------------------------------------------------------------------------------------


        zaehler = zaehler + 1
        print "Kunden " + str(_customerno) + " / " + _customername1 + _importtype + " - bereits " + str(
            zaehler) + " von " + str(gesamtzaehler) + " Positionen.."

con.close()
print "Fertig!"
