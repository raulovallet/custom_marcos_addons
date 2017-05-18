# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomMarcosAddonsAcountInvoce(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    @api.model
    def create(self,vals):

        if vals.get('fiscal_position_id') is not False:
            fisacal_position = self.env['account.fiscal.position'].search([('id','=',vals.get('fiscal_position_id'))])
            vals['sale_fiscal_type'] = fisacal_position.sale_fiscal_type

        return super(CustomMarcosAddonsAcountInvoce, self).create(vals)