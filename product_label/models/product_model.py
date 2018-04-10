# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.base.ir.ir_qweb.qweb import QWeb
from lxml import etree


class ProductTemplate(models.Model):
    _inherit = "product.template"

    default_label_id = fields.Many2one('product.label', 'Default Label', help="Select label for the current product")


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def get_render_qweb(self):
        template =self.default_label_id.qweb_template
        dom = etree.fromstring(template)
        html = QWeb().render(dom, {'product': self})
        return html


class ProductLabel(models.Model):
    _name = "product.label"

    name = fields.Char('Name', required=True)
    paper_format_id = fields.Many2one('report.paperformat', 'Paper format', required=True)
    qweb_template = fields.Text('Qweb')
