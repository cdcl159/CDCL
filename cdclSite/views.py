from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse

from cdclSite.forms import *
from cdclSite.models import *
import datetime
import time
import json
import csv


# page displaying information about cdcl
def aboutPage(request):

	return render(request, "cdclSite/about.html")



# page displaying rules and constitution
def constitutionPage(request):

	return render(request, "cdclSite/constitution.html")



# page displaying all officers (should be made automated)
def officersPage(request):

	return render(request, "cdclSite/officers.html")



# page displaying all registered clubs
def clubsPage(request):

	return render(request, "cdclSite/clubs.html", {"clubs": Club.objects.all()})



# page displaying results so far
def resultsPage(request):

	return render(request, "cdclSite/results.html")



# main page (displays login form and announcements) 
def index(request):

	if request.method == "POST":

		loginForm = LoginForm(request.POST)

		if loginForm.is_valid():


			form_username = loginForm.cleaned_data["username"]
			form_password = loginForm.cleaned_data["password"]

			authenticatedUser = authenticate(username=form_username, password=form_password)

			if authenticatedUser:
				login(request, authenticatedUser)

				return HttpResponseRedirect("../dashboard")

			else:
				pageMessage = {
					"type": "WARNING", "message": "Username or password incorrect.\n"+
					"Please apply for an account if not already a member."
				}


		else:
			pageMessage = {
				"type": "ERROR",
				"message": "The login form was invalid.\n" +
				"Please make sure you have entered both your username and password."
			}

	else:

		pageMessage = {"type": "BLANK", "message": "NOTHING"}

		loginForm = LoginForm()


	return render(request, "cdclSite/index.html", {"loginForm": loginForm, "pageMessage": json.dumps(pageMessage)})



# logs out the user and redirects them to the index page
def logoutPage(request):
	
	logout(request)
	return HttpResponseRedirect("../")



# displays player stats and links to other sections of system
@login_required(login_url='index')
def dashboard(request):

	pageMessage = {"type": "BLANK", "message": "NOTHING"}

	return render(request, "cdclSite/dashboard.html", {"pageMessage": json.dumps(pageMessage)})



@login_required(login_url='index')
def announcementsPage(request):

	pageMessage = {"type": "BLANK", "message": "NOTHING"}

	return render(request, "cdclSite/announcementsPage.html", {"pageMessage": json.dumps(pageMessage)}) 



# displays tools for managing/adding clubs
@login_required(login_url='index')
def clubManagement(request):

	if request.method == "POST":
		
		clubManagementForm = ClubManagementForm(request.POST)

		if clubManagementForm.is_valid():

			# get data from form
			form_addMode = clubManagementForm.cleaned_data["addMode"]
			form_editMode = clubManagementForm.cleaned_data["editMode"]
			form_selectedClubID = clubManagementForm.cleaned_data["selectedClubID"]
			form_name = clubManagementForm.cleaned_data["name"]
			form_contactName = clubManagementForm.cleaned_data["contactName"]
			form_contactNumber = clubManagementForm.cleaned_data["contactNumber"]
			form_contactEmail = clubManagementForm.cleaned_data["contactEmail"]
			form_clubWebsite = clubManagementForm.cleaned_data["clubWebsite"]
			form_clubNight = clubManagementForm.cleaned_data["clubNight"]
			form_clubVenue = clubManagementForm.cleaned_data["clubVenue"]
			form_clubAddress = clubManagementForm.cleaned_data["clubAddress"]

			# use data to create a new club
			if form_addMode:

				try:

					newClub = Club.objects.create(
						name = form_name,
						contactName = form_contactName,
						contactNumber = form_contactNumber,
						contactEmail = form_contactEmail,
						website = form_clubWebsite,
						night = form_clubNight,
						venue = form_clubVenue,
						address = form_clubAddress
					)
				
				except Exception as e:
					
					pageMessage = {"type": "ERROR", "message": "The new club could not be added to the database: " + str(e)}

				else:
					
					pageMessage = {"type": "SUCCESS", "message": "The new club was added to the database successfully."}

			if form_editMode:

				try:

					selectedClub = Club.objects.get(id = int(form_selectedClubID))
					selectedClub.name = form_name
					selectedClub.contactName = form_contactName
					selectedClub.contactNumber = form_contactNumber
					selectedClub.contactEmail = form_contactEmail
					selectedClub.website = form_clubWebsite
					selectedClub.night = form_clubNight
					selectedClub.venue = form_clubVenue
					selectedClub.address = form_clubAddress

					selectedClub.save()

				except Exception as e:

					pageMessage = {"type": "ERROR", "message": "The club details could not be changed in the database:" + str(e)}

				else:

					pageMessage = {"type": "SUCCESS", "message": "The club details were changed in the database successfully."}

		else:
			
			pageMessage = {
				"type": "ERROR",
				"message": "The club form was invalid.\n Please ensure the fields were filled out correctly."
			}

	else:

		pageMessage = {"type": "BLANK", "message": "NOTHING"}

		clubManagementForm = ClubManagementForm()
	

	clubData = {}
	for club in Club.objects.all():

		clubData[club.id] = {
			"name": club.name,
			"contactName": club.contactName,
			"contactNumber": club.contactNumber,
			"contactEmail": club.contactEmail,
			"website": club.website,
			"night": club.night,
			"venue": club.venue,
			"address": club.address
		}
	
	return render(request,
		"cdclSite/clubManagement.html",
		{
			"clubManagementForm": clubManagementForm,
			"pageMessage": json.dumps(pageMessage),
			"clubData": json.dumps(clubData)
		})



