function handlePageMessage(pageMessage) {

    $("#messageTitle").text(pageMessage.type);
    $("#messageBody").text(pageMessage.message)
    $("#messageModal").addClass("modal"+pageMessage.type);
    $("#messageModal").show()

}


function submitLoginForm() {
    
    $("#submitLoginForm").click(function() {
        var inputUsername = $("#usernameInput").val();
        var inputPassword = $("#passwordInput").val();

        $("#id_username").val(inputUsername);
        $("#id_password").val(inputPassword);
        
        $("#loginForm").submit();

    });
    
}
