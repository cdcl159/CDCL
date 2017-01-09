function initUI() {

    $("#id_bulkMode").val(false);
    $("#id_editMode").val(false);
    $("#id_addMode").val(false);
    $("#id_teamMode").val(false);
    $("#id_statusMode").val(false);
    $("#id_removeFixtureMode").val(false);
    $("#id_removeTeamMode").val(false);
    $("#id_addTeamMode").val(false);

}
function displayUploadFixturesModal() {
    $("#openUpload").click(function() {
        $("#fixturesUploadModal").modal("show");
    });
}

function displayEditFixturesModal(fixturesData) {
    $(".editFixtureIcon").click(function() {

        var selectedFixtureID = $(this).parent().parent().attr("id");
        
        $("#editFixtureTitle").text("Edit Fixture: " + selectedFixtureID);
        
        $(".editEventDropdown").val(fixturesData[selectedFixtureID]["eventID"]);
        $(".editEventDropdown").text(fixturesData[selectedFixtureID]["eventName"]);
        $(".editSeasonDropdown").val(fixturesData[selectedFixtureID]["seasonID"]);
        $(".editSeasonDropdown").text(fixturesData[selectedFixtureID]["seasonName"]);

        $("#editDate").val(fixturesData[selectedFixtureID]["date"])

        $(".editHomeTeamDropdown").text(fixturesData[selectedFixtureID]["homeTeamName"]);
        $(".editAwayTeamDropdown").text(fixturesData[selectedFixtureID]["awayTeamName"]);
        $(".editHomeTeamDropdown").val(fixturesData[selectedFixtureID]["homeTeamID"]);
        $(".editAwayTeamDropdown").val(fixturesData[selectedFixtureID]["awayTeamID"]);

        $("#editFixtureModal").modal("show");

    });
}

function editFixtureEvent() {
    $(".editEventOption").click(function() {
        $(".editSelectedEvent").removeClass("editSelectedEvent");
        $(this).addClass("editSelectedEvent");
        $(".editEventDropdown").val($(this).attr("id"));
        $(".editEventDropdown").text($(this).text());
        
    });
}

function editFixtureSeason() {
    $(".editSeasonOption").click(function() {
        $(".editSelectedSeason").removeClass("editSelectedSeason");
        $(this).addClass("editSelectedSeason");
        $(".editSeasonDropdown").val($(this).attr("id"));
        $(".editSeasonDropdown").text($(this).text());
        
    });
}

function editFixtureHomeTeam() {
    $(".editHomeTeamOption").click(function() {
        $(".editSelectedHomeTeam").removeClass("ediTeamtSelectedHome");
        $(this).addClass("editSelectedHomeTeam");
        $(".editHomeTeamDropdown").val($(this).attr("id"));
        $(".editHomeTeamDropdown").text($(this).text());
        
    });
}

function editFixtureAwayTeam() {
    $(".editAwayTeamOption").click(function() {
        $(".editSelectedAwayTeam").removeClass("ediTeamtSelectedAway");
        $(this).addClass("editSelectedAwayTeam");
        $(".editAwayTeamDropdown").val($(this).attr("id"));
        $(".editAwayTeamDropdown").text($(this).text());
        
    });
}

function submitFixtureChanges() {
    $("#submitChanges").click(function() {
        $("#id_editMode").val(true);
        $("#id_selectedFixtureID").val($("#editFixtureTitle").text().split(": ")[1]);
        $("#id_editFixtureSeason").val($(".editSeasonDropdown").val());
        $("#id_editFixtureEvent").val($(".editEventDropdown").val());
        $("#id_editFixtureDate").val($("#editDate").val());
        $("#id_editFixtureHomeTeam").val($(".editHomeTeamDropdown").val());
        $("#id_editFixtureAwayTeam").val($(".editAwayTeamDropdown").val());

        $("#fixtureManagementForm").submit();
    });
    
}



function displayAddFixturesModal() {
    $("#addFixtureIcon").click(function() {
        $("#addFixtureModal").modal("show");
    });
}

function selectNewFixtureEvent() {
    $(".newFixtureEventOption").click(function() {
        $(".newSelectedEvent").removeClass("newSelectedEvent");
        $(this).addClass("newSelectedEvent");
        $(".newSelectedEventDropdown").val($(this).text());
        $(".newSelectedEventDropdown").text($(this).text());
        
    });
}

function selectNewFixtureSeason() {
    $(".newFixtureSeasonOption").click(function() {

        $(".newSelectedSeason").removeClass("newSelectedSeason");
        $(this).addClass("newSelectedSeason");
        $(".newSelectedSeasonDropdown").val($(this).text());
        $(".newSelectedSeasonDropdown").text($(this).text());
        

    });
}

