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
        
        $('.clubTable').append(newRowHTML);
        
    }
    
}

function clearFields() {
    
    $("#addClubIcon").click(function() {
        $("#submitClubChanges").addClass("addMode");
        $("#submitClubChanges").removeClass("editMode");
        $(".existingClubInput").val("");
    });
    
}

function addClub() {
    $("#addNewClub").click(function() {

        $("#id_addMode").val(true);
        
        $("#id_name").val($("#existingClubName").val());
        $("#id_contactName").val($("#existingContactName").val());
        $("#id_contactNumber").val($("#existingContactNumber").val());
        $("#id_contactEmail").val($("#existingContactEmail").val());
        $("#id_clubWebsite").val($("#existingClubWebsite").val());
        $("#id_clubNight").val($("#existingClubNight").val());
        $("#id_clubVenue").val($("#existingClubVenue").val());
        $("#id_clubAddress").val($("#existingClubAddress").val());
        
        $("#clubManagementForm").submit();

    });
}

function editClub() {

    $("#submitClubChanges").click(function() {

        if ($(".selectedClub")[0]) {

            $("#id_selectedClubID").val($(".selectedClub").attr("id"));
            $("#id_editMode").val(true);

            $("#id_name").val($("#existingClubName").val());
            $("#id_contactName").val($("#existingContactName").val());
            $("#id_contactNumber").val($("#existingContactNumber").val());
            $("#id_contactEmail").val($("#existingContactEmail").val());
            $("#id_clubWebsite").val($("#existingClubWebsite").val());
            $("#id_clubNight").val($("#existingClubNight").val());
            $("#id_clubVenue").val($("#existingClubVenue").val());
            $("#id_clubAddress").val($("#existingClubAddress").val());
            $("#id_clubCode").val($("#existingClubCode").val());
            alert($("#id_clubCode").val());
            $("#clubManagementForm").submit();
        }

    });
    
}


function selectClub(clubdata) {
    $(".clubRow").click(function() {
        
        if ($(this).attr("id") != "newClubRow") {
            
            var clubInfo = clubdata[$(this).attr("id")];
            
            $(".selectedClub").removeClass("selectedClub");
            $(this).addClass("selectedClub");
            
            $("#existingClubName").val(clubInfo["name"]);
            $("#existingContactName").val(clubInfo["contactName"]);
            $("#existingContactNumber").val(clubInfo["contactNumber"]);
            $("#existingContactEmail").val(clubInfo["contactEmail"]);
            $("#existingClubWebsite").val(clubInfo["website"]);
            $("#existingClubNight").val(clubInfo["night"]);
            $("#existingClubVenue").val(clubInfo["venue"]);
            $("#existingClubAddress").val(clubInfo["address"]);
            $("#existingClubCode").val(clubInfo["code"]);
                        
        }
        
    });
}