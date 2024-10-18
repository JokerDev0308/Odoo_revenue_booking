# controllers/booking_controller.py

from odoo import http
from odoo.http import request

class BookingController(http.Controller):

    @http.route('/booking/confirm', type='http', auth="user", website=True, methods=['POST'])
    def confirm_booking(self, **kwargs):
        venue_id = kwargs.get('venue_id')
        booking_date = kwargs.get('booking_date')
        sport_id = kwargs.get('sport_id')
        duration = kwargs.get('duration')

        # Creating the booking record
        booking_vals = {
            'venue_id': int(venue_id),
            'user_id': request.env.user.id,
            'booking_date': booking_date,
            'sport': int(sport_id),
            'duration': float(duration),
        }

        # Calling the booking model to create the booking
        booking = request.env['venue.booking.reservation'].create(booking_vals)

        # Redirecting to a success page
        return request.redirect('/booking/success')

    @http.route('/booking/success', type='http', auth="user", website=True)
    def booking_success(self, **kwargs):
        return request.render('venue_booking.booking_success_template', {})
