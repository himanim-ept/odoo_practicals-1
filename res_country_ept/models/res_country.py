from odoo import fields, models, api


class Country(models.Model):
    _name = "res.country.ept"
    _description = "This is country module"

    name = fields.Char(string="Name", help="Enter Name")
    short_country = fields.Char(string="Short_Country", help="Enter Short_Country code")
    active = fields.Boolean(string="Active", help="Select if active")
