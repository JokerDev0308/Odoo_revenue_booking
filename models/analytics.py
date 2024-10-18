# models/analytics.py

from odoo import models, fields, api

class VenueAnalytics(models.Model):
    _name = 'venue.analytics'
    _description = 'Analytics for venue bookings and revenue'

    venue_id = fields.Many2one('venue.booking', string="Venue")
    total_revenue = fields.Float("Total Revenue")
    total_bookings = fields.Integer("Total Bookings")
    report_date = fields.Date("Report Date", default=fields.Date.today())

    @api.model
    def generate_report(self):
        # Logic for generating analytics report
        venues = self.env['venue.booking'].search([])
        for venue in venues:
            bookings = self.env['venue.booking.reservation'].search([('venue_id', '=', venue.id)])
            total_revenue = sum(booking.price for booking in bookings)
            total_bookings = len(bookings)

            # Create or update analytics record
            self.create({
                'venue_id': venue.id,
                'total_revenue': total_revenue,
                'total_bookings': total_bookings,
            })

        return True