function selectNewFixtureHomeTeam() {
    $(".newFixtureHomeTeamOption").click(function() {

        $(".newSelectedHomeTeam").removeClass("newSelectedHomeTeam");
        $(this).addClass("newSelectedHomeTeam");
        $(".newSelectedHomeTeamDropdown").val($(this).text());
        $(".newSelectedHomeTeamDropdown").text($(this).text());
        

    });
}



function selectNewFixtureAwayTeam() {
    $(".newFixtureAwayTeamOption").click(function() {

        $(".newSelectedAwayTeam").removeClass("newSelectedAwayTeam");
        $(this).addClass("newSelectedAwayTeam");
        $(".newSelectedAwayTeamDropdown").val($(this).text());
        $(".newSelectedAwayTeamDropdown").text($(this).text());
        

    });
}


function handleFileUpload() {
    
    $("#browseButton").click(function() {
        $(this).parent().find('input[type=file]').click();
    });
    
    $("#fixtureFileUpload").change(function() {
       $(this).parent().parent().find('.form-control').html($(this).val().split(/[\\|/]/).pop());
    });
    
}

function submitFixureForm() {
    
    $("#submitFixtures").click(function() {

        $("#id_bulkMode").val(true);
        $("#id_fixtureFile").val($("#fixtureFileUpload").val());
        $("#fixtureManagementForm").submit();
    });

    $("#submitSingleFixture").click(function() {
        $("#id_addMode").val(true);
        $("#id_newFixtureDivision").val($(".newSelectedDivisionDropdown").val());
        $("#id_newFixtureSeason").val($(".newSelectedSeasonDropdown").val());
        $("#id_newFixtureEvent").val($(".newSelectedEventDropdown").val());
        $("#id_newFixtureDate").val($("#newFixtureDate").val());
        $("#id_newFixtureHomeTeam").val($(".newSelectedHomeTeamDropdown").val());
        $("#id_newFixtureAwayTeam").val($(".newSelectedAwayTeamDropdown").val());
        $("#fixtureManagementForm").submit();

    });
    
}


function selectClubForTeam(players) {
    $(".teamClubOption").click(function() {
        
        $(this).parent().parent().find(".teamClubDropdown").text($(this).text());
        $(this).parent().parent().find(".teamClubDropdown").val($(this).attr("id"));

        var dropdownMenu = $(this).closest('tr').children('td.captainName').find(".teamCaptainDropdownMenu");
        
        dropdownMenu.empty();
  
        for (p in players) {
            if (players[p]["club"] == $(this).text()) {
                
                var newOption = "<li class='captainOption' id='" + p + "'>" + players[p]["name"] + "</li>";
                
                dropdownMenu.append(newOption);
                
            }
        }
        
    });
}


function selectClubForNewTeam(players) {
    $(".newTeamClubOption").click(function() {
        
        $(this).parent().parent().find("#newTeamClubDropdown").text($(this).text());
        $(this).parent().parent().find("#newTeamClubDropdown").val($(this).attr("id"));

        var dropdownMenu = $("#newTeamCaptainDropdownMenu");
        
        dropdownMenu.empty();
  
        for (p in players) {
            if (players[p]["club"] == $(this).text()) {
                
                var newOption = "<li class='captainOption' id='" + p + "'>" + players[p]["name"] + "</li>";
                
                dropdownMenu.append(newOption);
                
            }
        }
        
    });
}

function selectNewTeamCaptain() {
    $("#newTeamCaptainDropdownMenu").on("click", ".captainOption", function() {
       
        $(this).parent().parent().find("#newTeamCaptainDropdown").text($(this).text())
        $(this).parent().parent().find("#newTeamCaptainDropdown").val($(this).attr("id"));
        
    });

}


function selectTeamCaptain() {
    $(".teamCaptainDropdownMenu").on("click", ".captainOption", function() {
       
        $(this).parent().parent().find(".teamCaptainDropdown").text($(this).text())
        $(this).parent().parent().find(".teamCaptainDropdown").val($(this).attr("id"));
        
    });

}


function submitTeams() {
    $("#submitTeams").click(function() {
        
        var teamData = {}
        
        var teamIDs = $(".teamRow").each(function() {
            
            var currentID = $(this).attr("id");
            
            teamData[currentID] = {
                "clubID": $("." + currentID+"_club").val(),
                "captainID": $("." + currentID+"_cap").val()
            }
            
        });
        
        $("#id_teamMode").val(true);
        $("#id_bulkMode").val(false);
        
        $("#id_teamData").val(JSON.stringify(teamData));
        
        $("#fixtureManagementForm").submit();
        
    });
}


