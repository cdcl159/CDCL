from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
	title = models.CharField(max_length = 50)
	creator = models.OneToOneField(User)
	creationDateTime = models.DateTimeField()
	body = models.CharField(max_length = 5000)



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
	Address_1 = models.CharField(max_length = 100, null = True)
	Address_2 = models.CharField(max_length = 100, null = True)
	Address_3 = models.CharField(max_length = 100, null = True)
	Postcode = models.CharField(max_length = 100, null = True)
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

	



class Player(models.Model):


	# link to site-user object
	user = models.OneToOneField(User, null=True)

	# names for player
	forenames = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)

	# code and rating given externally
	ecfCode = models.CharField(max_length=8)
	grading = models.IntegerField()

	# key to owner club
	club = models.ForeignKey(Club)


class Season(models.Model):

	name = models.CharField(max_length=10)
	
	startDate = models.DateField(null = True)
	endDate = models.DateField(null = True)



class Event(models.Model):

	name = models.CharField(max_length=20)






class Team(models.Model):

	name = models.CharField(max_length=30)

	captain = models.ForeignKey(Player, null=True)
	club = models.ForeignKey(Club, null=True)
	


class Submission(models.Model):

	# teach which made the submission
	team = models.ForeignKey(Team)


class Game(models.Model):

	# board number of game in fixture
	boardNumber = models.IntegerField()

	# player ids
	blackPlayerID = models.IntegerField()
	whitePlayerID = models.IntegerField()

	# player scores
	blackPlayerScore = models.FloatField()
	whitePlayerScore = models.FloatField()

	# submission to which the game belongs
	submission = models.ForeignKey(Submission)



class Fixture(models.Model):

	# date on which the fixture is played on
	date = models.DateField()

	# teams playing the fixture
	homeTeam = models.ForeignKey(Team, related_name="homeTeam", null=True)
	awayTeam = models.ForeignKey(Team, related_name="awayTeam", null=True)

	# score (based on outcome of the games)
	homeScore = models.IntegerField(null=True)
	awayScore = models.IntegerField(null=True)

	# event to which the fixture belongs
	event = models.ForeignKey(Event, null=True)

	# season in which the fixture took place
	season = models.ForeignKey(Season, null=True)

	# status of the fixture (played, approved, postponed pending etc)
	status = models.CharField(max_length=15)

	# submissions from teams (hold game results)
	homeSubmission = models.OneToOneField(Submission, related_name="homeSubmission", null=True)
	awaySubmission = models.OneToOneField(Submission, related_name="awaySubmission", null=True)

