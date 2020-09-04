#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 09:21:07 2020

@author: Hrishikesh Terdalkar
"""

###############################################################################

site = {
    'title': 'samarpaṇam (समर्पणम्)',
    'copyright': 'samarpaṇam',
    'navigation': {
        'index': 'Home',
        'about': 'About',
        'contact': 'Contact'
    }
}

###############################################################################

pages = {}

pages['index'] = {
    'title': '',
    'events': [
        {'name': 'Conclave', 'venue': 'Internet', 'date': '12th September, 2020 (Saturday)', 'time': '9:30am-12:30pm'},
        #{'name': 'Event 2', 'venue': 'TBD', 'time': '8pm'}
    ],
    'show_events': True
}

pages['contact'] = {
    'title': 'Contact',
    'contacts': [
        {'name': 'ABC', 'email': 'abc@abc.com', 'institution': 'Institute'},
    ]
}

pages['about'] = {
    'title': 'samarpaṇam (समर्पणम्) is a group of Sanskrit-minded people',
}

###############################################################################
