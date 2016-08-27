// Username
// Active
// Superuser
// Officer
// RecordSecretary
// Treasurer
// User Data
// Player Data

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
            var activeCell = '<td><img class="tableIcon checkedIcon" src="' + enabledIconPath + '" %}></td>';
        } else {
            var activeCell = '<td><img class="tableIcon uncheckedIcon" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["Superuser"]) {
            var superuserCell = '<td><img class="tableIcon checkedIcon" src="' + enabledIconPath + '" %}></td>';
        } else {
            var superuserCell = '<td><img class="tableIcon uncheckedIcon" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isOffier"]) {
            var officerCell = '<td><img class="tableIcon checkedIcon" src="' + enabledIconPath + '" %}></td>';
        } else {
            var officerCell = '<td><img class="tableIcon uncheckedIcon" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isRecordSecretary"]) {
            var recordSecretaryCell = '<td><img class="tableIcon checkedIcon" src="' + enabledIconPath + '" %}></td>';
        } else {
            var recordSecretaryCell = '<td><img class="tableIcon uncheckedIcon" src="' + disabledIconPath + '" %}></td>';
        }

        if (userData[x]["userData"] && userData[x]["userData"]["isTreasurer"]) {
            var treasurerCell = '<td><img class="tableIcon checkedIcon" src="' + enabledIconPath + '" %}></td>';
        } else {
            var treasurerCell = '<td><img class="tableIcon uncheckedIcon" src="' + disabledIconPath + '" %}></td>';
        }

        var userdataCell = '<td><img class="tableIcon userdataIcon" src="' + dataIconPath + '" %}></td>';

        var playerdataCell = '<td><img class="tableIcon userdataIcon" src="' + playerIconPath + '" %}></td>';

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