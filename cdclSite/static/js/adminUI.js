
// DISPLAY MODALS
function displayFixturesModal() {
    $("#fixturesIcon").click(function() {
        $("#fixturesModal").modal("show");
    });
}

function displayEventsModal() {
    $("#eventsIcon").click(function() {
        $("#eventsModal").modal("show");
    });
}

function displayTeamModal() {
    $("#teamIcon").click(function() {
        $("#teamModal").modal("show");
    });
}


function handleFileUpload() {
    
    $("#browseButton").click(function() {
        $(this).parent().find('input[type=file]').click();
        console.log($(this).val());
    });
    
    $("#fixtureFileUpload").change(function() {
       $(this).parent().parent().find('.form-control').html($(this).val().split(/[\\|/]/).pop());
        console.log($(this).val());
    });
    
}






// DROPDOWN SELECTIONS BELOW...



// FIXTURE EVENT SELECTION
function handleEventSelection() {
    
    $(".eventOption").click(function() {
        $(".selectedEvent").removeClass("selectedEvent");
        $(this).addClass("selectedEvent");
        $("#eventDropdown").text($(this).text());
        $("#eventDropdown").val($(this).text());
     
    });
    
}

// FIXTURE CLUB SELECTION
function handleAwayClubSelection() {
    
    $(".awayClubOption").click(function() {
        $(".selectedAwayClub").removeClass("selectedAwayClub");
        $(this).addClass("selectedAwayClub");
        $("#awayClubDropdown").text($(this).text());
        $("#awayClubDropdown").val($(this).text());
      
    });
    
}

function handleHomeClubSelection() {
    
    $(".homeClubOption").click(function() {
        $(".selectedHomeClub").removeClass("selectedHomeClub");
        $(this).addClass("selectedHomeClub");
        $("#homeClubDropdown").text($(this).text());
        $("#homeClubDropdown").val($(this).text());
      
    });
    
}


// FIXTURE TEAM SELECTION
function handleHomeTeamSelection() {
    
    $(".homeTeamOption").click(function() {
        $(".selectedHomeClub").removeClass("selectedHomeTeam");
        $(this).addClass("selectedHomeTeam");
        $("#homeTeamDropdown").text($(this).text());
        $("#homeTeamDropdown").val($(this).text());
      
    });
}

function handleAwayTeamSelection() {
    
    $(".awayTeamOption").click(function() {
        $(".selectedAwayClub").removeClass("selectedAwayTeam");
        $(this).addClass("selectedAwayTeam");
        $("#awayTeamDropdown").text($(this).text());
        $("#awayTeamDropdown").val($(this).text());
      
    });
}




// FIXTURE CAPTAIN SELECTION
function handleAwayCaptainSelection() {
    
    $(".awayCaptainOption").click(function() {
        $(".selectedAwayCaptain").removeClass("selectedAwayCaptain");
        $(this).addClass("selectedAwayCaptain");
        $("#awayCaptainDropdown").text($(this).text());
        $("#awayCaptainDropdown").val($(this).text());
      
    });
    
}

function handleHomeCaptainSelection() {
    
    $(".homeCaptainOption").click(function() {
        $(".selectedHomeCaptain").removeClass("selectedHomeCaptain");
        $(this).addClass("selectedHomeCaptain");
        $("#homeCaptainDropdown").text($(this).text());
        $("#homeCaptainDropdown").val($(this).text());
      
    });
    
}


// FIXURE CLUB SELECTION
function handleTeamClubSelection() {
    $(".teamClubOption").click(function() {
        $(".selectedTeamClubOption").removeClass("selectedTeamClubOption");
        $(this).addClass("selectedTeamClubOption");
        $("#teamClubDropdown").text($(this).text());
        $("#teamClubDropdown").val($(this).text());
        $("#newTeamName").val($(this).text());
    });
}


// FORM SUBMISSION
function submitAdminForm() {
    
    $("#submitSingleFixture").click(function() {
        
        $("#id_addFixture").val("TRUE");
        $("#id_fixtureEvent").val($(".selectedEvent").attr("id"));
        $("#id_homeClub").val($(".selectedHomeClub").attr("id"));
        $("#id_awayClub").val($(".selectedAwayClub").attr("id"));
        $("#id_homeCaptain").val($(".selectedHomeCaptain").attr("id"));
        $("#id_awayCaptain").val($(".selectedAwayCaptain").attr("id"));
        
        $("#id_homeTeam").val($(".selectedHomeTeam").attr("id"));
        $("#id_awayTeam").val($(".selectedAwayTeam").attr("id"));
        $("#id_fixtureDate").val($("#addFixtureDate").val());
        $("#adminForm").submit();
        
    });
    
    $("#submitBulkFixtures").click(function() {
        $("#id_addFixtureFile").val("TRUE");
        
        $("#id_fixtureFile").val($("#fixtureFileUpload").val());
        
        $("#adminForm").submit();
    });
    
    
    $("#submitSingleEvent").click(function() {
        $("#id_addEvent").val("TRUE");
        $("#id_newEventName").val($("#newEventName").val());
        $("#id_newEventBoards").val($("#newEventBoards").val());
        $("#adminForm").submit();
    });
    
    $("#submitTeamName").click(function() {
        
        $("#id_addTeamName").val("TRUE");
        $("#id_newTeamName").val($("#newTeamName").val());
        
        
        $("#adminForm").submit();
    });
    
}
