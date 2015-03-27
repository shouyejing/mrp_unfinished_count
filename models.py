from openerp import models, fields, api, exceptions, _

class MO(models.Model):
    _inherit = 'mrp.production'

    unfinished_quantity = fields.Float(compute='_compute_unfinished_quantity', string='Unfinished Quantity',
                                       store=True)
    finished_quantity = fields.Float(compute='_compute_unfinished_quantity', string='Finished Quantity',
                                     store=True)

    @api.depends("move_created_ids", "move_created_ids2")
    @api.one
    def _compute_unfinished_quantity(self):
        self.finished_quantity = sum(x.product_uom_qty for x in self.move_created_ids2)
        self.unfinished_quantity = self.product_qty - self.finished_quantity
