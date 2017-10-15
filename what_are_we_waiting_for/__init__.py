"""
what_are_we_waiting_for - Our Opal Application
"""
from opal.core import application


class Application(application.OpalApplication):
    javascripts = [
        'js/what_are_we_waiting_for/routes.js',
        'js/opal/controllers/discharge.js',
        'js/what_are_we_waiting_for/request_receive.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/what_are_we_waiting_for/flow.js',
    ]
