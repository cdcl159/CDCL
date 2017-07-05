from cdclSite.models import *
import csv

def report_all(output_filename):
	output = []

	for fixture in Fixture.objects.all():
		
		fixture_data = {}
		fixture_data["hometeam"] = fixture.homeTeam.name
		fixture_data["awayteam"] = fixture.awayTeam.name
		fixture_data["date"] = str(fixture.date)
		fixture_data["event"] = fixture.event.name
		fixture_data["season"] = fixture.season.name

		games = []
		for game in fixture.homeSubmission.game_set.all():
			homeplayer = Player.objects.get(id = game.homePlayerID)
			awayplayer = Player.objects.get(id = game.awayPlayerID)
			games.append(
				{
					"boardnumber": game.boardNumber,
					"homeplayer": {
						"id": game.homePlayerID,
						"name": homeplayer.forenames + " " + homeplayer.surname,
						"ecf": homeplayer.ecfCode,
						"score": game.homePlayerScore
					},
					"awayplayer": {
						"id": game.awayPlayerID,
						"name": awayplayer.forenames + " " + awayplayer.surname,
						"ecf": awayplayer.ecfCode,
						"score": game.awayPlayerScore
					},

					
				}
			)
		
		fixture_data["games"] = games
	
		output.append(fixture_data)

	with open(output_filename, "w+") as f:
		writer = csv.writer(f)

		writer.writerow(
			[
				"season",
				"event",
				"date",
				"hometeam",
				"awayteam",
				"boardnumber",
				"homeplayer_id"
				"homeplayer_name",
				"homeplayer_ecf",
				"homeplayer_score",
				"awayplayer_id",
				"awayplayer_name",
				"awayplayer_ecf",
				"awayplayer_score"
			]
		)

		for fixture in output:

			for game in fixture["games"]:
				
				print game

				writer.writerow(
					[
						fixture["season"],
						fixture["event"],
						fixture["date"],
						fixture["hometeam"],
						fixture["awayteam"],
						game["boardnumber"],
						game["homeplayer"]["id"]
						game["homeplayer"]["name"],
						game["homeplayer"]["ecf"],
						game["homeplayer"]["score"],
						game["awayplayer"]["id"],
						game["awayplayer"]["name"],
						game["awayplayer"]["ecf"],
						game["awayplayer"]["score"]
					]
				)