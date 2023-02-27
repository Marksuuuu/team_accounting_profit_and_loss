#John Raymark LLavanes
#MIS - 2k23
{
    'name': 'Team Pacific Corporation Accounting Module (PROFIT AND LOSS)',
    'version': '0.1',
    'category': 'Accounting Extensions',
    'summary': 'Accounting Customization For Odoo 13',
    'sequence': '10',
    'author': 'John Raymark LLavanes - 10450',
    'company': 'Team Pacific Corporation',
    'maintainer': 'MIS - LOC 267',
    'support': 'mis@teamglac.com',
    'website': '',
    'depends': ['account'],
    'live_test_url': '',
    'demo': [],
    'data': [
        #Security
        'security/ir.model.access.csv',

        # Views
        'views/team_accounting_profit_and_loss_view_menu.xml',
        'views/team_accounting_profit_and_loss_view.xml',
        'views/team_accounting_profit_and_loss_view_v2.xml',
        'views/analytic_account_view.xml',

        #Reports


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [

    ],

}
