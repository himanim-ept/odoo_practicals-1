{
    'name': "Res State",
    'version': "0.1",
    'category': "state",
    'depends': ['sales_team'],
    'data': ['security/ir.model.access.csv',
             'views/view_res_state.xml',
             'data/res_state_demo_data.xml'],
    'installable': True,
    'auto_install': False,
    'description': 'This module is for state'
}