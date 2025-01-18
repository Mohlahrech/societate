# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': '58 Wilayas - Algérie + Modifs',
    'summary' : "Gestion par base de données relationnelles des adresses de vos contacts localisé en Algérie",
    'description' : "Modifié par moh: 58 wilayas avac commune + imprimé des wilayas et communes dans factures + filtrer factures par wilaya + champ tele commercial dans contact recuperé dans la facture pour pouvoir filtrer",
    'version': '16.1.2.0',
    'category': 'Sales/CRM',

    'company': 'Modified',
    'author' : 'Mohamed LAHRECH',
    'maintainer': 'Mohamed LAHRECH ',

    
    'support' : "mohamed.lahrech.dz@gmail.com",
    'website' : "https://www.odooavecvous.net",

    "contributors": [
        
        "1 <Mohamed LAHRECH>"

    ],

    'license' : "OPL-1",
    'price' : "55",
    'currency' : 'DZ',


    'images' : ['images/banner.gif'],

    'depends': [
        'base',
        'contacts',
        'account',
        'stock',
    ],
    
    'data': [
        'security/ir.model.access.csv',
        'report/invoice.xml',
        'report/bls.xml',


        'data/res_country_state.xml',
        'data/res_country_commune.xml',
        'data/res_country_localite.xml',

        'views/res_country.xml',
        'views/res_bank.xml',
        'views/res_partner.xml',
        'views/res_company.xml',
    ],
    
    'demo' : [
    ],
    
    'installable': True,
    'auto_install': False,
    "application": False,
}
