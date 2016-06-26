
function initUI(fixtures) {
    
    populateFixtureDropdown(fixtures);
    
}


function populateFixtureDropdown(fixtures) {
    
    for (f in fixtures) {
        $(".fixtureDropdownMenu").append("<li class='fixtureOption' id='" + f + "'>" + fixtures[f].date + "</li>");
    }
    
}


function selectFixture(fixtures, playerData) {
    
    $(".fixtureOption").click(function() {
        
        $(".selectedFixture").removeClass("selectedFixture");
        $(this).addClass("selectedFixture");
        
        $(".fixtureDropdown").text($(this).text());
        $("#eventName").text(fixtures[$(".selectedFixture").attr("id")]["event"]);
        $("#fixtureDate").text(fixtures[$(".selectedFixture").attr("id")]["date"]);
        
        var selectedFixture = fixtures[$(this).attr("id")];
        
        updatePlayerDropdowns(selectedFixture, playerData);
        
        $("#homeTeamTitle").text("Home Team: " + selectedFixture["homeTeam"]["name"])
        $("#awayTeamTitle").text("Away Team: " + selectedFixture["awayTeam"]["name"])
    });
    
}

function updatePlayerDropdowns(fixture, playerData) {
    
    $(".playerDropdownMenu_h").empty();
    $(".playerDropdownMenu_a").empty();
    
    for (playerID in playerData) {
        
        var player = playerData[playerID];
        
        if (player["club"] == fixture["homeTeam"]["club"]) {
            
            $(".playerDropdownMenu_h").append("<li class='playerOption' id='" + playerID + "'>" + player["name"] + "</li>")
            
        }
        
        if (player["club"] == fixture["awayTeam"]["club"]) {
            
            $(".playerDropdownMenu_a").append("<li class='playerOption' id='" + playerID + "'>" + player["name"] + "</li>")
            
        }
        
    }
    
}


function selectPlayer(playerData) {
    
    
    $(".playerDropdownMenu_h").on("click", ".playerOption", function() {
        
        var player = $(this);
        
        $(this).parent().parent().find("button").text(player.text());
        $(this).parent().parent().find("button").val(player.attr("id"));
        
        $(this).parent().parent().parent().parent().find("td.gradingCell_h").find(".playerGrading").text(playerData[player.attr("id")]["grading"]);
        
    });
    
    $(".playerDropdownMenu_a").on("click", ".playerOption", function() {
        
        var player = $(this);
        
        $(this).parent().parent().find("button").text(player.text());
        $(this).parent().parent().find("button").val(player.attr("id"));
        
        $(this).parent().parent().parent().parent().find("td.gradingCell_a").find(".playerGrading").text(playerData[player.attr("id")]["grading"]);
        
    });
    
}