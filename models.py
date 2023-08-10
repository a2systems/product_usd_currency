##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    parent_document_ids = fields.One2many(comodel_name='partner.document',inverse_name='parent_id',string='Company Documents')
    document_ids = fields.One2many(comodel_name='partner.document',inverse_name='partner_id',string='Employee Documents')
    msa = fields.Boolean('MSA')
    rt_insurance_cover = fields.Boolean('RangeTower Insurance Cover')
    team_qty = fields.Integer('Teams Quantity')
    state_ids = fields.Many2many(comodel_name='res.country.state',relname='res_partner_states',col1='partner_id',col2='state_id',string='Allowed States')
    equipment_ids = fields.Many2many(comodel_name='res.partner.equipment',relname='rel_partner_equipments',col1='partner_id',col2='equipment_id',string='Equipments')
    capability_ids = fields.Many2many(comodel_name='res.partner.capability',relname='rel_partner_capabilities',col1='partner_id',col2='capability_id',string='Capabilities')

class ResPartnerEquipment(models.Model):
    _name = 'res.partner.equipment'
    _description = 'res.partner.equipment'

    name = fields.Char('Equipment')

class ResPartnerCapability(models.Model):
    _name = 'res.partner.capability'
    _description = 'res.partner.capability'

    name = fields.Char('Capability')

class PartnerDocumentTag(models.Model):
    _name = 'partner.document.tag'
    _description = 'partner.document.tag'

    name = fields.Char('Name')

class PartnerDocumentType(models.Model):
    _name = 'partner.document.type'
    _description = 'partner.document.type'

    name = fields.Char('Name')

class PartnerDocument(models.Model):
    _name = 'partner.document'
    _description = 'partner.document'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def create(self, vals):
        res = super(PartnerDocument, self).create(vals)
        if res.partner_id.parent_id:
            res.parent_id = res.partner_id.parent_id.id
        return res

    document_path = fields.Char('Company/Employee documents')
    name = fields.Char('Name')
    deadline = fields.Date('Deadline')
    partner_id = fields.Many2one('res.partner','Contact')
    parent_id = fields.Many2one('res.partner','Company')
    document_type_id = fields.Many2one('partner.document.type',string='Document Type')
    tag_ids = fields.Many2many(comodel_name='partner.document.tag',relname='partner_document_tag_rel',col1='partner_id',col2='tag_id',string='Tags')
