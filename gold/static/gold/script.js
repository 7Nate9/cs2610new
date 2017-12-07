var submit = document.querySelector("#submitWeight");
submit.addEventListener("click", submitRequest());
submit.addEventListener("keypress", function(event){
    if (event.which == 13 || event.which == 32)
        submitRequest();
});

function submitRequest(){
    var startDate = Date.now();
    var fiveDays = (24*60*60*1000) * 5;
    startDate.setTime(startDate.getTime() - fiveDays);
    
    var endDate = Date.now();
    
    var start = startDate.toJSON();
    var end = endDate.toJSON();
    
    var apiKey = "tyByYiu5iQZxpDxC1aXT";
    
    var goldRUrl = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=" + apiKey + "&column_index=2&start_date=" + start + "&end_date=" + end;
}