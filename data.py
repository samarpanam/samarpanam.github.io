#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 09:21:07 2020

@author: Hrishikesh Terdalkar
"""

###############################################################################

site = {
    'title': 'Samarpaṇam',
    'copyright': 'Samarpaṇam',
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
        {'name': 'Event 1', 'venue': 'Internet', 'time': '7pm'},
        {'name': 'Event 2', 'venue': 'TBD', 'time': '8pm'}
    ],
    'show_events': True
}

pages['contact'] = {
    'title': 'Contact',
    'contacts': [
        {'name': 'ABC', 'email': 'abc@abc.com'},
        {'name': 'XYZ', 'email': 'xyz@xyz.com'},
    ]
}

pages['about'] = {
    'title': 'About'
}

###############################################################################
