# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    _sql_constraints = [
        ('pricelist_item_uniq', 'unique(product_tmpl_id,min_quantity,fixed_price,currency_id,date_start,date_end)',
         'Price List item (Product,Min. Quantity,Price,Start Date,End Date) must be unique!'),
    ]