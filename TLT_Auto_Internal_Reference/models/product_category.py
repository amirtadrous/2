# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    product_sequence_id = fields.Many2one('ir.sequence', 'Product Sequence', ondelete="restrict")
    apply_on_barcode = fields.Boolean('Barcode = Internal Reference', default=False)
    product_type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service'),
        ('product', 'Storable Product')], string='Product Type',  help="Product type that all included products must have.")


    @api.onchange('product_sequence_id')
    def _onchange_product_sequence_id(self):
        if not self.product_sequence_id:
            self.apply_on_barcode = False

