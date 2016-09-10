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
        
        $("#playerdata_forenames").text("");
        $("#playerdata_surname").text("");
        $("#playerdata_ecf").text("");
        $("#playerdata_grading").text("");
        $("#playerdata_club").text("");

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


function toggleActivity() {

    $("#userTable").on("click", ".activeToggle", function() {

        var selectedUserID = $(this).parent().parent().attr("id");

        $("#id_selectedUserId").val(selectedUserID);

        $("#id_activeMode").val(true);
        $("#id_officerMode").val(false);
        $("#id_recordsMode").val(false);
        $("#id_treasurerMode").val(false);
        $("#id_superuserMode").val(false);

        $("#userManagementToolsForm").submit();

    });

}


function toggleOfficer() {


    $("#userTable").on("click", ".officerToggle", function() {

        var selectedUserID = $(this).parent().parent().attr("id");

        $("#id_selectedUserId").val(selectedUserID);

        $("#id_activeMode").val(false);
        $("#id_officerMode").val(true);
        $("#id_recordsMode").val(false);
        $("#id_treasurerMode").val(false);
        $("#id_superuserMode").val(false);

        $("#userManagementToolsForm").submit();

    });

}

function toggleTreasurer() {


    $("#userTable").on("click", ".treasurerToggle", function() {

        var selectedUserID = $(this).parent().parent().attr("id");

        $("#id_selectedUserId").val(selectedUserID);

        $("#id_activeMode").val(false);
        $("#id_officerMode").val(false);
        $("#id_recordsMode").val(false);
        $("#id_treasurerMode").val(true);
        $("#id_superuserMode").val(false);

        $("#userManagementToolsForm").submit();

    });

}

function togglRecords() {


    $("#userTable").on("click", ".recordToggle", function() {

        var selectedUserID = $(this).parent().parent().attr("id");

        $("#id_selectedUserId").val(selectedUserID);

        $("#id_activeMode").val(false);
        $("#id_officerMode").val(false);
        $("#id_recordsMode").val(true);
        $("#id_treasurerMode").val(false);
        $("#id_superuserMode").val(false);

        $("#userManagementToolsForm").submit();

    });

}


function toggleSuperuser() {

    $("#userTable").on("click", ".superuserToggle", function() {

        var selectedUserID = $(this).parent().parent().attr("id");

        $("#id_selectedUserId").val(selectedUserID);
        $("#id_activeMode").val(false);
        $("#id_officerMode").val(false);
        $("#id_recordsMode").val(false);
        $("#id_treasurerMode").val(false);
        $("#id_superuserMode").val(true);

        $("#userManagementToolsForm").submit();

    });

}



function initUI(
    userData,
    enabledIconPath,
    disabledIconPath,
    playerIconPath,
    dataIconPath) {

    for (x in userData) {

        console.log(userData[x]);

        var usernameCell = "<td>" + userData[x]["username"] + "</td>";

        if (userData[x]["active"]) {
            var activeCell = '<td><img class="tableIcon activeToggle" src="' + enabledIconPath + '" %}></td>';
        } else {
            var activeCell = '<td><img class="tableIcon activeToggle" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["superuser"]) {
            var superuserCell = '<td><img class="tableIcon superuserToggle" src="' + enabledIconPath + '" %}></td>';
        } else {
            var superuserCell = '<td><img class="tableIcon superuserToggle" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isOfficer"]) {
            var officerCell = '<td><img class="tableIcon officerToggle" src="' + enabledIconPath + '" %}></td>';
        } else {
            var officerCell = '<td><img class="tableIcon officerToggle" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isRecordSecretary"]) {
            var recordSecretaryCell = '<td><img class="tableIcon recordToggle" src="' + enabledIconPath + '" %}></td>';
        } else {
            var recordSecretaryCell = '<td><img class="tableIcon recordToggle" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isTreasurer"]) {
            var treasurerCell = '<td><img class="tableIcon treasurerToggle" src="' + enabledIconPath + '" %}></td>';
        } else {
            var treasurerCell = '<td><img class="tableIcon treasurerToggle" src="' + disabledIconPath + '" %}></td>';
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