from odoo import models, fields

class User(models.Model):
    _inherit = 'res.users'

    mobile_verified = fields.Boolean("Mobile Verified", default=False)
    email_verified = fields.Boolean("Email Verified", default=False)
    otp_sent = fields.Char("OTP Sent")

    def send_otp(self):
        # Logic to send OTP to the user via WhatsApp
        pass

    def verify_otp(self, otp):
        if otp == self.otp_sent:
            self.mobile_verified = True
            self.email_verified = True
        else:
            raise ValidationError('Invalid OTP!')
