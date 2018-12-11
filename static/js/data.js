
d3.json("http://127.0.0.1:5000/get-data",
    function(d){
        console.log(d);
        document.getElementById("d3-write-here").innerHTML = d;
    })
