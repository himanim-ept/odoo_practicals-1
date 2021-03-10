from odoo import fields, models, api


class City(models.Model):
    _name = "res.city.ept"
    _description = "This module is for city"

    city_name = fields.Char(string="City Name", help="Enter city name")
    state_name = fields.Char(string="State Name", copy=False, help="Enter state Name")
    active = fields.Boolean(string="Active", help="Seelect if active")
