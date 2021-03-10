{
    'name': "Lead",
    'version': "0.1",
    'category': "crm_lead",
    'depends': ['base'],
    'data': [
        'security/crm_lead_ept.xml',
        'security/ir.model.access.csv',
        'views/view_lead.xml'
    ],
    'installable': True,
    'auto_install': False,
    'description': "This module is for crm_lead"
}
