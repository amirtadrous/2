# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals_list):
        if 'categ_id' in vals_list:
            categ_id = vals_list.get('categ_id', False)
            product_type = vals_list.get('detailed_type', False)
            categ_product_type = self.env['product.category'].browse(categ_id).product_type if categ_id else ''
            if categ_product_type and product_type and categ_product_type != product_type:
                vals_list['detailed_type'] = categ_product_type
                raise UserError("You can't choose product type different than Category product type !")
            elif categ_product_type and not product_type:
                vals_list['detailed_type'] = categ_product_type
        return super(ProductTemplate, self).create(vals_list)

    def write(self, vals):
        categ_id = vals.get('categ_id', self.categ_id.id)
        product_type = vals.get('detailed_type', False)
        categ_product_type = self.env['product.category'].browse(categ_id).product_type if categ_id else ''
        if product_type and categ_product_type and product_type != categ_product_type:
            raise UserError("You can't choose product type different than Category product type !")
        elif categ_product_type and not product_type:
            vals['detailed_type'] = categ_product_type
        return super(ProductTemplate, self).write(vals)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals_list):
        if 'categ_id' in vals_list:
            categ_id = vals_list.get('categ_id', False)
            product_type = vals_list.get('detailed_type', False)
            categ_product_type = self.env['product.category'].browse(categ_id).product_type if categ_id else ''
            if categ_product_type and product_type and categ_product_type != product_type:
                vals_list['detailed_type'] = categ_product_type
                raise UserError("You can't choose product type different than Category product type !")
            elif categ_product_type and not product_type:
                vals_list['detailed_type'] = categ_product_type
        record = super(ProductProduct, self).create(vals_list)
        if record.categ_id.product_sequence_id:
            next_code = record.categ_id.product_sequence_id.next_by_id()
            record.default_code = next_code
            if record.categ_id.apply_on_barcode:
                record.barcode = next_code
        return record

    def write(self, vals):
        categ_id = vals.get('categ_id', self.categ_id.id)
        product_type = vals.get('detailed_type', False)
        categ_product_type = self.env['product.category'].browse(categ_id).product_type if categ_id else ''
        if product_type and categ_product_type and product_type != categ_product_type:
            raise UserError("You can't choose product type different than Category product type !")
        elif categ_product_type and not product_type:
            vals['detailed_type'] = categ_product_type
        return super(ProductProduct, self).write(vals)
