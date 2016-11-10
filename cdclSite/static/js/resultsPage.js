


function populateTable(eventName, data) {

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

	console.log(orderable);

}