

function displayUploadModal() {
    $("#openUpload").click(function() {
        
        $("#uploadModal").modal("show");
        
    });
}


function handleFileUpload() {
    
    $("#browseButton").click(function() {
        $(this).parent().find('input[type=file]').click();
        console.log($(this).val());
    });
    
    $("#playerFileUpload").change(function() {
       $(this).parent().parent().find('.form-control').html($(this).val().split(/[\\|/]/).pop());
        console.log($(this).val());
    });
    
}

function submitPlayerForm() {
    
    
    $("#uploadPlayerForm").click(function() {
        
        $("#id_bulkMode").val(true);
        $("#id_playerFile").val($("#playerFileUpload").val());
        $("#playerManagementForm").submit();
        
    });
    
}


function initUI(playerData, settingsIconSrc) {
    
    for (p in playerData) {
        
        var currentPlayer = playerData[p];
        
        var newRowHTML = "<tr class='playerRow' id='" + p + "'><td class='forenames'>" + currentPlayer["forenames"] +
            "</td><td class='surname'>" + currentPlayer["surname"] +
            "</td><td class='ecf'>" + currentPlayer["ecfCode"] +
            "</td><td class='grading'>" + currentPlayer["grading"] +
            "</td><td class='club'>" + currentPlayer["club"] +
            "</td><td class='edit'>" + '<img class="toolIcon editPlayer" src="'+settingsIconSrc+'">' +
            "</td></tr>"
            
        $('.playerTable tr:last').before(newRowHTML);
        
    }
    
}

function displayDetailsModal() {

    $(".editPlayer").click(function() {
        
        var editButton = $(this);
        
        $(".detailsTitle").text("EDIT PLAYER: " + editButton.closest('tr').attr("id"));
        $("#submitDetails").text("Submit Changes");
        $("#submitDetails").removeClass("addMode");
        $("#submitDetails").addClass("editMode");
        
        $("#playerForenamesInput").val(editButton.closest('tr').children('td.forenames').text());
        $("#playerSurnameInput").val(editButton.closest('tr').children('td.surname').text());
        $("#playerECFInput").val(editButton.closest('tr').children('td.ecf').text());
        $("#playerGradingInput").val(editButton.closest('tr').children('td.grading').text());
        $("#playerClubInput").val(editButton.closest('tr').children('td.club').text());
        
        $("#detailsModal").modal("show");
        
        
    });
    
    $("#addPlayerIcon").click(function() {
        
        $(".detailsTitle").text("ADD PLAYER");
        $(".playerDetailsInput").val("");
        
        $("#submitDetails").text("Add Player");
        $("#submitDetails").removeClass("editMode");
        $("#submitDetails").addClass("addMode");
        
        $("#detailsModal").modal("show");
        
    });
    
}


function submitPlayerDetails() {

    $("#submitDetails").click(function() {
        
        
        if ($(this).hasClass("editMode")) {
            
            $("#id_editMode").val(true);
            $("#id_addMode").val(false);
            $("#id_playerID").val(parseInt($(".detailsTitle").text().split(": ")[1]));

        }
        
        if ($(this).hasClass("addMode")) {
        
            $("#id_addMode").val(true);
            $("#id_editMode").val(false);
            
        }
        
        
        $("#id_playerForenames").val($("#playerForenamesInput").val());
        $("#id_playerSurname").val($("#playerSurnameInput").val());
        $("#id_playerEcfCode").val($("#playerECFInput").val());
        $("#id_playerGrading").val($("#playerGradingInput").val());
        $("#id_playerClub").val($("#playerClubInput").val());

        $("#playerManagementForm").submit();
        
    });

}
