__author__ = 'wangting'
from openerp import models, fields, api, exceptions, _

class MO(models.Model):
    _inherit = 'mrp.production'

    unfinished_count = fields.Float(compute='_compute_unfinished_count')
    finished_count = fields.Float(compute='_compute_unfinished_count')

    @api.depends("move_created_ids", "move_created_ids2")
    def _compute_unfinished_count(self):
        total = sum(map(lambda x: x.product_uom_qty, self.move_created_ids))
        self.finished_count = sum(map(lambda x: x.product_uom_qty, self.move_created_ids2))
        self.unfinished_count = total-self.finished_count