# displays tools for managing players
@login_required(login_url='index')
def playerManagement(request):

	if request.method == "POST":
		
		playerManagementForm = PlayerManagementForm(request.POST, request.FILES)

		if playerManagementForm.is_valid():

			# form processing flags
			form_bulkMode = playerManagementForm.cleaned_data["bulkMode"]
			form_addMode = playerManagementForm.cleaned_data["addMode"]
			form_editMode = playerManagementForm.cleaned_data["editMode"]

			# player details
			form_playerID = playerManagementForm.cleaned_data["playerID"]
			form_playerForenames = playerManagementForm.cleaned_data["playerForenames"]
			form_playerSurname = playerManagementForm.cleaned_data["playerSurname"]
			form_playerEcfCode = playerManagementForm.cleaned_data["playerEcfCode"]
			form_playerGrading = playerManagementForm.cleaned_data["playerGrading"]
			form_playerClub = playerManagementForm.cleaned_data["playerClub"]

			# uploaded file of player data
			form_playerFile = playerManagementForm.cleaned_data["playerFile"]


			# if editMode is true, get the selected player

			if form_editMode:

				try:

					selectedPlayer = Player.objects.get(id=form_playerID)

				except Exception as e:

					pageMessage = {"type": "ERROR", "message": "The selected player could not be found in the database."}

				else:

					try:

						selectedPlayer.forenames = form_playerForenames
						selectedPlayer.surname = form_playerSurname
						selectedPlayer.ecfCode = form_playerEcfCode
						selectedPlayer.grading = int(form_playerGrading)
						selectedPlayer.club = Club.objects.get(name=form_playerClub)

						selectedPlayer.save()

					except Exception as e:

						pageMessage = {"type": "ERROR", "message": "The changes could not be made to the selected player."}

					else:

						pageMessage = {"type": "SUCCESS", "message": "The changes were made successfully."}

			# if addMode is trye, use the player details from the from to create a new player
			if form_addMode:

				try:

					newPlayer = Player.objects.create(
						forenames = form_playerForenames,
						surname = form_playerSurname,
						ecfCode = form_playerEcfCode,
						grading = int(form_playerGrading),
						club = Club.objects.get(name=form_playerClub)
					)

				except Exception as e:

					pageMessage = {"type": "ERROR", "message": "The new player could not be made with these details."}

				else:

					pageMessage = {"type": "SUCCESS", "message": "The new player was created successfully."}



			# if bulkMode is true, a file has been submitted
			if form_bulkMode:


				try:

					newPlayerFile = PlayerFile.objects.create(playerFile=request.FILES['playerFile'])
					
					with open(newPlayerFile.playerFile.path) as csvFile:
						reader = csv.reader(csvFile)
						playersData = [row for row in reader]

					for row in playersData[1:]:

						try:

							existing = Player.objects.get(ecfCode=row[0])

						except Player.DoesNotExist:

							newPlayer = Player.objects.create(
								forenames = row[1],
								surname = row[2],
								ecfCode = row[0],
								grading = row[3],
								club = Club.objects.get(name=row[4])
							)

						else:

							pass

				except Exception as e:
					pageMessage = {
						"type": "ERROR",
						"message": "The players could not be added: " + str(e)
					}

				else:
					pageMessage = {
						"type": "SUCCESS",
						"message": "The players were added."
					}

		else:
			pageMessage = {
				"type": "ERROR",
				"message": "Bad Form"
			}
			

	else:

		pageMessage = {"type": "BLANK", "message": "NOTHING"}

		playerManagementForm = PlayerManagementForm()

	playerData = {}

	for player in Player.objects.all():

		playerData[player.id] = {
			"forenames": player.forenames,
			"surname": player.surname,
			"ecfCode": player.ecfCode,
			"grading": player.grading,
			"club": player.club.name
		}


	return render(request, "cdclSite/playerManagement.html", {"pageMessage": json.dumps(pageMessage), "players": json.dumps(playerData), "playerManagementForm": playerManagementForm})



