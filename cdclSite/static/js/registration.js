function selectClub() {
    $(".clubOption").click(function() {
        $(".clubDropdown").val($(this).attr("id"));
        $(".clubDropdown").text($(this).text());
    });
}

function submitForm() {
    $("#submitRequest").click(function() {

        $("#id_username").val($("#username").val());
        $("#id_password").val($("#password").val());
        $("#id_passwordConfirm").val($("#passwordConfirm").val());
        $("#id_forenames").val($("#fornames").val());
        $("#id_surname").val($("#surname").val());
        $("#id_address_1").val($("#address1").val());
        $("#id_address_2").val($("#address2").val());
        $("#id_address_3").val($("#address3").val());
        $("#id_postcode").val($("#postcode").val());
        $("#id_primaryContactNumber").val($("#contactNumberA").val());
        $("#id_backupContactNumber").val($("#contactNumberB").val());
        $("#id_email").val($("#email").val());
        $("#id_ecfCode").val();
        $("#id_club").val($(".clubDropdown").val());

        $("#registrationForm").submit();

    });
    
}