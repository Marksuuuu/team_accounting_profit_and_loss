from odoo import fields, models, api
from ast import literal_eval


class ProfitAndLossV2(models.Model):
    _name = 'team.profit.loss.v2'
    _description = 'Team Profit and Loss'

    name = fields.Char()
    analytic_acc = fields.Many2many('account.analytic.account', string='Analytic Account')
    chart_of_account = fields.Many2many('account.account', copy=False)
    move_id = fields.Many2many('account.move.line', string='Journal Item', ondelete='cascade', index=True)


    @api.onchange('analytic_acc')
    def _get_analytic_acc(self):
        for rec in self.analytic_acc:
            for get_move_line in rec.line_ids:
                print(get_move_line._origin)











