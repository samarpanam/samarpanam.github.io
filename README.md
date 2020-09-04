# samarpanam.github.io
Website for Samarpaṇam

## Build Instructions

### Build Requirements

`pip3 install Jinja2 indic_transliteration`

### Structure

HTML Jinja2 template for a page `sample.html` should be put in `src/` directory with the same file name (`sample.html`).
Data for page `sample.html` should be put in the `data.py` file, in the `pages` object. `title` field is used to show title in the header.


### Build
Add the pages that you want to build to the list `build` in `config.py` and run `python3 build.py`
To launch the page, you can also run `python3 build.py --launch`
Pages to build can also be specified as a command line argument to `build.py`, i.e., `python3 build.py --page index contact`

## Custom Site Builder

Static pages can be built by any alternative procedure, be it other static site builder or manual.
Only requirement is that output pages should be put in the `www` directory for the `publish.sh` method to work.

## Publish

Once the website is ready and commit is made, run the file `publish.sh`.
This will push the `www` directory from `master` branch to the root of `gh-pages` branch, which is used to render the website.

