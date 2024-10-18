from odoo import models, fields, api

class Venue(models.Model):
    _name = 'venue.booking'
    _description = 'Venue Management'

    name = fields.Char("Venue Name", required=True)
    location = fields.Char("Location", required=True)
    google_map_url = fields.Char("Google Map URL")
    sports_facilities = fields.One2many('venue.sport', 'venue_id', string="Sports Facilities")
    pricing = fields.One2many('venue.pricing', 'venue_id', string="Pricing")
    owner_id = fields.Many2one('res.users', string="Venue Owner")
    status = fields.Selection([('pending', 'Pending'), ('approved', 'Approved')], default='pending')

    @api.model
    def approve_venue(self):
        self.status = 'approved'
