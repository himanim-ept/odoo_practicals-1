from odoo import fields, models, api


class Lead(models.Model):
    _name = "crm.lead.ept"
    _description = "This module is for lead generation"

    name = fields.Char(string="Name", required=True, help='Enter name of customer')
    email = fields.Char(string="Email", required=True, help='Enter email Id of customer')
    customer_contact = fields.Char(string="Customer Contact", required=True, help='Enter contact of customer')
    expected_revenue = fields.Float(string="Expected revenue", digit=(6, 2), help='Enter expected revenue of customer')
    sales_person = fields.Char(string="Sales Person", required=True, help='Enter name of sales person')
    sales_team = fields.Char(string="Sales Team", help='Enter name of sales team')
    campaign = fields.Char(string="Campaign", help='Enter name of campaign')
    channel = fields.Selection([('Facebook', 'Facebook'),
                                ('WhatsApp', 'WhatsApp'),
                                ('Email', 'Email'),
                                ('Newspaper', 'Newspaper'),
                                ('Television', 'Television'),
                                ('Phone Call', 'Phone Call'),
                                ('SMS', 'SMS'),
                                ('Google Ads', 'Google Ads')], required=True, help='Select anyone channel from given')
    state = fields.Selection([('New', 'New'),
                              ('Qualified', 'Qualified'),
                              ('Proposition', 'Proposition'),
                              ('Won', 'Won'),
                              ('Lost', 'Lost')], default="New", help='Select anyone state')
    follow_up_date = fields.Date(string="follow_up_date", required=True, help='Mark date from calender')
    won_date = fields.Date(string="Won Date", help='Select winning date of campaign from calender')
    lost_reason = fields.Text(string="Lost Reason", help='Enter the reason for loss achieved from campaign')
