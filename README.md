# flask_d3_example

## Dependencies

* create conda env with:

        $ conda env create -f env.yml

* then activate:

        S source activate flask-d3-example

## Run

    $ python run.py


### The Problem

* Navigate to: [http://127.0.0.1:5000/get-data](http://127.0.0.1:5000/get-data)
* you will see some simple json data served
* but when I try to pick this data up with `d3.json` (see `static/js/data.js`):
    * I get a CORS error (this is actually better than what i was experiencing before, which was no error and no data, so lets just see what we can do from here)
