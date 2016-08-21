
function displayUploadFixturesModal() {
    
    $("#openUpload").click(function() {
    
        $("#fixturesUploadModal").modal("show");
        
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

function selectClubCaptain() {
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
            console.log(currentID);
            
            teamData[currentID] = {
                "clubID": $("." + currentID+"_club").val(),
                "captainID": $("." + currentID+"_cap").val()
            }
            
        });
        
        $("#id_teamMode").val(true);
        $("#id_bulkMode").val(false);
        
        console.log(teamData);
        $("#id_teamData").val(JSON.stringify(teamData));
        
        $("#fixtureManagementForm").submit();
        
    });
}