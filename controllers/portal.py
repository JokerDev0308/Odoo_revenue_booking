from odoo import http
from odoo.http import request

class BookingPortal(http.Controller):

    @http.route('/venue_booking', type='http', auth="user", website=True)
    def venue_booking(self, **kwargs):
        venues = request.env['venue.booking'].search([])
        return request.render('venue_booking.venue_templates', {'venues': venues})

    @http.route('/venue/<model("venue.booking"):venue>/', type='http', auth="user", website=True)
    def venue_details(self, venue, **kwargs):
        return request.render('venue_booking.venue_detail_template', {'venue': venue})

    @http.route('/booking/confirm', type='http', auth="user", website=True)
    def booking_confirm(self, venue_id, date, sport_id, duration, **kwargs):
        booking_vals = {
            'venue_id': venue_id,
            'user_id': request.env.user.id,
            'booking_date': date,
            'sport': sport_id,
            'duration': duration,
        }
        booking = request.env['venue.booking.reservation'].create(booking_vals)
        return request.redirect('/booking/success')
