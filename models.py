##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
   _inherit = 'product.template'

   @api.depends('company_id')
   def _compute_currency_id(self):
        for template in self:
            template.currency_id = self.env.ref('base.USD')
            template.cost_currency_id = self.env.ref('base.USD')
