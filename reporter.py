from cdclSite.models import *


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

	return output