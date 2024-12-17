{
    'name': 'Inventory TofuPilot Integration',
    'version': '18.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Adds a TofuPilot field to Lots/Serial Numbers.',
    'description': 'Fetches and displays a TofuPilot link for Lots/Serial Numbers.',
    'depends': ['stock'],  # Inherit from stock.lot
    'data': [
        'views/stock_lot_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