function submitNewTeam() {
    $("#submitNewTeam").click(function() {
        $("#id_addTeamMode").val(true);
        $("#id_newTeamName").val($("#newTeamName").val());
        $("#id_newTeamClubID").val($("#newTeamClubDropdown").val());
        $("#id_newTeamCaptainID").val($("#newTeamCaptainDropdown").val());
        $("#fixtureManagementForm").submit();
    });
}

function selectTeam(teamData, players) {
    $(".editTeamIcon").click(function() {
        
        var data = teamData[$(this).parent().parent().attr("id")];
        $("#teamModalTitle").text(data["name"]);
        $("#editTeamName").val(data["name"]);

        $("#editTeamCaptainDropdown").text(data["captainName"]);
        $("#editTeamCaptainDropdown").val(data["captainID`"]);
        $("#editTeamClubDropdown").text(data["clubName"]);
        $("#editTeamClubDropdown").val(data["clubID"]);

        $("#editTeamCaptainDropdownMenu").empty();

        var initialPlayers = populatePlayerDropdown(players, data["clubName"]);

        for (i = 0; i < initialPlayers.length; i++) {
            var player = initialPlayers[i];
            var option = "<li class='editCaptainOption' id='" + player["id"] + "'>" + player["name"] + "</li>"
            $("#editTeamCaptainDropdownMenu").append(option);
        }

        $("#editTeamModal").modal("show");

    });
}



function populatePlayerDropdown(players, clubName) {

    var output = [];
    console.log(clubName);
    for (p in players) {
        if (players[p].club == clubName) {
            console.log("FOUND");
            output.push(players[p]);
        }
    }

    console.log("out:", output);
    return output;

}



function displaySubmission(fixturesData) {

    $(".receivedHomeSubmission").click(function() {

        console.log(fixturesData);
        
        var selectedFixtureID = $(this).parent().parent().attr("id");

        var homeSubmission = fixturesData[selectedFixtureID]["homeSubmission"]
        
        $("#submissionTitle").text("Submission From: " + homeSubmission["teamName"]);

        for (var i = 0; i < homeSubmission["games"].length; i++) {

            var currentGame = homeSubmission["games"][i];

            $("#b" + (i + 1).toString() + "_h_name").text(currentGame["homePlayerName"]);
            $("#b" + (i + 1).toString() + "_h_grade").text(currentGame["homePlayerGrade"]);
            $("#b" + (i + 1).toString() + "_h_score").text(currentGame["homePlayerScore"]);
            $("#b" + (i + 1).toString() + "_a_name").text(currentGame["awayPlayerName"]);
            $("#b" + (i + 1).toString() + "_a_grade").text(currentGame["awayPlayerGrade"]);
            $("#b" + (i + 1).toString() + "_a_score").text(currentGame["awayPlayerScore"]);

        }

        $("#submissionModal").modal("show");

    });

    $(".receivedAwaySubmission").click(function() {
        
        var selectedFixtureID = $(this).parent().parent().attr("id");

        var awaySubmission = fixturesData[selectedFixtureID]["awaySubmission"]

        $("#submissionTitle").text("Submission From: " + awaySubmission["teamName"]);

        for (var i = 0; i < awaySubmission["games"].length; i++) {

            var currentGame = awaySubmission["games"][i];

            $("#b" + (i + 1).toString() + "_h_name").text(currentGame["homePlayerName"]);
            $("#b" + (i + 1).toString() + "_h_grade").text(currentGame["homePlayerGrade"]);
            $("#b" + (i + 1).toString() + "_h_score").text(currentGame["homePlayerScore"]);
            $("#b" + (i + 1).toString() + "_a_name").text(currentGame["awayPlayerName"]);
            $("#b" + (i + 1).toString() + "_a_grade").text(currentGame["awayPlayerGrade"]);
            $("#b" + (i + 1).toString() + "_a_score").text(currentGame["awayPlayerScore"]);

        }

        $("#submissionModal").modal("show");
        
    });


}

function selectStatus() {
    $(".statusOption").click(function() {

        $("#id_statusMode").val(true);
        $("#id_selectedFixtureID").val($(this).parent().parent().parent().parent().attr("id"));
        $("#id_newStatus").val($(this).attr("id"));

        $("#fixtureManagementForm").submit();

    });
}

function removeTeam() {
    $(".removeTeam").click(function() {

        $("#id_removeTeamMode").val(true);
        $("#id_selectedTeamID").val($(this).parent().parent().attr("id"));

        $("#fixtureManagementForm").submit();

    });
}

function displayNewTeamModal() {
    
    $("#addTeamIcon").click(function() {
        $("#newTeamModal").modal("show");
    });
    
}