from odoo import fields, models, api


class Product(models.Model):
    _name = "product.ept"
    _description = "This module is for Product"

    name = fields.Char(string="Name", help='Enter name of product')
    sku = fields.Char(string="SKU", help='Enter sku of product')
    barcode = fields.Char(string="Barcode", help='Enter barcode of product')
    can_product_sold = fields.Boolean(string="Can_Product_Sold", help='Mark if product cab be sold')
    product_type = fields.Selection([('Storable', 'Storable'),
                                     ('Consumbale', 'Consumbale'),
                                     ('Service', 'Service')], help='Select the product type from below')
    sale_price = fields.Float(string="Sale_Price", digit=(6, 2), help='Enter sale_price of product')
    cost_price = fields.Float(string="Cost_Price", digit=(6, 2), help='Enter cost_price of product')
    active = fields.Boolean(string="Active",help='Select if order is active')
    warehouse = fields.Char(string="Warehouse", help='Enter Warehouse Name')
    image = fields.Image(string="Product Image", help='Upload Image')
    web_description = fields.Html(string="Website Description", help='Write website Description')
    internal_notes = fields.Text(string="Internal Notes", help='write internal notes')

