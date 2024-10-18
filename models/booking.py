from odoo import models, fields, api

class Booking(models.Model):
    _name = 'venue.booking.reservation'
    _description = 'Booking Management'

    venue_id = fields.Many2one('venue.booking', string="Venue", required=True)
    user_id = fields.Many2one('res.users', string="Booked By", required=True)
    booking_date = fields.Datetime("Booking Date", required=True)
    sport = fields.Many2one('venue.sport', string="Sport", required=True)
    duration = fields.Float("Duration (hours)", required=True)
    price = fields.Float("Price", compute='_compute_price')

    @api.depends('venue_id', 'sport', 'duration')
    def _compute_price(self):
        # Pricing logic based on venue and sport selection
        for record in self:
            pricing = record.venue_id.pricing.filtered(lambda p: p.sport_id == record.sport)
            record.price = pricing.price_per_hour * record.duration

    @api.model
    def create_booking(self, vals):
        # Logic to check venue availability and create booking
        venue = self.env['venue.booking'].browse(vals['venue_id'])
        if self.check_availability(venue, vals['booking_date']):
            return super(Booking, self).create(vals)
        else:
            raise UserError('Venue is not available at the selected time!')

    def check_availability(self, venue, booking_date):
        # Custom logic to check if the venue is available at the given date and time
        bookings = self.search([('venue_id', '=', venue.id), ('booking_date', '=', booking_date)])
        return not bookings
