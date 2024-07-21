# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': "Droit de timbre client - Algérie",
    'summary': """Ce module permettant de gérer les droits de timbre pour les paiements en liquide sur les factures et les avoirs clients""",
    'description': """Gestion des droits de timbre client""",

    'version': '15.0.3.3',
    'category': 'Accounting/Accounting',


    "contributors": [
        "1 <Djamel Eddine YAGOUB>",
        "2 <Nassim REFES>",
        "3 <Kamel BENCHEHIDA>",
        "4 <Yamina ZOUATINE>",
        "5 <Fatima MESSADI>",
        "6 <Yassamine CHENAFA>",
        "7 <Chems eddine SAHININE>",
    ],
    
    
    
    'company'     : 'Elosys',
    'author'      : 'Elosys',
    'maintainer'  : 'Elosys',

    'website': 'http://www.elosys.net',
    'support' : "support@elosys.net",

    'live_test_url' : "https://www.elosys.net/shop",    


    "license": "OPL-1",
    "price": 55,
    "currency": 'EUR',


    'depends': [
        'base',
        'account'
    ],

    "sequence":1,

    'data': [
        'views/configuration_timbre.xml',
        'views/account_move.xml',
        'views/account_move_report.xml',
        'views/account_payment.xml',
        
        'security/ir.model.access.csv',

        'data/paymment_mode.xml',
        'data/accounting_group.xml',
    ],



    'images': ['images/banner.gif'],



    'installable': True,
    'auto_install': False,
    'application': False,
    #'post_init_hook': "post_init_hook",
}
