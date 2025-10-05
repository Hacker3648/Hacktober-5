# -*- coding: utf-8 -*-

{
    'name': 'Custom Receipt',
    'version': '17.0',
    'summary': '',
    'author': 'Sunil Prajapati',
    'sequence': 2,
    'description': """ """,
    'category': '',
    'website': 'https://sunilprajapati.pythonanywhere.com',
    'images': ['static/description/icon.png'],
    'depends': ['l10n_sa_pos','point_of_sale'],
    'assets':{
        'point_of_sale._assets_pos': [
            'custom_receipt/static/src/order_receipt.xml',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
