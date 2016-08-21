from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

	username = forms.CharField(max_length = 100, required = True)
	password = forms.CharField(max_length = 100, required = True)



class ClubManagementForm(forms.Form):

	addMode = forms.BooleanField(required = False)
	editMode = forms.BooleanField(required = False)

	selectedClubID = forms.IntegerField(required = False)
	name = forms.CharField(max_length = 100, required = False)
	contactName = forms.CharField(max_length = 50, required = False)
	contactNumber = forms.CharField(max_length = 20, required = False)
	contactEmail = forms.CharField(max_length = 50, required = False)
	clubWebsite = forms.CharField(max_length = 100, required = False)
	clubNight = forms.CharField(max_length = 20, required = False)
	clubVenue = forms.CharField(max_length = 50, required = False)
	clubAddress = forms.CharField(max_length = 200, required = False)


class PlayerManagementForm(forms.Form):

	# bool values to determine how to process the form
	bulkMode = forms.BooleanField(required = False)
	addMode = forms.BooleanField(required = False)
	editMode = forms.BooleanField(required = False)

	# csv file of player details for bulk uploading player data
	playerFile = forms.FileField(required = False)

	# player details
	playerID = forms.IntegerField(required = False)
	playerForenames = forms.CharField(required = False, max_length = 100)
	playerSurname = forms.CharField(required = False, max_length = 100)
	playerEcfCode = forms.CharField(required = False, max_length = 8)
	playerGrading = forms.CharField(required = False)
	playerClub = forms.CharField(required = False, max_length = 100)


class FixtureManagementForm(forms.Form):

	# bool values to determine how to process the form
	bulkMode = forms.BooleanField(required = False)
	editMode = forms.BooleanField(required = False)
	addMode = forms.BooleanField(required = False)
	teamMode = forms.BooleanField(required = False)

	# csv file of fixtures
	fixtureFile = forms.FileField(required = False)
	newFixtureSeason = forms.CharField(required = False, max_length = 100)
	newFixtureDivision = forms.CharField(required = False, max_length = 100)
	newFixtureEvent = forms.CharField(required = False, max_length = 100)
	newFixtureDate = forms.CharField(required = False, max_length = 100)
	newFixtureHomeTeam = forms.CharField(required = False, max_length = 100)
	newFixtureAwayTeam = forms.CharField(required = False, max_length = 100)

	teamData = forms.CharField(required = False, max_length = 1000)


class ResultsSubmissionForm(forms.Form):

	pass
	# TODO!