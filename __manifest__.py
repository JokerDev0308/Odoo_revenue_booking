{
    'name': 'Venue Booking System',
    'version': '1.0',
    'depends': ['base', 'web', 'portal'],
    'data': [
        'views/venue_templates.xml',
        'views/booking_templates.xml',
        'views/analytics_templates.xml',
        'views/portal_templates.xml',
        'views/employee_templates.xml',
    ],
    'installable': True,
    'application': True,
}
