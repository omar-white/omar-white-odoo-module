{
    'name': 'Inventory TofuPilot Integration',
    'version': '16.0.1.0.0',
    'author': 'Your Name or Company',
    'category': 'Inventory',
    'summary': 'Integrates Inventory Lot/Serial numbers with TofuPilot API.',
    'description': 'Adds a TofuPilot field to the Lot/Serial numbers in the Inventory module and fetches data from the TofuPilot API.',
    'depends': ['stock'],
    'data': [
        'views/stock_lot_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}