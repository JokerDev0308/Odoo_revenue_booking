# models/employee.py

from odoo import models, fields

class VenueEmployee(models.Model):
    _name = 'venue.employee'
    _description = 'Employee Management for venue owners'

    name = fields.Char("Employee Name", required=True)
    email = fields.Char("Email", required=True)
    mobile = fields.Char("Mobile Number", required=True)
    active = fields.Boolean("Active", default=True)
    venue_id = fields.Many2one('venue.booking', string="Venue")

    def deactivate_employee(self):
        # Logic to deactivate an employee
        self.active = False

    def activate_employee(self):
        # Logic to activate an employee
        self.active = True
