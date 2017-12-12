function setHandlers(){
    var submit = document.querySelector("#submitWeight");
    submit.addEventListener("click", submitRequest);
    submit.addEventListener("keypress", function(event){
        if (event.which == 13 || event.which == 32)
            submitRequest();
    });
}

function submitRequest(){
    var startTime = Date.now();
    var fiveDays = (24*60*60*1000) * 5;
    startTime -= fiveDays;
    var startDate = new Date();
    startDate.setTime(startTime);
    
    var endDate = new Date();
    endDate.setTime(Date.now());
    
    var start = startDate.toJSON();
    var end = endDate.toJSON();
    
    var apiKey = "tyByYiu5iQZxpDxC1aXT";
    
    var goldRUrl = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=" + apiKey + "&column_index=2&start_date=" + start + "&end_date=" + end;
    
    var request = new XMLHttpRequest();
    request.open("GET", goldRUrl, false);
    request.send(null);
    
    var jsonResponse = JSON.parse(request.responseText);
    var dataset = jsonResponse.dataset;
    var data = dataset.data;
    var price = data[0][1];
    
    var unitconvURL = "/goldconvert/?from=" + document.getElementById("fromUnit").value + "&to=t_oz&value=" + document.getElementById("weight").value;
    request = new XMLHttpRequest;
    request.open("GET", unitconvURL, false);
    request.send(null);
    
    jsonResponse = JSON.parse(request.responseText);
    var endWeight = jsonResponse.value;
    
    var value = (price * endWeight).toFixed(2);
    
    document.getElementById("results").innerHTML = "<h2>Results</h2><p>You're worth $"+ value +"! Congratulations!</p>"
}

function test(){
    alert("Testing");
}