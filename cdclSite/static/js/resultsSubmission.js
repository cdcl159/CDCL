
function initUI(fixtures) {
    
    populateFixtureDropdown(fixtures);
    
}


function populateFixtureDropdown(fixtures) {
    
    for (f in fixtures) {
        console.log(f);
        $(".fixtureDropdownMenu").append("<li class='fixtureOption' id='" + f + "'>" + fixtures[f].date + "(" + fixtures[f].event + ")" + "</li>");
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




function submitResults() {
    $("#submitResultsSubmission").click(function() {
        
        $("#id_selectedFixtureID").val($(".selectedFixture").attr("id"));

        $("#id_homeTeam").val($("#homeTeamTitle").text().replace("Home Team: ", ""));
        $("#id_awayTeam").val($("#awayTeamTitle").text().replace("Away Team: ", ""));

        $("#id_board1_homePlayerID").val($(".playerDropdown_b1_h").val());
        $("#id_board2_homePlayerID").val($(".playerDropdown_b2_h").val());
        $("#id_board3_homePlayerID").val($(".playerDropdown_b3_h").val());
        $("#id_board4_homePlayerID").val($(".playerDropdown_b4_h").val());
        $("#id_board5_homePlayerID").val($(".playerDropdown_b5_h").val());
        $("#id_board6_homePlayerID").val($(".playerDropdown_b6_h").val());

        $("#id_board1_awayPlayerID").val($(".playerDropdown_b1_a").val());
        $("#id_board2_awayPlayerID").val($(".playerDropdown_b2_a").val());
        $("#id_board3_awayPlayerID").val($(".playerDropdown_b3_a").val());
        $("#id_board4_awayPlayerID").val($(".playerDropdown_b4_a").val());
        $("#id_board5_awayPlayerID").val($(".playerDropdown_b5_a").val());
        $("#id_board6_awayPlayerID").val($(".playerDropdown_b6_a").val());

        $("#id_board1_homePlayerScore").val($("#board_1_homeScore").val());
        $("#id_board2_homePlayerScore").val($("#board_2_homeScore").val());
        $("#id_board3_homePlayerScore").val($("#board_3_homeScore").val());
        $("#id_board4_homePlayerScore").val($("#board_4_homeScore").val());
        $("#id_board5_homePlayerScore").val($("#board_5_homeScore").val());
        $("#id_board6_homePlayerScore").val($("#board_6_homeScore").val());

        $("#id_board1_awayPlayerScore").val($("#board_1_awayScore").val());
        $("#id_board2_awayPlayerScore").val($("#board_2_awayScore").val());
        $("#id_board3_awayPlayerScore").val($("#board_3_awayScore").val());
        $("#id_board4_awayPlayerScore").val($("#board_4_awayScore").val());
        $("#id_board5_awayPlayerScore").val($("#board_5_awayScore").val());
        $("#id_board6_awayPlayerScore").val($("#board_6_awayScore").val());


        alert("fixture id", $("#id_selectedFixtureID").val());
        alert("home team", $("#id_homeTeam").val());
        alert("away team", $("#id_awayTeam").val());

        alert("board1_h_playerid", $("#id_board1_homePlayerID").val());
        alert("board2_h_playerid", $("#id_board2_homePlayerID").val());
        alert("board3_h_playerid", $("#id_board3_homePlayerID").val());
        alert("board4_h_playerid", $("#id_board4_homePlayerID").val());
        alert("board5_h_playerid", $("#id_board5_homePlayerID").val());
        alert("board6_h_playerid", $("#id_board6_homePlayerID").val());
        alert("board1_a_playerid", $("#id_board1_awayPlayerID").val());
        alert("board2_a_playerid", $("#id_board2_awayPlayerID").val());
        alert("board3_a_playerid", $("#id_board3_awayPlayerID").val());
        alert("board4_a_playerid", $("#id_board4_awayPlayerID").val());
        alert("board5_a_playerid", $("#id_board5_awayPlayerID").val());
        alert("board6_a_playerid", $("#id_board6_awayPlayerID").val());
        alert("board1_h_playerscore", $("#id_board1_homePlayerScore").val());
        alert("board2_h_playerscore", $("#id_board2_homePlayerScore").val());
        alert("board3_h_playerscore", $("#id_board3_homePlayerScore").val());
        alert("board4_h_playerscore", $("#id_board4_homePlayerScore").val());
        alert("board5_h_playerscore", $("#id_board5_homePlayerScore").val());
        alert("board6_h_playerscore", $("#id_board6_homePlayerScore").val());
        alert("board1_a_playerscore", $("#id_board1_awayPlayerScore").val());
        alert("board2_a_playerscore", $("#id_board2_awayPlayerScore").val());
        alert("board3_a_playerscore", $("#id_board3_awayPlayerScore").val());
        alert("board4_a_playerscore", $("#id_board4_awayPlayerScore").val());
        alert("board5_a_playerscore", $("#id_board5_awayPlayerScore").val());
        alert("board6_a_playerscore", $("#id_board6_awayPlayerScore").val());


        $("#resultsForm").submit();

    });
}