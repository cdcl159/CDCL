

function displayConfirmationModal() {


    $("#acceptAnnouncement").click(function() {
        $("#confirmationModal").modal("show");
    });

}

function selectPostToLocation() {
    $(".postToOption").click(function() {
        $(".postToDropdown").val($(this).attr("id"));
        $(".postToDropdown").text($(this).text());
    });
}

function submitAnnouncementForm() {
    
    $("#id_title").val($("#title").val());
    $("#id_body").val($("#body").val());

    $("#id_postTo").val($("#postToDropdown").val());

    $("#announcementForm").submit();

}