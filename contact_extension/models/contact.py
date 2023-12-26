from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductImport(models.Model):
    _inherit = 'res.partner'

    license_no = fields.Char(string='License no')
    exp_date = fields.Date('Expiration Date')
    partner_code = fields.Char('Code')

    @api.constrains('partner_code')
    def _check_partner_code_uniqueness(self):
        for record in self:
            if self.search_count([('partner_code', '=', record.partner_code)]) > 1:
                raise ValidationError("Partner code must be unique.")