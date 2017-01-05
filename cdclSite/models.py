from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class SiteAnnouncement(models.Model):
	title = models.CharField(max_length = 50)
	creator = models.ForeignKey(User)
	creationDateTime = models.DateTimeField()
	body = models.CharField(max_length = 5000)
	postTo = models.CharField(max_length = 1)



class PlayerFile(models.Model):
	playerFile = models.FileField(upload_to='.')


class FixtureFile(models.Model):
	fixtureFile = models.FileField(upload_to=".")


class UserData(models.Model):

	# link to site-user object
	user = models.OneToOneField(User, null = True)

	# post news/announcements, emails
	isOfficer = models.BooleanField(default = False)
	
	# data management
	isRecordSecretary = models.BooleanField(default = False)

	# finance management
	isTreasurer = models.BooleanField(default = False)

	forenames = models.CharField(max_length = 100, null = True)
	surname = models.CharField(max_length = 100, null = True)
	primaryContactNumber = models.CharField(max_length = 100, null = True)
	backupContactNumber = models.CharField(max_length = 100, null = True)
	email = models.CharField(max_length = 100, null = True)


class Club(models.Model):

	# name of club
	name = models.CharField(max_length = 100)

	# contact details for club
	contactName = models.CharField(max_length = 50)
	contactNumber = models.CharField(max_length = 20)
	contactEmail = models.CharField(max_length = 50)

	# club details
	website = models.CharField(max_length = 100, default = "")
	night = models.CharField(max_length = 20)
	venue = models.CharField(max_length = 50)
	address = models.CharField(max_length = 200)

	code = models.CharField(max_length = 8, null = True)

	



class Player(models.Model):

	# link to site-user object
	user = models.OneToOneField(User, null = True)

	# names for player
	forenames = models.CharField(max_length = 100)
	surname = models.CharField(max_length = 100)

	# code and rating given externally
	ecfCode = models.CharField(max_length = 8)
	grading = models.IntegerField()

	# key to owner club
	club = models.ForeignKey(Club)

	isCaptain = models.BooleanField(default = False)


	def getResults(self):
		
		results = {
			"homeTotal": 0,
			"awayTotal": 0,
			"historic": []
		}

		fixtures = []

		for f in Fixture.objects.all():

			if f.homeTeam.club == self.club or f.awayTeam.club == self.club:

				if f.status == "APPROVED":

					fixtures.append(f)

		for f in fixtures:

			for g in fixture.homeSubmission.game_set.all():

				if g.homePlayerID == self.id:

					results["homeTotal"] += g.homePlayerScore
					results["historic"].append(
						{
							"date": f.date,
							"score": g.homePlayerScore,
							"opponentName": Player.objects.get(id = g.awayPlayerID).name
						}
					)

				elif g.awayPlayerID == self.id:
					results["awayTotal"] += g.awayPlayerScore
					results["historic"].append(
						{
							"date": f.date,
							"score": g.awayPlayerScore,
							"opponentName": Player.objects.get(id = g.homePlayerID).name
						}
					)

				else:

					pass

		return results



class Season(models.Model):

	name = models.CharField(max_length = 10)
	
	startDate = models.DateField(null = True)
	endDate = models.DateField(null = True)


	def aggregateResults(self):

		seasonResults = {}

		seasonFixtures = self.fixture_set.all()

		for f in seasonFixtures:

			if f.homeTeam.name not in teamScores:

				seasonResults[f.homeTeam.name] = {
					"total": 0,
					"fixtureResults": []
				}
			
			if f.awayTeam.name not in teamScores:

				seasonResults[f.awayTeam.name] = {
					"total": 0,
					"fixtureResults": []
				}


			seasonResults[f.homeTeam.name]["fixtureResults"].append({"date": f.date, "result": f.homeScore})

			seasonResults[f.homeTeam.name]["total"] += f.homeScore
			
			seasonResults[f.awayTeam.name]["fixtureResults"].append({"date": f.date, "result": f.awayScore})

			seasonResults[f.awayTeam.name]["total"] += f.awayScore

		
		return seasonResults




class Event(models.Model):

	name = models.CharField(max_length = 20)






class Team(models.Model):

	name = models.CharField(max_length = 30)

	captain = models.ForeignKey(Player, null = True)
	club = models.ForeignKey(Club, null = True)
	


class Submission(models.Model):

	# teach which made the submission
	team = models.ForeignKey(Team)


class Game(models.Model):

	# board number of game in fixture
	boardNumber = models.IntegerField()

	# player ids
	homePlayerID = models.IntegerField()
	awayPlayerID = models.IntegerField()

	# player scores
	homePlayerScore = models.FloatField()
	awayPlayerScore = models.FloatField()

	# submission to which the game belongs
	submission = models.ForeignKey(Submission)



class Fixture(models.Model):

	# date on which the fixture is played on
	date = models.DateField()

	# teams playing the fixture
	homeTeam = models.ForeignKey(Team, related_name = "homeTeam", null = True)
	awayTeam = models.ForeignKey(Team, related_name = "awayTeam", null = True)

	# score (based on outcome of the games)
	homeScore = models.IntegerField(null = True)
	awayScore = models.IntegerField(null = True)

	# event to which the fixture belongs
	event = models.ForeignKey(Event, null = True)

	# season in which the fixture took place
	season = models.ForeignKey(Season, null = True)

	# status of the fixture (played, approved, postponed pending etc)
	status = models.CharField(max_length = 15)

	# submissions from teams (hold game results)
	homeSubmission = models.OneToOneField(Submission, related_name = "homeSubmission", null = True)
	awaySubmission = models.OneToOneField(Submission, related_name = "awaySubmission", null = True)

