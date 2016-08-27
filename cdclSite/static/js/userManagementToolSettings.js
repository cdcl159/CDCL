function displayUserDataModal(userData) {
    
    $("#userTable").on("click", ".userdataIcon", function() {

        var selectedUserID = $(this).parent().parent().attr("id");
        if (userData[selectedUserID]["userData"] != null) {

            $("#userdataTitle").text("User Data for: " + userData[selectedUserID]["username"]);

            $("#userdata_forenames").text(userData[selectedUserID]["userData"]["forenames"]);
            $("#userdata_surname").text(userData[selectedUserID]["userData"]["surname"]);
            $("#userdata_address_1").text(userData[selectedUserID]["userData"]["address_1"]);
            $("#userdata_address_2").text(userData[selectedUserID]["userData"]["address_2"]);
            $("#userdata_address_3").text(userData[selectedUserID]["userData"]["address_3"]);
            $("#userdata_postcode").text(userData[selectedUserID]["userData"]["postcode"]);
            $("#userdata_primaryContactNumber").text(userData[selectedUserID]["userData"]["primaryContactNumber"]);
            $("#userdata_backupContactNumber").text(userData[selectedUserID]["userData"]["backupContactNumber"]);
            $("#userdata_email").text(userData[selectedUserID]["userData"]["email"]);

        } else {
            
            $("#userdataTitle").text("User Data for: " + userData[selectedUserID]["username"] + " (none on record)");

        }
        
        $("#userdataModal").modal("show");

    });

}


function displayPlayerDataModal(userData) {
    
    $("#userTable").on("click", ".playerdataIcon", function() {

        var selectedUserID = $(this).parent().parent().attr("id");
        
        if (userData[selectedUserID]["playerData"] != null) {

            $("#playerdataTitle").text("Player Data for: " + userData[selectedUserID]["username"]);

            $("#playerdata_forenames").text(userData[selectedUserID]["playerData"]["forenames"]);
            $("#playerdata_surname").text(userData[selectedUserID]["playerData"]["surname"]);
            $("#playerdata_ecf").text(userData[selectedUserID]["playerData"]["ecfCode"]);
            $("#playerdata_grading").text(userData[selectedUserID]["userData"]["grading"]);
            $("#playerdata_club").text(userData[selectedUserID]["playerData"]["club"]);
            
        } else {
            
            $("#playerdataTitle").text("User Data for: " + userData[selectedUserID]["username"] + " (none on record)");

        }
        
        $("#playerdataModal").modal("show");

    });

}


function initUI(
    userData,
    enabledIconPath,
    disabledIconPath,
    playerIconPath,
    dataIconPath) {

    for (x in userData) {

        var usernameCell = "<td>" + userData[x]["username"] + "</td>";

        if (userData[x]["active"]) {
            var activeCell = '<td><img class="tableIcon toggleIcon userActive" src="' + enabledIconPath + '" %}></td>';
        } else {
            var activeCell = '<td><img class="tableIcon toggleIcon userInactive" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["Superuser"]) {
            var superuserCell = '<td><img class="tableIcon toggleIcon userSuperuser" src="' + enabledIconPath + '" %}></td>';
        } else {
            var superuserCell = '<td><img class="tableIcon toggleIcon userNotSuperuser" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isOffier"]) {
            var officerCell = '<td><img class="tableIcon toggleIcon userOfficer" src="' + enabledIconPath + '" %}></td>';
        } else {
            var officerCell = '<td><img class="tableIcon toggleIcon userNotOfficer" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isRecordSecretary"]) {
            var recordSecretaryCell = '<td><img class="tableIcon toggleIcon userRecordSec" src="' + enabledIconPath + '" %}></td>';
        } else {
            var recordSecretaryCell = '<td><img class="tableIcon toggleIcon userNotRecordSec" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isTreasurer"]) {
            var treasurerCell = '<td><img class="tableIcon toggleIcon userTreasurer" src="' + enabledIconPath + '" %}></td>';
        } else {
            var treasurerCell = '<td><img class="tableIcon toggleIcon userNotTreasurer" src="' + disabledIconPath + '" %}></td>';
        }

        var userdataCell = '<td><img class="tableIcon userdataIcon" src="' + dataIconPath + '" %}></td>';

        var playerdataCell = '<td><img class="tableIcon playerdataIcon" src="' + playerIconPath + '" %}></td>';

        var row = "<tr class='userRow' id='" + x + "'>" +
            usernameCell + 
            activeCell + 
            superuserCell + 
            officerCell + 
            recordSecretaryCell + 
            treasurerCell + 
            userdataCell + 
            playerdataCell + 
            "</tr>";

        $("#userTable").append(row);

    }

}