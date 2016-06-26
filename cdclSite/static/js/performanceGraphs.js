function drawPerformanceBarChart(drawTo, w, h, margin, results) {

    var width = w - margin.left - margin.right;
    
    var height = h - margin.top - margin.bottom;
    
    var xScale = d3.scale.ordinal().rangeRoundBands([0, width], 0.1);
    
    var yScale = d3.scale.linear().range([height, 0]);
    
    var xAxis = d3.svg.axis().scale(xScale).orient("bottom");
    
    var yAxis = d3.svg.axis().scale(yScale).orient("left");
    
    
    var svg = d3.select(drawTo)
        .append("svg")
            .attr("class", "graphSVG")
            .attr("id", "barGraphSVG")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    
    
    
    
    xScale.domain(["wins", "losses", "draws"]);
    
    var maxResult = 0;
    
    if (results["wins"] > maxResult) {
        maxResult = results["wins"];
    }
    
    if (results["losses"] > maxResult) {
        maxResult = results["losses"];
    }
    
    if (results["draws"] > maxResult) {
        maxResult = results["draws"];
    }
    
    
    yScale.domain([0, maxResult + 3]);
    

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .style("font-size","20px")
        .call(xAxis);

    
    svg.append("g")
        .attr("class", "y axis")
        .style("font-size","18px")
        .call(yAxis)
        .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .style("font-size","20px")
            .text("Games");
    
    
    svg.append("rect")
        .attr("class", "performanceBar")
        .attr("id", "winsBar")
        .attr("x", xScale("wins"))
        .attr("width", xScale.rangeBand())
        .attr("y", yScale(results["wins"]))
        .attr("height", function() {return (height - yScale(results["wins"]))})
        .style("fill", "#7bc8a4");
    
    
    svg.append("rect")
        .attr("class", "performanceBar")
        .attr("id", "lossesBar")
        .attr("x", xScale("losses"))
        .attr("width", xScale.rangeBand())
        .attr("y", yScale(results["losses"]))
        .attr("height", function() {return (height - yScale(results["losses"]))})
        .style("fill", "#f16745");
    
    
    svg.append("rect")
        .attr("class", "performanceBar")
        .attr("id", "drawsBar")
        .attr("x", xScale("draws"))
        .attr("width", xScale.rangeBand())
        .attr("y", yScale(results["draws"]))
        .attr("height", function() {return (height - yScale(results["draws"]))})
        .style("fill", "#ffc65d");
    
    
    svg.append("text")
        .attr("class", "graphTitle")
        .attr("id", "cumulativePerformanceTitle")
        .attr("x", (width / 2))    
        .attr("y", 5 - (margin.top / 2))
        .attr("text-anchor", "middle")   
        .text("CUMULATIVE RESULTS");

}



function drawPerformanceLineGraph(drawTo, w, h, margin, results) {
    
    var width = w - margin.left - margin.right;
    var height = h - margin.top - margin.bottom;
    
    var xScale = d3.scale.linear().range([0, width]);
    var yScale = d3.scale.linear().range([height, 0]);
    
    
    // Define the axes
    var xAxis = d3.svg.axis().scale(xScale)
        .orient("bottom");

    var yAxis = d3.svg.axis().scale(yScale)
    .orient("left");

    // Define the line
    var valueline = d3.svg.line()
        .x(function(d) { return xScale(d.gameNumber); })
        .y(function(d) { return yScale(d.opponentRating); });

    // Adds the svg canvas
    var svg = d3.select(drawTo)
        .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform", 
                "translate(" + margin.left + "," + margin.top + ")");
    
    xScale.domain(d3.extent(results["seriesA"], function(d) { return d.gameNumber; }));
    yScale.domain([0, d3.max(results["seriesA"], function(d) { return d.opponentRating; })]);
    
    // Add the valueline path.
    svg.append("path")
        .attr("class", "line")
        .attr("d", valueline(results["seriesA"]));

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    
}