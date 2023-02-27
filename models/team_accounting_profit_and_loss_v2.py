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

    def _find_default_analytic_id(self):
        alias = self.env.ref('team_accounting_profit_and_loss.analytic_acc', False)
        return alias
    
    @api.model
    def get_values(self):
        res = super(ProfitAndLossV2, self).get_values()
        alias = self._find_default_analytic_id()
        res.update(
            analytic_acc=alias.alias_name if alias else False,
        )
        return res

    def set_values(self):
        super(ProfitAndLossV2, self).set_values()
        analytic_var = self._find_default_analytic_id()
        if analytic_var:
            analytic_var.write({
                'analytic_acc': self.analytic_acc.id
            })
        else:
            #checking if have data
            return False
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








