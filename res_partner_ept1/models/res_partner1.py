from odoo import fields, models, api


class ResPartner(models.Model):
    _name = 'res.partner1.ept'
    _description = 'This is my second module'

    name = fields.Char(string='Name', required=True, help="Enter Name")
    street1 = fields.Char(string='Street1', help="Enter street1")
    street2 = fields.Char(string='Street2', help="Enter street2")
    city = fields.Char(string='City', help="Enter City")
    state = fields.Char(string='State', help="Enter State")
    zip_code = fields.Char(string='Zip_Code', help="enter zip_code")
    country = fields.Char(string='Country', help="Enter Country Name")
    birthdate = fields.Date(string='Birth Date', help="Enter Birthdate")
    age = fields.Integer(string='Age', help="Enter Age")
    weight = fields.Float(string='Weight', help="Enter weight")
    description = fields.Text(string='Description', help="Enter Description")
    gender = fields.Selection([('Male', 'Male'),
                               ('Female', 'Female'),
                               ('Transgender', 'Transgender')], help="Select Gender")
    details = fields.Html(string='Details', help="Enter Details")
    is_sepctacles = fields.Boolean(string='is_Sepctacles', help="Select if you have sepctacles")

