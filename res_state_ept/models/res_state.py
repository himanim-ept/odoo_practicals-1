from odoo import fields, models, api


class State(models.Model):
    _name = "res.state.ept"
    _description = "This is my state module"

    state_name = fields.Char(string="State_Name", help="Enter State Name")
    state_code = fields.Char(string="State_Code", help="Enter State Code")
    country_name = fields.Char(string="Country_Name", copy=False, help="Enter Country Name")
    active = fields.Boolean(string="Active", help="Select if active")
