
function submitLoginForm() {
    
    $("#submitLoginForm").click(function() {
        var inputUsername = $("#usernameInput").val();
        var inputPassword = $("#passwordInput").val();

        $("#id_inputUsername").val(inputUsername);
        $("#id_inputPassword").val(inputPassword);
        
        $("#loginForm").submit();

    });
    
}


function processErrorString(errorString) {
    
    if (errorString == "FORM_INVALID") {
        $("#errorMessage").text("Please ensure all fields in form are complete.");
        $("#errorTitle").text("INCOMPLETE FORM");
    }
    if (errorString == "ACCOUNT_INACTIVE") {
        $("#errorMessage").text("Account not active. Please contact site admin.");
        $("#errorTitle").text("ACCOUNT INACTIVE");
    }
    if (errorString == "ACCOUNT_ERROR") {
        $("#errorMessage").text("Username or password incorrect.");
        $("#errorTitle").text("INCORRECT DETAILS");
    }
    
    if (errorString != "NO_ERROR") {
        $("#errorModal").modal("show");
    }
    

}