.. image:: https://travis-ci.com/eric-s-s/bind_json_error_handlers.svg?branch=master
    :target: https://travis-ci.com/eric-s-s/bind_json_error_handlers

.. image:: https://coveralls.io/repos/github/eric-s-s/bind_json_error_handlers/badge.svg?branch=master
    :target: https://coveralls.io/github/eric-s-s/bind_json_error_handlers?branch=master


bind_json_error_handlers
========================

This binds json error handlers to a Flask so that any error generated is handled as
a json response


To install:

.. code-block:: bash

    $ pip install git+https://github.com/eric-s-s/bind_json_error_handler

or:

.. code-block:: bash

    $ git clone https://github.com/eric-s-s/bind_json_error_handler
    $ cd sentences
    $ python setup.py install  # or pip install .


to use:

.. code-block:: python

    from bind_json_error_handler import bind_json_error_handler
    app = Flask(__name__)
    bind_json_error_handler(app)

the end.