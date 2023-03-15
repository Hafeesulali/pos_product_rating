{'name': 'Pos rating',
 'installable': True,
 'auto_install': False,
 'version': '16.0.1.0.0',
 'depends': ['base', 'point_of_sale'],
 'data': ['views/product_rating_views.xml'],
 'assets': {
     'point_of_sale.assets': [
         'pos_rating/static/src/js/receipt.js',
         'pos_rating/static/src/xml/pos_session_views.xml',
         'pos_rating/static/src/xml/pos_receipt.xml',
     ],
 },

 }
