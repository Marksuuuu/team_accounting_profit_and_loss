from odoo import fields, models, api


class ProfitAndLoss(models.Model):
    _name = 'team.profit.loss'
    _description = 'Team Profit and Loss'

    name = fields.Char(string="Profit and Loss", readonly=True, copy=False, default='New')
    state = fields.Selection(selection=[
        ('post', 'Post'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancelled'),
        ('draft', 'Draft'),
    ], string='Status', readonly=True, copy=False, tracking=True, default='draft')

    profit_and_loss_date_start = fields.Datetime('Date Start')
    profit_and_loss_date_end = fields.Datetime('Date End')
    connection = fields.One2many('team.profit.loss.line', 'team_and_l')
    fetch_analytic_line_data = fields.Float()
    view_count = fields.Integer()

    def action_view_lines(self):
        return {
            'name': 'Analytic Account Line',
            'view_mode': 'tree,form',
            'res_model': 'team.profit.loss.line',
            'view_id': self.env.ref("team_profit_loss_line_act_window").id,
            'type': 'ir.actions.act_window',
            'domain': [('payment_id', 'in', self.ids)],
        }

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'team.profit.loss') or 'New'
        result = super(ProfitAndLoss, self).create(vals)
        return result

    def post_but(self):
        for rec in self:
            rec.state = 'post'

    def confirm_but(self):
        for rec in self:
            rec.state = 'confirm'

    def cancel_but(self):
        for rec in self:
            rec.state = 'cancel'


class TeamProfitLossLine(models.Model):
    _name = 'team.profit.loss.line'
    _description = 'Team Profit and Loss Move Line'

    team_and_l = fields.Many2one('team.profit.loss')
    test = fields.Many2one('account.analytic.line')
    connection = fields.Many2one('team.analytic.line')
    analytic_acc = fields.Many2one('account.analytic.account', 'Analytic Account')
    debit_line_team = fields.Float('Debit', related='analytic_acc.ann_account_debit', stored=True)
    credit_line_team = fields.Float('Credit', related='analytic_acc.ann_account_credit', stored=True)
    balance_line_team = fields.Float('Balance', related='analytic_acc.ann_account_balance', stored=True)

    name = fields.Char('Name')
    date_data = fields.Datetime('Date')
    amount = fields.Float('Amount')
    unit_amm = fields.Float('Unit Amount')
    acc_id = fields.Integer('Account Id')

    @api.onchange('analytic_acc')
    def _onchange_fetch_analytic_acc_line(self):
        for rec in self:
            get_id = rec.analytic_acc.line_ids
            for pass_data in get_id:
                pass_value = self.connection
                pass_value.create({
                    'connection_id': rec.analytic_acc.id,
                    'analytic_id': pass_data.id,
                    'name': pass_data.name,
                    'date': pass_data.date,
                    'amount': pass_data.amount,
                    'unit_amount': pass_data.unit_amount,
                })
                return pass_value


class AnalyticLine(models.Model):
    _name = 'team.analytic.line'
    _description = 'Team Pacific Corp Analytic Line'

    team_profit_loss_conn = fields.Many2one('team.profit.loss')
    connection_id = fields.Many2one('account.analytic.account')
    analytic_id = fields.Integer()

    @api.model
    def _default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    name = fields.Char('Description', required=True)
    date = fields.Date('Date', required=True, index=True, default=fields.Date.context_today)
    amount = fields.Monetary('Amount', required=True, default=0.0)
    unit_amount = fields.Float('Quantity', default=0.0)
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure',
                                     domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_uom_id.category_id', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Partner',
                                 domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    user_id = fields.Many2one('res.users', string='User', default=_default_user)
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one(related="company_id.currency_id", string="Currency", readonly=True, store=True,
                                  compute_sudo=True)






















