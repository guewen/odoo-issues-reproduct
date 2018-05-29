from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    country_id = fields.Many2one(index=True)
