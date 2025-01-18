# -*- coding: utf-8 -*-
# module template
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Sequence',
    'version': '16.0',
    'category': 'Base',
    'license': 'AGPL-3',
    'author': "Odoo Tips",
    'website': 'https://www.facebook.com/OdooTips/',
    'depends': ['base','crm',
                ],

    'images': ['images/main_screenshot.png'],
    'data': [
              'security/ir.model.access.csv',
             'data/res_partner_sequence.xml',
             'views/hopitaux.xml',
             'views/crm.xml',
              'views/sécurité_sociale.xml',
             ],
    'installable': True,
    'application': True,
}
