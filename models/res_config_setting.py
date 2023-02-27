from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _find_default_analytic_id(self):
        analytic_var = self.env.ref('team.profit.loss.v2', False)
        return analytic_var

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        alias = self._find_default_analytic_id()
        res.update(
            crm_alias_prefix=alias.alias_name if alias else False,
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        alias = self._find_default_lead_alias_id()
        if alias:
            alias.write({'alias_name': self.crm_alias_prefix})
        else:
            self.env['mail.alias'].with_context(
                alias_model_name='crm.lead',
                alias_parent_model_name='crm.team').create({'alias_name': self.crm_alias_prefix})

        for team in self.env['crm.team'].search([]):
            team.alias_id.write(team.get_alias_values())