

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

    $("#submit").click(function() {

        console.log($("#title").val());
        console.log($("#body").val());
        console.log($(".postToDropdown").val());

        $("#id_title").val($("#title").val());
        $("#id_body").val($("#body").val());
        $("#id_postTo").val($(".postToDropdown").val());

        console.log($("#id_title").val());
        console.log($("#id_body").val());
        console.log($("#id_postTo").val());

        $("#announcementForm").submit();

    });
  

}