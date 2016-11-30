function handlePanelSlide(eventName) {
	$("#" + eventName + "_panelToggle").click(function() {
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
        $("#" + eventName + "_panel").slideToggle();
	});

}


function sortEventLeaders(eventName, data) {

	var dataForEvent = data[eventName];

	var orderable = [];

	for (team in dataForEvent["teamData"]) {
		orderable.push(dataForEvent["teamData"][team]);
	}

	orderable.sort(function(a, b) {

		return a["score"] - b["score"];

	});

	orderable.sort(function(a, b) {
		if (a["score"] == b["score"]) {
			return a["boardsFor"] - b["boardsFor"];
		}
	});

	return orderable.reverse();

}

function populateEventLeaderTable(eventName, data) {

	var leaderData = sortEventLeaders(eventName, data);

	for (var i = 0; i < leaderData.length; i++) {
		
		var currentEntry = leaderData[i];

		var newRow = "<tr>" +
			"<td>" + currentEntry["name"] + "</td>" +
			"<td>" + currentEntry["score"] + "</td>" +
			"<td>" + currentEntry["boardsFor"] + "</td>" +
			"<td>" + currentEntry["boardsAgainst"] + "</td>" +
			"</tr>";

		$("[id='" + eventName + "_leaderTable']").append(newRow);
		
	}

}

function sortFixturesByDate(eventName, data) {

	var fixtureData = data[eventName]["fixtureData"];

	var orderable = [];

	for (fixture in fixtureData) {
		orderable.push(fixtureData[fixture]);
	}

	orderable.sort(function(a, b) {

		var aDate = new Date(a["date"]);
		var bDate = new Date(b["date"]);

		return aDate - bDate;

	});
	
	return orderable.reverse();

}


function populateFixtureTable(eventName, data) {
	
	var fixtureData = sortFixturesByDate(eventName, data);

	for (var i = 0; i < fixtureData.length; i++) {
		
		var currentEntry = fixtureData[i];

		var newRow = "<tr>" +
			"<td>" + currentEntry["date"] + "</td>" +
			"<td>" + currentEntry["homeTeamName"] + "</td>" +
			"<td>" + currentEntry["awayTeamName"] + "</td>" +
			"<td>" + currentEntry["homeBoards"].toString() + "</td>" +
			"<td>" + currentEntry["awayBoards"].toString() + "</td>" +
			"</tr>";

		$("[id='" + eventName + "_fixtureTable']").append(newRow);
		
	}
}