from odoo import models, fields, api


class AddressBook(models.Model):
    _name = 'address.book'
    _description = ''

    name = fields.Char(string='Name', required=True, help="Enter your name ")
    city = fields.Char(string='City', help='Enter name of your city')
    state = fields.Char(string='State', help='Enter name of your state')
