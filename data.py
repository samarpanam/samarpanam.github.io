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
        #'contact': 'Contact'
    }
}

###############################################################################

phrases = {
    'name': 'समर्पणम्',
    'expansion': 'संस्कृताय अर्पणम्'
}

###############################################################################

pages = {}

pages['index'] = {
    'title': f'iast({phrases["name"]}) ({phrases["name"]})',
    'body': (
        'A group of Sanskrit-minded individuals from technological institutes '
        'whose aim is to revive the culture of studying technical content '
        'written in or using Sanskrit.<br>'
        f'The term \'iast({phrases["name"]}) ({phrases["name"]})\' is formed '
        f'of two words <span class="font-italic">iast({phrases["expansion"]}) '
        f'({phrases["expansion"]})</span> that means dedicating to/for '
        'the sake of Samskrit.'
    )
}

pages['events'] = {
    'title': 'Events',
    'events': [
        {'name': 'Conclave', 'venue': 'Webex', 'date': '27th September, 2020 (Sunday)', 'time': '5:00pm-8:00pm'},
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
        {'name': 'Anil Kumar Gourishetty', 'email': 'abc@abc.com', 'institution': 'IIT Roorkee'},
        {'name': 'Anuradha Choudry', 'email': 'abc@abc.com', 'institution': 'IIT Kharagpur'},
        {'name': 'Anway Mukhopadhyay', 'email': 'abc@abc.com', 'institution': 'IIT Kharagpur'},
        {'name': 'Arnab Bhattacharya', 'email': 'abc@abc.com', 'institution': 'IIT Kanpur'},
        {'name': 'G S Murthy', 'email': 'abc@abc.com', 'institution': 'IIT Indore'},
        {'name': 'Ganesh Ramakrishnan', 'email': 'abc@abc.com', 'institution': 'IIT Bombay'},
        {'name': 'Nomesh Bolla', 'email': 'abc@abc.com', 'institution': 'IIT Delhi'},
        {'name': 'Prathosh', 'email': 'abc@abc.com', 'institution': 'IIT Delhi'},
        {'name': 'Ravi Kiran', 'email': 'abc@abc.com', 'institution': 'IIIT Hyderabad'},
        {'name': 'Venkateswara Pai', 'email': 'abc@abc.com', 'institution': 'IISER Pune'},
    ],
    'subtitle': 'Advisory Board',
    'mentors': [
        {'name': 'K Ramasubramanian', 'email': 'abc@abc.com', 'institution': 'IIT Bombay'},
        {'name': 'M D Srinivas', 'email': 'abc@abc.com', 'institution': 'Centre for Policy Studies, Chennai'},
        {'name': 'Srinivasa Varakhedi', 'email': 'abc@abc.com', 'institution': 'Kavikulaguru Kalidas Sanskrit University'},
        {'name': 'Subhash Kak', 'email': 'abc@abc.com', 'institution': 'Oklahoma State University, USA'},
    ]
}

pages['contact'] = {
    'title': 'Contact',
    'contacts': [
        {'name': 'ABC', 'email': 'abc@abc.com', 'institution': 'Institute'},
    ]
}

###############################################################################
