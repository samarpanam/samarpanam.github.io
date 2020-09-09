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
        'events': 'Events',
        'about': 'About',
        'members': 'Members',
        'contact': 'Contact'
    }
}

###############################################################################

pages = {}

pages['index'] = {
    'title': 'samarpaṇam (समर्पणम्) is a group of Sanskrit-minded people',
}

pages['events'] = {
    'title': 'Events',
    'events': [
        {'name': 'Conclave', 'venue': 'Internet', 'date': '27th September, 2020 (Saturday)', 'time': '9:30am-12:30pm'},
        #{'name': 'Event 2', 'venue': 'TBD', 'time': '8pm'}
    ],
    'show_events': True
}

pages['about'] = {
    'title': 'Mission and Vision',
    'mission': 'Mission',
    'vision': 'Vision',
}

pages['members'] = {
    'title': 'Members',
    'members': [
        {'name': 'Anil Gourishetty', 'email': 'abc@abc.com', 'institution': 'IIT Roorkee'},
        {'name': 'Anuradha Choudry', 'email': 'abc@abc.com', 'institution': 'IIT Kharagpur'},
        {'name': 'Anway Mukhopadhyay', 'email': 'abc@abc.com', 'institution': 'IIT Kharagpur'},
    ],
    'subtitle': 'Advisory Board',
    'mentors': [
        {'name': 'Ramasubramanian', 'email': 'abc@abc.com', 'institution': 'IIT Bombay'},
        {'name': 'Shrinivasa Varakhedi', 'email': 'abc@abc.com', 'institution': 'Kaviguru'},
    ]
}

pages['contact'] = {
    'title': 'Contact',
    'contacts': [
        {'name': 'ABC', 'email': 'abc@abc.com', 'institution': 'Institute'},
    ]
}

###############################################################################
