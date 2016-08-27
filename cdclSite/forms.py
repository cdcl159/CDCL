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

	selectedFixtureID = forms.IntegerField(required = False)

	board1_homePlayerID = forms.IntegerField(required = False)
	board2_homePlayerID = forms.IntegerField(required = False)
	board3_homePlayerID = forms.IntegerField(required = False)
	board4_homePlayerID = forms.IntegerField(required = False)
	board5_homePlayerID = forms.IntegerField(required = False)
	board6_homePlayerID = forms.IntegerField(required = False)

	board1_awayPlayerID = forms.IntegerField(required = False)
	board2_awayPlayerID = forms.IntegerField(required = False)
	board3_awayPlayerID = forms.IntegerField(required = False)
	board4_awayPlayerID = forms.IntegerField(required = False)
	board5_awayPlayerID = forms.IntegerField(required = False)
	board6_awayPlayerID = forms.IntegerField(required = False)

	board1_homePlayerScore = forms.IntegerField(required = False)
	board2_homePlayerScore = forms.IntegerField(required = False)
	board3_homePlayerScore = forms.IntegerField(required = False)
	board4_homePlayerScore = forms.IntegerField(required = False)
	board5_homePlayerScore = forms.IntegerField(required = False)
	board6_homePlayerScore = forms.IntegerField(required = False)

	board1_awayPlayerScore = forms.IntegerField(required = False)
	board2_awayPlayerScore = forms.IntegerField(required = False)
	board3_awayPlayerScore = forms.IntegerField(required = False)
	board4_awayPlayerScore = forms.IntegerField(required = False)
	board5_awayPlayerScore = forms.IntegerField(required = False)
	board6_awayPlayerScore = forms.IntegerField(required = False)
	
	homeTeam = forms.CharField(required = False, max_length = 100)
	awayTeam = forms.CharField(required = False, max_length = 100)

class UserManagementToolsForm(forms.Form):

	selectedUserId = forms.IntegerField(required = False)

	activeMode = forms.BooleanField(required = False)
	superuserMode = forms.BooleanField(required = False)
	officerMode = forms.BooleanField(required = False)
	recordsMode = forms.BooleanField(required = False)
	treasurerMode = forms.BooleanField(required = False)


class RegistrationForm(forms.Form):
	
	# NEED TO ADJUST MAX LENGTHS
	username = forms.CharField(required = True, max_length = 100)
	password = forms.CharField(required = True, max_length = 100)
	passwordConfirm = forms.CharField(required = True, max_length = 100)

	forenames = forms.CharField(required = True, max_length = 100)
	surname = forms.CharField(required = True, max_length = 100)
	address_1 = forms.CharField(required = False, max_length = 100)
	address_2 = forms.CharField(required = False, max_length = 100)
	address_3 = forms.CharField(required = False, max_length = 100)
	postcode = forms.CharField(required = False, max_length = 100)
	primaryContactNumber = forms.CharField(required = False, max_length = 100)
	backupContactNumber = forms.CharField(required = False, max_length = 100)
	email = forms.CharField(required = False, max_length = 100)

	ecfCode = forms.CharField(required = False, max_length = 100)
	club = forms.IntegerField(required = False)


class AnnouncementForm(forms.Form):

	title = forms.CharField(required = True, max_length = 50)
	body = forms.CharField(required = True, max_length = 5000)
	postTo = forms.CharField(required = True, max_length = 1)