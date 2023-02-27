from odoo import fields, models, api
from ast import literal_eval


class ProfitAndLossV2(models.Model):
    _name = 'team.profit.loss.v2'
    _description = 'Team Profit and Loss'
    _inherit = 'res.config.settings'

    name = fields.Char('Name', copy=False)
    analytic_acc = fields.Many2many('account.analytic.account')

    # def _add_domain(self):
    #     user_obj = self.env['res.users'].search([('department_id', '=', self.env.user.department_id.id)])
    #     if user_obj:
    #         domain = [('id', 'in', user_obj.ids)]
    #     else:
    #         domain = [('id', '=', -1)]
    #     return domain
    #
    # analytic_acc = fields.Many2many('account.analytic.account', 'your_many2many_table_name', 'column_1', 'columns_2',
    #                                 string="My many2many Field", domain=_add_domain)

    def set_values(self):
        res = super(ProfitAndLossV2, self).set_values()
        self.env['ir.config_parameter'].set_param('team_accounting_profit_and_loss.analytic_acc', self.analytic_acc.ids)
        return res
    #
    # @api.model
    # def get_values(self):
    #     res = super(ProfitAndLossV2, self).get_values()
    #     ICPSudo = self.env['ir.config_parameter'].sudo()
    #     partner_parameter = ICPSudo.get_param('team_accounting_profit_and_loss.analytic_acc')
    #     print(partner_parameter, '<---- Param ID')
    #     res.update(
    #         analytic_acc=[(6, 0, literal_eval(partner_parameter))],
    #     )
    #     return res








