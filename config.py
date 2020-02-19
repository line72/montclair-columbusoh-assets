# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'columbusoh',
    package_name = 'montclair-columbusoh',
    name = 'Go Columbus',
    description = 'Real Time Tracking of the Buses for Columbus, OH',
    url = 'https://columbusoh.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.7.6',
        revision = 1,
        title = 'Go Columbus',
        first_run_text = "Welcome to Columbus, OH's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 2,
        app_id = 'com.gotransitapp.columbusoh',
        app_store_id = 'REPLACE_ME',
        app_store_url = 'https://apps.apple.com/us/app/REPLACE_ME'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 2,
        app_id = 'com.gotransitapp.columbusoh',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.columbusoh'
    )
)
