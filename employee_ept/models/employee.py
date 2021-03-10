from odoo import fields, models, api


class Employee(models.Model):
    _name = "employee.ept"
    _description = "This module is for Employee"

    name = fields.Char(string="Employee Name", help='Enter name of employee')
    department = fields.Char(string="Department Name", help='Enter department of employee')
    job_position = fields.Char(string="Job Position of Employee", help='Enter job position of employee')
    salary = fields.Float(string="Salary", digits=(6, 2), help='Enter salary of employee')
    hire_date = fields.Date(string="Hire Date", help='Select hire date of employee from calender')
    gender = fields.Selection([('Male', 'Male'),
                               ('Female', 'Female'),
                               ('Transgender', 'Transgender')], help='Select gender from below')
    job_type = fields.Selection([('Permanent', 'Permanent'),
                                 ('Ad Hoc', 'Ad Hoc')], help='Select job type from below')
