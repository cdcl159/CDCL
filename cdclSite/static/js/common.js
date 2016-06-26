
function handlePageMessage(pageMessage) {

    if (pageMessage.type != "BLANK") {

        $("#messageTitle").text(pageMessage.type);
        $("#messageBody").text(pageMessage.message);
        $(".messageHeader").addClass("modal"+pageMessage.type);
        $("#messageModal").modal("show");
    }
}



function menuHover() {
    
    $(".menuIcon").mouseover(function() {
        
        $(".menuIcon").not(this).animate({opacity: '0.4'}, 250)
        
    });
    
    $(".menuIcon").mouseout(function() {
        
        $(".menuIcon").not(this).animate({opacity: '1'}, 250)
        
    });
    
    
}

function calcMenuHeight() {
    console.log($(document).height());
    console.log($(".topNavBar").height());
    $(".menuContainer").height($(document).height() - $(".topNavBar").height());

}