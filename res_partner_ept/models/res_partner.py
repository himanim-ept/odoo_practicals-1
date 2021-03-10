from odoo import models, fields, api


class ResPartner(models.Model):
    _name = 'res.partner.ept'
    _description = 'This is my first module'

    name = fields.Char(string='Name', required=True, help="enter Name")
    street1 = fields.Char(string='street1', help="Enter Street1")
    street2 = fields.Char(string='street2', help="Enter street2")
    city = fields.Char(string='City', help="Enter City")
    state = fields.Char(string='State', help="Enter State")
    zip_code = fields.Char(string='zip_code', help="enter zip_code")
    country = fields.Char(string='Country', help="Enter Country Name")
    birthdate = fields.Date(string='BirthDate', help="Enter Birthdate")
    age = fields.Integer(string='Age', help="Enter Age")
    weight = fields.Float(string='Weight', help="Enter weight")
    description = fields.Text(string='Description', help="Enter Description")
    gender = fields.Selection([('Male', 'Male'),
                               ('Female', 'Female'),
                               ('Trasgender', 'Transgender')], help="Select Gender")
    details = fields.Html(string='Details', help="Enter Details")
    is_sepctacles = fields.Boolean(string='is_Sepctacles', help="Select if you have sepctacles")
