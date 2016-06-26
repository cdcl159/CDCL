
function displayLoginModal() {
    
    $("#loginIcon").click(function() {
        $("#loginModal").modal("show");
    });
    
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
