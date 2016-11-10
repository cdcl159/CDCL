


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
	console.log("ld:");
	console.log(leaderData);
	console.log("- - - ");

	for (var i = 0; i < leaderData.length; i++) {
		
		var currentEntry = leaderData[i];
		console.log("ce:");
		console.log(currentEntry);
		console.log("- - - ");

		var newRow = "<tr>" +
			"<td>" + currentEntry["name"] + "</td>" +
			"<td>" + currentEntry["score"] + "</td>" +
			"<td>" + currentEntry["boardsFor"] + "</td>" +
			"<td>" + currentEntry["boardsAgainst"] + "</td>" +
			"</tr>";

		console.log("nr:");
		console.log(newRow);
		console.log("- - - ")

		$("#" + eventName +"_leaderTable").append(newRow);
		
	}

}