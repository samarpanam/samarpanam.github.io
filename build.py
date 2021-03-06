#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 00:14:28 2020

@author: Hrishikesh Terdalkar
"""

import re
import os

import jinja2
from indic_transliteration.sanscript import transliterate, DEVANAGARI, IAST

import config
import data

###############################################################################


def re_iast(matchobj):
    return transliterate(matchobj.group(1), DEVANAGARI, IAST)


def re_devangari(matchobj):
    return transliterate(matchobj.group(1), IAST,  DEVANAGARI)


def filter_devanagari(input_text):
    start = r"devanagari("
    end = r")"
    pattern = "%s(.*?)%s" % (re.escape(start), re.escape(end))
    return re.sub(pattern, re_iast, input_text, flags=re.DOTALL)


def filter_iast(input_text):
    start = r"iast("
    end = r")"
    pattern = "%s(.*?)%s" % (re.escape(start), re.escape(end))
    return re.sub(pattern, re_iast, input_text, flags=re.DOTALL)


def devanagari(text):
    return transliterate(text, IAST, DEVANAGARI)


def iast(text):
    return transliterate(text, DEVANAGARI, IAST)


###############################################################################
# Jinja2 Templates

environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.abspath(os.path.join('.', config.source_dir))
    )
)

###############################################################################
# Register Filters

environment.filters['devanagari'] = filter_devanagari
environment.filters['iast'] = filter_iast

###############################################################################


def render_page(page, **kwargs):
    global environment
    template_path = f'{page}.html'
    template = environment.get_template(template_path)
    return template.render(data=data.pages[page], active_page=page, **kwargs)


def build_website(pages, **kwargs):
    if pages:
        print(f"Building {len(pages)} pages ...")
        for page in pages:
            output_path = os.path.join(config.output_dir, f'{page}.html')
            html = render_page(page, **kwargs)
            with open(output_path, 'w') as f:
                f.write(html)
            print(f"Built '{page}'.")
    else:
        print("Nothing to build.")


###############################################################################

if __name__ == '__main__':
    import argparse
    desc = "Build static website"

    p = argparse.ArgumentParser(description=desc)
    p.add_argument("--page", action='append',
                   help="Page(s) to build", default=config.build)
    p.add_argument("--launch", action='store_true',
                   help="Launch")
    args = vars(p.parse_args())

    build_website(args['page'], site=data.site)
    if args['launch']:
        import http.server
        import webbrowser

        os.chdir(config.output_dir)
        server_address = ('localhost', 8000)
        local_server = f'http://{server_address[0]}:{server_address[1]}/'
        webbrowser.open(local_server)
        print(f"Launching {local_server} ...")

        httpd = http.server.HTTPServer(server_address,
                                       http.server.SimpleHTTPRequestHandler)
        httpd.serve_forever()
