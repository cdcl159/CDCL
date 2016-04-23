function drawBlockGraph(drawTo, graphData, width, height, colorScheme, title, xLabel, yLabel, margin) {

    
    
    var tip = d3.tip()
        .attr('class', 'd3-tip')
        .offset([-10, 0])
        .html(function(d) {
            var nameHTMLString = "<strong>Opponent:</strong> <span style='color:red'>" + $(this).attr("id").split("_")[0] + "</span><br>";
            var gradeHTMLString = "<strong>Grading:</strong> <span style='color:red'>" + $(this).attr("id").split("_")[1] + "</span>";
            
            return nameHTMLString + gradeHTMLString;
        });
    
    var svg = d3.select(drawTo)
        .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    
    
    svg.append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .style("fill", "#888888");
    
    svg.call(tip);
    
    var minimumContainerDim = Math.min((width - margin.left - margin.right), (height - margin.top - margin.bottom))

    var columnPadding = 5;
    var boxDim = (minimumContainerDim / graphData["results"].length) - columnPadding;
    
    console.log(graphData["results"].length);
    
    // x axis loop
    for (var i = 0; i < graphData["results"].length; i++) {
        
        console.log("A");
        console.log("B", graphData["results"][i]);
        console.log("C", i);
        
        var currentDataPoint = graphData["results"][i];
        var currentIndex = i;

        svg.append("rect")
            .attr("class", currentDataPoint["gameName"])
            .attr("id", currentDataPoint["opponent"]["name"]+"_"+currentDataPoint["opponent"]["grading"])
            .attr("width", boxDim)
            .attr("height", boxDim)
            .attr("x", i*boxDim+(i*columnPadding))
            .attr("y", height - boxDim)
            .style("fill", colorScheme[currentDataPoint["result"]])
            .on("mouseover", tip.show)
            .on("mouseout", tip.hide);
        
        var yOffset = height - 2*boxDim - columnPadding;
        
        for (var j = currentIndex-1; j >= 0; j--) {
            
            var previousDataPoint = graphData["results"][j];
            
            svg.append("rect")
                .attr("class", previousDataPoint["gameName"])
                .attr("id", previousDataPoint["opponent"]["name"]+"_"+previousDataPoint["opponent"]["grading"])
                .attr("width", boxDim)
                .attr("height", boxDim)
                .attr("x", i*boxDim+(i*columnPadding))
                .attr("y", yOffset)
                .style("fill", colorScheme[previousDataPoint["result"]])
                .on("mouseover", tip.show)
                .on("mouseout", tip.hide);
            
            yOffset = yOffset - boxDim - columnPadding;
        }

    }
    
    svg.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .style("text-decoration", "underline")  
        .text(title);

}