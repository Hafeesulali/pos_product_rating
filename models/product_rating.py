from odoo import fields, models


class ProductRating(models.Model):
    _inherit = "product.template"

    product_rating = fields.Selection(string="Product Rating",
                                      selection=[('\u2B50', '1'),
                                                 ('\u2B50' * 2, '2'),
                                                 ('\u2B50' * 3, '3'),
                                                 ('\u2B50' * 4, '4'),
                                                 ('\u2B50' * 5, '5'),
                                                 ], default='\u2B50')
