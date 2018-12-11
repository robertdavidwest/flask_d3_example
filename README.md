# flask_d3_example

## Dependencies

* create conda env with:

        $ conda env create -f env.yml

* then activate:

        S source activate flask-d3-example

## Run the WebApp

    $ python run.py


### The Problem

* Navigate to: [http://127.0.0.1:5000/get-data](http://127.0.0.1:5000/get-data)(you will see some simple json data served):

        {
          "a": 1, 
          "b": 2
        }
    
    as expected from the backend:
   
        @app.route("/get-data")
        def get_data():
            return jsonify({"a": 1, "b": 2})

* but when I try to pick this data up with `d3.json` (in `static/js/data.js`) nothing seems to happen. I try logging it and writing it to a div, neither is successful and no errors show in the console:

        static/js/data.js
        ---
        d3.json("http://127.0.0.1:5000/get-data",
          function(d){
          console.log(d);
           document.getElementById("d3-write-here").innerHTML = d;
        })


