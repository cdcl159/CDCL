

function initUI() {
    
    $("#constitutionBody").slideUp();
    $("#leaguePlayBody").slideUp();
    $("#chaseTrophyBody").slideUp();
    $("#robertWardBody").slideUp();

}

function handlePanelToggles() {
    
    $("#constitutionToggle").click(function() {
        if ($(this).hasClass("down")) {
            var newSrc = $(this).attr("src").replace("downArrow", "upArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("down");
            $(this).addClass("up");
        } else {
            var newSrc = $(this).attr("src").replace("upArrow", "downArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("up");
            $(this).addClass("down");
        }
        $("#constitutionBody").slideToggle();
    });

    $("#leaguePlayToggle").click(function() {
        if ($(this).hasClass("down")) {
            var newSrc = $(this).attr("src").replace("downArrow", "upArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("down");
            $(this).addClass("up");
        } else {
            var newSrc = $(this).attr("src").replace("upArrow", "downArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("up");
            $(this).addClass("down");
        }
        $("#leaguePlayBody").slideToggle();
    });

    $("#chaseTrophyToggle").click(function() {
        if ($(this).hasClass("down")) {
            var newSrc = $(this).attr("src").replace("downArrow", "upArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("down");
            $(this).addClass("up");
        } else {
            var newSrc = $(this).attr("src").replace("upArrow", "downArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("up");
            $(this).addClass("down");
        }
        $("#chaseTrophyBody").slideToggle();
    });

    $("#robertWardToggle").click(function() {
        if ($(this).hasClass("down")) {
            var newSrc = $(this).attr("src").replace("downArrow", "upArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("down");
            $(this).addClass("up");
        } else {
            var newSrc = $(this).attr("src").replace("upArrow", "downArrow");
            $(this).attr("src", newSrc);
            $(this).removeClass("up");
            $(this).addClass("down");
        }
        $("#robertWardBody").slideToggle();
    });
}