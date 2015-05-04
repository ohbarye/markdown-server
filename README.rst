===============
Markdown Server
===============

Markdown-server is a simple web application.
It converts markdown file to HTML and response by `text/html`.

How to use
==========

--------------------
Runtime Environment
--------------------

:Python:        2.7.9
:pip:           6.1.1
:virtualenv:    12.1.1


--------------------
Library Dependencies
--------------------

See `requirements.txt`.

--------
Just try
--------

Start server
------------

You don't need any special preparation to try to start server. Just execute below comands.

::

    $ git clone https://github.com/ohbarye/markdown-server
    $ cd markdown-server
    $ virtualenv .venv
    $ source .venv/bin/activate
    (.venv)$ pip install -r requirements.txt
    (.venv)$ mdsvr
        Bottle v0.12.8 server starting up (using WSGIRefServer())...
        Listening on http://localhost:8009/

If server start up successfully, browse below URL and check the converted result.

::

    $ open http://localhost:8009/sample.md

Only Conversion
---------------

Additionally, You can use the conversion function alone.

::

    (.venv)$ convert source_md_file target_html_file

--------------
Do as you like
--------------

- Markdown server purvey `http://host/[file_name]` URL. This corresponds to `resources/markdown/[file_name]`.You can put any markdown file here.

- Converted file will be placed to `resources/html` directory. Generated html file includes CSS so it's ease to distribute.

- Environment variables like *host name* or *port number* are set in `env.py`. Edit arbitrarily.

    ::

        ms_port        = '8009'
        ms_host        = 'localhost'


- The default markdown engine is Github flavored Markdown. If you want to use another style, add CSS and edit `env.py`.

    ::

        css_name       = 'github.css'
        markdown_type  = 'gfm'
