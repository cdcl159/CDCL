function selectClub() {
    $(".clubOption").click(function() {
        $("#clubDropdown").val($(this).attr("id"));
        $("#clubDropdown").text($(this).text());
    });
}

function submitForm() {
    $("#submitRequest").click(function() {

        $("#id_username").val($("#username").val());
        $("#id_password").val($("#password").val());
        $("#id_passwordConfirm").val($("#passwordConfirm").val());
        $("#id_forenames").val($("#fornames").val());
        $("#id_surname").val($("#surname").val());
        $("#id_primaryContactNumber").val($("#pcn").val());
        $("#id_backupContactNumber").val($("#bcn").val());
        $("#id_email").val($("#email").val());
        $("#id_ecfCode").val($("#ecf").val());
        $("#id_club").val($("#clubDropdown").val());

        $("#registrationForm").submit();

    });
    
}