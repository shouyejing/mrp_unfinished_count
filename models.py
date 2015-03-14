from openerp import models, fields, api, exceptions, _

class MO(models.Model):
    _inherit = 'mrp.production'

    unfinished_count = fields.Float(compute='_compute_unfinished_count', store=True)
    finished_count = fields.Float(compute='_compute_unfinished_count', store=True)

    @api.depends("move_created_ids", "move_created_ids2")
    def _compute_unfinished_count(self):
        self.unfinished_count = sum(map(lambda x: x.product_uom_qty, self.move_created_ids))
        self.finished_count = sum(map(lambda x: x.product_uom_qty, self.move_created_ids2))
