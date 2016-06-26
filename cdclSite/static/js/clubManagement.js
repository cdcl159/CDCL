function initUI(clubData) {
    populateClubTable(clubData);
}



function populateClubTable(clubData) {
    
    for (x in clubData) {
        var currentClub = clubData[x];
        console.log(currentClub);
        
        console.log(x);
        console.log(currentClub.name);
        
        
        var newRowHTML = "<tr class='clubRow' id='" + x + "'><td>" + currentClub.name + "</td></tr>"
        
        $('.clubTable tr:last').before(newRowHTML);
        
    }
    
}

function clearFields() {
    
    $("#addClubIcon").click(function() {
        $("#submitClubChanges").addClass("addMode");
        $("#submitClubChanges").removeClass("editMode");
        $(".existingClubInput").val("");
    });
    
}

function submitNewClub() {
    
    $("#submitClubChanges").click(function() {
        
        if ($(this).hasClass("addMode")) {
            
            $("#id_addMode").val(true);
            $("#id_editMode").val(false);
            $("#id_name").val($("#existingClubName").val());
            $("#id_contactName").val($("#existingContactName").val());
            $("#id_contactNumber").val($("#existingContactNumber").val());
            $("#id_contactEmail").val($("#existingContactEmail").val());
            $("#id_clubWebsite").val($("#existingClubWebsite").val());
            $("#id_clubNight").val($("#existingClubNight").val());
            $("#id_clubVenue").val($("#existingClubVenue").val());
            $("#id_clubAddress").val($("#existingClubAddress").val());

            
        }
        
        if ($(this).hasClass("editMode")) {
            
            $("#id_selectedClubID").val($(".selectedClub").attr("id"));
            
            $("#id_addMode").val(false);
            $("#id_editMode").val(true);
            $("#id_name").val($("#existingClubName").val());
            $("#id_contactName").val($("#existingContactName").val());
            $("#id_contactNumber").val($("#existingContactNumber").val());
            $("#id_contactEmail").val($("#existingContactEmail").val());
            $("#id_clubWebsite").val($("#existingClubWebsite").val());
            $("#id_clubNight").val($("#existingClubNight").val());
            $("#id_clubVenue").val($("#existingClubVenue").val());
            $("#id_clubAddress").val($("#existingClubAddress").val());
            
        }
    
        $("#clubManagementForm").submit();

    });
    
}


function selectClub(clubdata) {
    $(".clubRow").click(function() {
        
        if ($(this).attr("id") != "newClubRow") {
            
            var clubInfo = clubdata[$(this).attr("id")];
            
            $(".selectedClub").removeClass("selectedClub");
            $(this).addClass("selectedClub");
            
            
            $("#submitClubChanges").addClass("editMode");
            $("#submitClubChanges").removeClass("addMode");
            
            
            $("#existingClubName").val(clubInfo["name"]);
            $("#existingContactName").val(clubInfo["contactName"]);
            $("#existingContactNumber").val(clubInfo["contactNumber"]);
            $("#existingContactEmail").val(clubInfo["contactEmail"]);
            $("#existingClubWebsite").val(clubInfo["clubWebsite"]);
            $("#existingClubNight").val(clubInfo["clubNight"]);
            $("#existingClubVenue").val(clubInfo["clubVenue"]);
            $("#existingClubAddress").val(clubInfo["clubAddress"]);
                        
        }
        
    });
}