# displays tools for managing fixtures
@login_required(login_url='index')
def fixtures(request):

	if request.method == "POST":
		
		fixtureManagementForm = FixtureManagementForm(request.POST, request.FILES)

		if fixtureManagementForm.is_valid():

			form_bulkMode = fixtureManagementForm.cleaned_data["bulkMode"]
			form_editMode = fixtureManagementForm.cleaned_data["editMode"]
			form_addMode = fixtureManagementForm.cleaned_data["addMode"]
			form_fixtureFile = fixtureManagementForm.cleaned_data["fixtureFile"]
			form_teamMode = fixtureManagementForm.cleaned_data["teamMode"]
			form_teamData = fixtureManagementForm.cleaned_data["teamData"]

			if form_teamMode:

				teamData = json.loads(form_teamData)

				try:

					for t in teamData:

						team = Team.objects.get(id = t)

						team.club = Club.objects.get(id = teamData[t]["clubID"])

						team.captain = Player.objects.get(id = teamData[t]["captainID"])

						team.save()

				except Exception as e:

					pageMessage = {
						"type": "ERROR",
						"message": "Some or all of the teams could not be edited: " + str(e)
					}

				else:

					pageMessage = {
						"type": "SUCCESS",
						"message": "The teams were edited successfully."
					}

			# if editMode is true, get the selected player
			if form_editMode:

				pass

			# if addMode is true, use the player details from the from to create a new player
			if form_addMode:
				pass

			# if bulkMode is true, a file has been submitted
			if form_bulkMode:

				try:

					newFixtureFile = FixtureFile.objects.create(fixtureFile=request.FILES['fixtureFile'])

					# test text replacement
					with open(newFixtureFile.fixtureFile.path) as csvFile:
						reader = csv.reader(csvFile)
						fixturesData = [row for row in reader]
					
					for row in fixturesData[1:]:

						# find or create the required teams
						try:
							homeTeam = Team.objects.get(name=str(row[3].title()))
						except Team.DoesNotExist:
							homeTeam = Team.objects.create(name=str(row[3]).title())
						else:
							homeTeam = Team.objects.get(name=str(row[3].title()))

						try:
							awayTeam = Team.objects.get(name=str(row[4].title()))
						except Team.DoesNotExist:
							awayTeam = Team.objects.create(name=str(row[4]).title())
						else:
							awayTeam = Team.objects.get(name=str(row[4].title()))

						# find or create the event
						try:
							locatedEvent = Event.objects.get(name=str(row[0].title()))
						except Event.DoesNotExist:
							locatedEvent = Event.objects.create(name=str(row[0].title()))
						else:
							pass
						
						# find or create the season
						try:
							locatedSeason = Season.objects.get(name=str(row[1]))
						except Season.DoesNotExist:
							locatedSeason = Season.objects.create(name=str(row[1]))
						else:
							pass
						
						# create the new fixture
						newFixture = Fixture.objects.create(
								date = datetime.datetime.strptime(row[2], "%d/%m/%Y"),
								homeTeam = homeTeam,
								awayTeam = awayTeam,
								season = locatedSeason,
								event = locatedEvent,
								status = "PENDING"
							)
						
				except Exception as e:
					pageMessage = {
						"type": "ERROR",
						"message": "One or more fixture could not be added: " + str(e)
					}
					

				else:
					pageMessage = {
						"type": "SUCCESS",
						"message": "All fixtures added successfully."
					}

		else:

			pageMessage = {
				"type": "ERROR",
				"message": "Bad Form"
			}

	else:

		pageMessage = {"type": "BLANK", "message": "NOTHING"}

		fixtureManagementForm = FixtureManagementForm()

	players = {}

	for p in Player.objects.all():

		players[p.id] = {
			"name": p.forenames + ", " + p.surname,
			"club": p.club.name
		}



	return render(request, "cdclSite/fixtures.html",
		{
			"fixtureManagementForm": fixtureManagementForm,
			"pageMessage": json.dumps(pageMessage),
			"events": Event.objects.all(),
			"seasons": Season.objects.all(),
			"fixtures": Fixture.objects.all(),
			"clubs": Club.objects.all(),
			"teams": Team.objects.all(),
			"players": json.dumps(players),
		})



# displays forms for captains to upload match results
@login_required(login_url='index')
def resultsSubmission(request):

	pageMessage = {"type": "BLANK", "message": "NOTHING"}

	fixtureData = {}

	for fixture in Fixture.objects.all():
		# if fixture.homeTeam.captain == request.user.player or fixture.awayTeam.captain == request.user.player:

		fixtureData[fixture.id] = {
			"date": str(fixture.date),
			"homeTeam": {"name": fixture.homeTeam.name, "club": fixture.homeTeam.club.name},
			"awayTeam": {"name": fixture.awayTeam.name, "club": fixture.awayTeam.club.name},
			"event": fixture.event.name
		}

	playerData = {}

	for player in Player.objects.all():
		
		playerData[player.id] = {
			"name": player.forenames + ", " + player.surname,
			"club": player.club.name,
			"grading": player.grading

		}


	return render(request, "cdclSite/resultsSubmission.html",
		{
			"pageMessage": json.dumps(pageMessage),
			"fixtureData": json.dumps(fixtureData),
			"playerData": json.dumps(playerData)
		})



# displays tools to keep user data up to date
@login_required(login_url='index')
def userDetails(request):
	
	pageMessage = {"type": "BLANK", "message": "NOTHING"}

	return render(request, "cdclSite/userDetails.html", {"pageMessage": json.dumps(pageMessage)})