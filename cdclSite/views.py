from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse

from cdclSite.forms import *
from cdclSite.models import *
import pprint
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


def registrationPage(request):

	if request.method == "POST":

		registrationForm = RegistrationForm(request.POST)

		if registrationForm.is_valid():

			form_username = registrationForm.cleaned_data["username"]
			form_password = registrationForm.cleaned_data["password"]
			form_passwordConfirm = registrationForm.cleaned_data["passwordConfirm"]
			form_forenames = registrationForm.cleaned_data["forenames"]
			form_surname = registrationForm.cleaned_data["surname"]
			form_primaryContactNumber = registrationForm.cleaned_data["primaryContactNumber"]
			form_backupContactNumber = registrationForm.cleaned_data["backupContactNumber"]
			form_email = registrationForm.cleaned_data["email"]
			form_ecfCode = registrationForm.cleaned_data["ecfCode"]
			form_club = registrationForm.cleaned_data["club"]

			if form_password != form_passwordConfirm:

				pageMessage = {
					"type": "ERROR",
					"message": "The password and confirmed password did not match."
				}

			else:

				try:

					newUser = User.objects.create_user(username = form_username, password = form_password)

					newUser.is_active = False
					newUser.save()
				
				except Exception as e:

					pageMessage = {
						"type": "ERROR",
						"message": "User account could not be created: " + str(e)
					}
				
				else:

					try:

						newUserData = UserData.objects.create(
							user = newUser,
							forenames = form_forenames,
							surname = form_surname,
							primaryContactNumber = form_primaryContactNumber,
							backupContactNumber = form_backupContactNumber,
							email = form_email
						)
					
					except Exception as e:

						pageMessage = {
							"type": "WARNING",
							"message": "Account created but user data (forenames, surname address etc) could not be created. " + str(e)
						}

					else:

						try:
							
							userPlayer = Player.objects.get(ecfCode = form_ecfCode)

							userPlayer.user = newUser

							userPlayer.save()

						except Player.DoesNotExist:
							
							if form_ecfCode:
								
								try:
									userPlayer = Player.objects.create(
										user = newUser,
										forenames = form_forenames,
										surname = form_surname,
										ecfCode = form_ecfCode,
										club = Club.objects.get(id = form_club)
									)
								except Exception as e:

									pageMessage = {
										"type": "WARNING",
										"message": "User account created but corresponding player data could not be formed."
									}
								
								else:

									pageMessage = {
										"type": "SUCCESS",
										"message": "User account and player data was created successfully."
									}

							
							else:

								try:

									userPlayer = Player.objects.create(
										user = newUser,
										forenames = form_forenames,
										surname = form_surname,
										club = Club.objects.get(id = form_club)
									)
								except Exception as e:

									pageMessage = {
										"type": "WARNING",
										"message": "User account created but corresponding player data could not be formed."
									}
								
								else:

									pageMessage = {
										"type": "SUCCESS",
										"message": "User account and player data was created successfully."
									}
						else:

							pageMessage = {
								"type": "SUCCESS",
								"message": "Account created successfully."
							}
		else:

			pageMessage = {
				"type": "ERROR",
				"message": "One or more fields in the form were not completed correctly."
			}

	else:

		registrationForm = RegistrationForm()

		pageMessage = {
			"type": "BLANK",
			"message": "NOTHING"
		}

	return render(
		request,
		"cdclSite/registration.html",
		{
			"registrationForm": registrationForm,
			"pageMessage": json.dumps(pageMessage),
			"clubs": Club.objects.all()
		}
	)


# main page (displays login form and announcements) 
def index(request):

	if request.method == "POST":

		loginForm = LoginForm(request.POST)

		if loginForm.is_valid():


			form_username = loginForm.cleaned_data["username"]
			form_password = loginForm.cleaned_data["password"]

			authenticatedUser = authenticate(username = form_username, password = form_password)

			if authenticatedUser:
				
				if authenticatedUser.is_active:

					login(request, authenticatedUser)

					return HttpResponseRedirect("../dashboard")

				else:


					pageMessage = {
						"type": "WARNING",
						"message": "Account not active. If you have recently registered, your account application is under review and may not yet be approved. Otherwise, please contact site admin."
					}

			else:
				pageMessage = {
					"type": "WARNING",
					"message": "Username or password incorrect. Please apply for an account if not already a member."
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


	return render(
		request,
		"cdclSite/index.html",
		{
			"loginForm": loginForm,
			"pageMessage": json.dumps(pageMessage),
			"announcements": reversed(list(SiteAnnouncement.objects.filter(postTo = "m")))
		}
	)


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

	if request.method == "POST":

		announcementForm = AnnouncementForm(request.POST)

		if announcementForm.is_valid():

			form_title = announcementForm.cleaned_data["title"]
			form_body = announcementForm.cleaned_data["body"]
			form_postTo = announcementForm.cleaned_data["postTo"]

			try:

				newAnnouncement = SiteAnnouncement.objects.create(
					title = form_title,
					creator = request.user,
					creationDateTime = datetime.datetime.now(),
					body = form_body,
					postTo = form_postTo
				)
				
			except Exception as e:

				pageMessage = {
					"type": "ERROR",
					"message": "The new announcement could not be created: " + str(e)
				}

			else:

				pageMessage = {
					"type": "SUCCESS",
					"message": "The new announcement was created successfully"
				}
		
		else:

			pageMessage = {
				"type": "ERROR",
				"message": "The form could not be submitted. Please make sure all fields are complete."
			}

	else:

		announcementForm = AnnouncementForm()

		pageMessage = {"type": "BLANK", "message": "NOTHING"}

	try:

		previousAnnouncements = SiteAnnouncement.objects.filter(creator = request.user)

	except SiteAnnouncement.DoesNotExist:

		previousAnnouncements = []

	else:

		pass 



	return render(
		request,
		"cdclSite/announcementsPage.html",
		{
			"announcementForm": announcementForm,
			"previousAnnouncements": previousAnnouncements,
			"pageMessage": json.dumps(pageMessage)
		}
	) 



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
	
	errorPlayers = []
	
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

					newPlayerFile = PlayerFile.objects.create(playerFile = request.FILES['playerFile'])

					with open(newPlayerFile.playerFile.path) as csvFile:
						reader = csv.reader(csvFile)
						playersData = [row for row in reader]
				
				except Exception as e:

					pageMessage = {
						"type": "ERROR",
						"message": "The player file could not be uploaded correctly: " + str(e)
					}
				
				else:

					for row in playersData[1:]:

						try:

							existing = Player.objects.get(ecfCode = row[0])

						except Player.DoesNotExist:

							try:

								newPlayer = Player.objects.create(
									forenames = row[1],
									surname = row[2],
									ecfCode = row[0],
									grading = row[3],
									club = Club.objects.get(name = row[4])
								)

							except Exception as e:
								row.append(str(e))
								errorPlayers.append(row)
							
							else:
								pass

						else:

							pass


				if len(errorPlayers)  > 0:

					pageMessage = {
						"type": "ERROR",
						"message": "Players could not be added: "
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

	for player in reversed(list(Player.objects.all().order_by("-club__name"))):

		playerData[player.id] = {
			"forenames": player.forenames,
			"surname": player.surname,
			"ecfCode": player.ecfCode,
			"grading": player.grading,
			"club": player.club.name
		}


	return render(
		request,
		"cdclSite/playerManagement.html",
		{
			"pageMessage": json.dumps(pageMessage),
			"players": json.dumps(playerData),
			"playerManagementForm": playerManagementForm,
			"errorPlayers": errorPlayers
		}
	)



# displays tools for managing fixtures
@login_required(login_url='index')
def fixtures(request):

	if request.method == "POST":
		
		fixtureManagementForm = FixtureManagementForm(request.POST, request.FILES)

		if fixtureManagementForm.is_valid():

			form_bulkMode = fixtureManagementForm.cleaned_data["bulkMode"]
			form_editMode = fixtureManagementForm.cleaned_data["editMode"]
			form_addMode = fixtureManagementForm.cleaned_data["addMode"]
			
			form_removeFixtureMode = fixtureManagementForm.cleaned_data["removeFixtureMode"]
			form_removeTeamMode = fixtureManagementForm.cleaned_data["removeTeamMode"]
			form_addTeamMode = fixtureManagementForm.cleaned_data["addTeamMode"]
			form_newTeamName = fixtureManagementForm.cleaned_data["newTeamName"]
			form_newTeamClubID = fixtureManagementForm.cleaned_data["newTeamClubID"]
			form_newTeamCaptainID = fixtureManagementForm.cleaned_data["newTeamCaptainID"]
			form_statusMode = fixtureManagementForm.cleaned_data["statusMode"]
			form_fixtureFile = fixtureManagementForm.cleaned_data["fixtureFile"]
			form_teamMode = fixtureManagementForm.cleaned_data["teamMode"]
			form_teamData = fixtureManagementForm.cleaned_data["teamData"]
			form_newFixtureDivision = fixtureManagementForm.cleaned_data["newFixtureDivision"]
			form_newFixtureSeason = fixtureManagementForm.cleaned_data["newFixtureSeason"]
			form_newFixtureEvent = fixtureManagementForm.cleaned_data["newFixtureEvent"]
			form_newFixtureDate = fixtureManagementForm.cleaned_data["newFixtureDate"]
			form_newFixtureHomeTeam = fixtureManagementForm.cleaned_data["newFixtureHomeTeam"]
			form_newFixtureAwayTeam = fixtureManagementForm.cleaned_data["newFixtureAwayTeam"]

			form_selectedFixtureID = fixtureManagementForm.cleaned_data["selectedFixtureID"]
			form_editFixtureSeason = fixtureManagementForm.cleaned_data["editFixtureSeason"]
			form_editFixtureEvent = fixtureManagementForm.cleaned_data["editFixtureEvent"]
			form_editFixtureDate = fixtureManagementForm.cleaned_data["editFixtureDate"]
			form_editFixtureHomeTeam = fixtureManagementForm.cleaned_data["editFixtureHomeTeam"]
			form_editFixtureAwayTeam = fixtureManagementForm.cleaned_data["editFixtureAwayTeam"]

			form_newStatus = fixtureManagementForm.cleaned_data["newStatus"]

			form_selectedTeamID = fixtureManagementForm.cleaned_data["selectedTeamID"]

			if form_addTeamMode:

				try:

					newTeam = Team.objects.create(
						name = form_newTeamName,
						captain = Player.objects.get(id = form_newTeamCaptainID),
						club = Club.objects.get(id = form_newTeamClubID)
					)
				
				except Exception as e:

					pageMessage = {
						"type": "ERROR",
						"message": "The team could not be created: " + str(e)
					}
				
				else:

					pageMessage = {
						"type": "SUCCESS",
						"message": "Team created successfully."
					}


			if form_removeTeamMode:
				
				try:
					selectedTeam = Team.objects.get(id = form_selectedTeamID)

				except Team.objects.DoesNotExist:

					pageMessage = {
						"type": "ERROR",
						"message": "The selected fixure could not be found."
					}
				
				else:

					try:

						selectedTeam.delete()

					except Exception as e:

						pageMessage = {
							"type": "ERROR",
							"message": "The selected team could not be deleted: " + str(e)
						}
					
					else:

						pageMessage = {
							"type": "SUCCESS",
							"message": "The selected team was deleted successfully."
						}


			if form_removeFixtureMode:

				try:
					selectedFixture = Fixture.objects.get(id = form_selectedFixtureID)

				except Fixture.objects.DoesNotExist:

					pageMessage = {
						"type": "ERROR",
						"message": "The selected fixure could not be found."
					}
				
				else:

					try:

						selectedFixture.delete()

					except Exception as e:

						pageMessage = {
							"type": "ERROR",
							"message": "The selected fixture could not be deleted: " + str(e)
						}
					
					else:

						pageMessage = {
							"type": "SUCCESS",
							"message": "The selected fixture status was deleted successfully."
						}


			if form_statusMode:

				try:
					selectedFixture = Fixture.objects.get(id = form_selectedFixtureID)

				except Fixture.objects.DoesNotExist:

					pageMessage = {
						"type": "ERROR",
						"message": "The selected fixure could not be found."
					}
				
				else:

					try:

						selectedFixture.status = form_newStatus
						selectedFixture.save()

					except Exception as e:

						pageMessage = {
							"type": "ERROR",
							"message": "The selected fixture's status could not be changed: " + str(e)
						}
					
					else:

						pageMessage = {
							"type": "SUCCESS",
							"message": "The selected fixture's status was changed successfully."
						}


			if form_teamMode:

				teamData = json.loads(form_teamData)

				try:

					for t in teamData:

						if teamData[t]["clubID"] and teamData[t]["captainID"]:

							team = Team.objects.get(id = t)

							team.club = Club.objects.get(id = teamData[t]["clubID"])

							captainPlayer = Player.objects.get(id = teamData[t]["captainID"])

							captainPlayer.isCaptain = True

							captainPlayer.save()

							team.captain = captainPlayer

							team.save()

				except Exception as e:

					pageMessage = {
						"type": "ERROR",
						"message": "Some or all of the teams could not be edited: " + str(e)
					}

				else:

					pageMessage = {
						"type": "SUCCESS",
						"message": "The team(s) were edited successfully."
					}

			# if editMode is true, get the selected player
			if form_editMode:

				try:

					selectedFixture = Fixture.objects.get(id = form_selectedFixtureID)

				except Fixture.DoesNotExist:

					pageMessage = {
						"type": "ERROR",
						"message": "The selected fixture could not be found in the database."
					}
				
				else:

					try:
						selectedFixture.date = datetime.datetime.strptime(form_editFixtureDate, "%d-%m-%y")
						selectedFixture.homeTeam = Team.objects.get(id = form_editFixtureHomeTeam)
						selectedFixture.awayTeam = Team.objects.get(id = form_editFixtureAwayTeam)
						selectedFixture.event = Event.objects.get(id = form_editFixtureEvent)
						selectedFixture.season = Season.objects.get(id = form_editFixtureSeason)

						selectedFixture.save()
					
					except Exception as e:

						pageMessage = {
							"type": "ERROR",
							"message": "The changes to the fixture could not be made: " + str(e)
						}

					else:

						pageMessage = {
							"type": "SUCCESS",
							"message": "The fixture was changed successfully."
						}



			# if addMode is true, use the player details from the from to create a new player
			if form_addMode:
				
				try:

					# find or create the required teams
					try:
						homeTeam = Team.objects.get(name = form_newFixtureHomeTeam.title())
					except Team.DoesNotExist:
						homeTeam = Team.objects.create(name = form_newFixtureHomeTeam.title())
					else:
						homeTeam = Team.objects.get(name = form_newFixtureHomeTeam.title())

					try:
						awayTeam = Team.objects.get(name = form_newFixtureAwayTeam.title())
					except Team.DoesNotExist:
						awayTeam = Team.objects.create(name = form_newFixtureAwayTeam.title())
					else:
						awayTeam = Team.objects.get(name = form_newFixtureAwayTeam.title())

					# find or create the event
					try:
						locatedEvent = Event.objects.get(name = form_newFixtureEvent.title())
					except Event.DoesNotExist:
						locatedEvent = Event.objects.create(name = form_newFixtureEvent.title())
					else:
						pass
					
					# find or create the season
					try:
						locatedSeason = Season.objects.get(name = form_newFixtureSeason)
					except Season.DoesNotExist:
						locatedSeason = Season.objects.create(name = form_newFixtureSeason)
					else:
						pass
					
					# create the new fixture
					newFixture = Fixture.objects.create(
							date = datetime.datetime.strptime(form_newFixtureDate, "%d-%m-%y"),
							homeTeam = homeTeam,
							awayTeam = awayTeam,
							season = locatedSeason,
							event = locatedEvent,
							status = "PENDING"
						)
					
				except Exception as e:

					pageMessage = {
						"type": "ERROR",
						"message": "The new fixture could not be added: " + str(e)
					}
				
				else:

					pageMessage = {
						"type": "SUCCESS",
						"message": "The new fixture was added successfully."
					}


			# if bulkMode is true, a file has been submitted
			if form_bulkMode:

				try:

					newFixtureFile = FixtureFile.objects.create(fixtureFile = request.FILES['fixtureFile'])

					# test text replacement
					with open(newFixtureFile.fixtureFile.path) as csvFile:
						reader = csv.reader(csvFile)
						fixturesData = [row for row in reader]
					
					for row in fixturesData[1:]:

						# find or create the required teams
						try:
							homeTeam = Team.objects.get(name = str(row[3].title()))
						except Team.DoesNotExist:
							homeTeam = Team.objects.create(name = str(row[3]).title())
						else:
							homeTeam = Team.objects.get(name = str(row[3].title()))

						try:
							awayTeam = Team.objects.get(name = str(row[4].title()))
						except Team.DoesNotExist:
							awayTeam = Team.objects.create(name = str(row[4]).title())
						else:
							awayTeam = Team.objects.get(name = str(row[4].title()))

						# find or create the event
						try:
							locatedEvent = Event.objects.get(name = str(row[0].title()))
						except Event.DoesNotExist:
							locatedEvent = Event.objects.create(name = str(row[0].title()))
						else:
							pass
						
						# find or create the season
						try:
							locatedSeason = Season.objects.get(name = str(row[1]))
						except Season.DoesNotExist:
							locatedSeason = Season.objects.create(name = str(row[1]))
						else:
							pass
						
						# create the new fixture
						newFixture = Fixture.objects.create(
							date = datetime.datetime.strptime(row[2], "%d-%m-%y"),
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

	fixturesData = {}
	for f in Fixture.objects.all():

		fixturesData[f.id] = {
			"date": str(f.date),
			"homeTeamID": f.homeTeam.id,
			"awayTeamID": f.awayTeam.id,
			"homeTeamName": f.homeTeam.name,
			"awayTeamName": f.awayTeam.name,
			"eventName": f.event.name,
			"seasonName": f.season.name,
			"eventID": f.event.id,
			"seasonID": f.season.id
		}


		if f.homeSubmission:
			
			submission = f.homeSubmission

			fixturesData[f.id]["homeSubmission"] = {
				"teamName": submission.team.name,
				"games": []
			}

			for g in submission.game_set.all():

				fixturesData[f.id]["homeSubmission"]["games"].append(
					{
						"boardNumber": g.boardNumber,
						"homePlayerID": g.homePlayerID,
						"homePlayerName": Player.objects.get(id = g.homePlayerID).forenames,
						"homePlayerGrade": Player.objects.get(id = g.homePlayerID).grading,
						"homePlayerScore": g.homePlayerScore,
						"awayPlayerID": g.awayPlayerID,
						"awayPlayerName": Player.objects.get(id = g.awayPlayerID).forenames,
						"awayPlayerGrade": Player.objects.get(id = g.awayPlayerID).grading,
						"awayPlayerScore": g.awayPlayerScore
					}
				)

		if f.awaySubmission:

			submission = f.awaySubmission
		
			fixturesData[f.id]["awaySubmission"] = {
				"teamName": submission.team.name,
				"games": []
			}

			for g in submission.game_set.all():

				fixturesData[f.id]["awaySubmission"]["games"].append(
					{
						"boardNumber": g.boardNumber,
						"homePlayerID": g.homePlayerID,
						"homePlayerName": Player.objects.get(id = g.homePlayerID).forenames,
						"homePlayerGrade": Player.objects.get(id = g.homePlayerID).grading,
						"awayPlayerID": g.awayPlayerID,
						"homePlayerName": Player.objects.get(id = g.awayPlayerID).forenames,
						"awayPlayerGrade": Player.objects.get(id = g.awayPlayerID).grading,
						"homePlayerScore": g.homePlayerScore,
						"awayPlayerScore": g.awayPlayerScore
					}
				)



	return render(request, "cdclSite/fixtures.html",
		{
			"fixtureManagementForm": fixtureManagementForm,
			"pageMessage": json.dumps(pageMessage),
			"events": Event.objects.all(),
			"seasons": Season.objects.all(),
			"fixtures": reversed(list(Fixture.objects.all().order_by("-date"))),
			"clubs": Club.objects.all(),
			"teams": Team.objects.all(),
			"players": json.dumps(players),
			"fixturesData": json.dumps(fixturesData)
		})



# displays forms for captains to upload match results
@login_required(login_url='index')
def resultsSubmission(request):

	if request.method == "POST":

		resultsSubmissionForm = ResultsSubmissionForm(request.POST)

		if resultsSubmissionForm.is_valid():

			
			form_selectedFixtureID = resultsSubmissionForm.cleaned_data["selectedFixtureID"] 

			form_board1_homePlayerID = resultsSubmissionForm.cleaned_data["board1_homePlayerID"] 
			form_board2_homePlayerID = resultsSubmissionForm.cleaned_data["board2_homePlayerID"] 
			form_board3_homePlayerID = resultsSubmissionForm.cleaned_data["board3_homePlayerID"] 
			form_board4_homePlayerID = resultsSubmissionForm.cleaned_data["board4_homePlayerID"] 
			form_board5_homePlayerID = resultsSubmissionForm.cleaned_data["board5_homePlayerID"] 
			form_board6_homePlayerID = resultsSubmissionForm.cleaned_data["board6_homePlayerID"] 

			form_board1_awayPlayerID = resultsSubmissionForm.cleaned_data["board1_awayPlayerID"] 
			form_board2_awayPlayerID = resultsSubmissionForm.cleaned_data["board2_awayPlayerID"] 
			form_board3_awayPlayerID = resultsSubmissionForm.cleaned_data["board3_awayPlayerID"] 
			form_board4_awayPlayerID = resultsSubmissionForm.cleaned_data["board4_awayPlayerID"] 
			form_board5_awayPlayerID = resultsSubmissionForm.cleaned_data["board5_awayPlayerID"] 
			form_board6_awayPlayerID = resultsSubmissionForm.cleaned_data["board6_awayPlayerID"] 

			form_board1_homePlayerScore = resultsSubmissionForm.cleaned_data["board1_homePlayerScore"] 
			form_board2_homePlayerScore = resultsSubmissionForm.cleaned_data["board2_homePlayerScore"] 
			form_board3_homePlayerScore = resultsSubmissionForm.cleaned_data["board3_homePlayerScore"] 
			form_board4_homePlayerScore = resultsSubmissionForm.cleaned_data["board4_homePlayerScore"] 
			form_board5_homePlayerScore = resultsSubmissionForm.cleaned_data["board5_homePlayerScore"] 
			form_board6_homePlayerScore = resultsSubmissionForm.cleaned_data["board6_homePlayerScore"] 

			form_board1_awayPlayerScore = resultsSubmissionForm.cleaned_data["board1_awayPlayerScore"]
			form_board2_awayPlayerScore = resultsSubmissionForm.cleaned_data["board2_awayPlayerScore"] 
			form_board3_awayPlayerScore = resultsSubmissionForm.cleaned_data["board3_awayPlayerScore"] 
			form_board4_awayPlayerScore = resultsSubmissionForm.cleaned_data["board4_awayPlayerScore"] 
			form_board5_awayPlayerScore = resultsSubmissionForm.cleaned_data["board5_awayPlayerScore"] 
			form_board6_awayPlayerScore = resultsSubmissionForm.cleaned_data["board6_awayPlayerScore"]

			form_homeTeam = resultsSubmissionForm.cleaned_data["homeTeam"]
			form_awayTeam = resultsSubmissionForm.cleaned_data["awayTeam"]

			boards = [
				{
					"homePlayerid": form_board1_homePlayerID,
					"awayPlayerid": form_board1_awayPlayerID,
					"homePlayerscore": form_board1_homePlayerScore,
					"awayPlayerscore": form_board1_awayPlayerScore

				},
				{
					"homePlayerid": form_board2_homePlayerID,
					"awayPlayerid": form_board2_awayPlayerID,
					"homePlayerscore": form_board2_homePlayerScore,
					"awayPlayerscore": form_board2_awayPlayerScore

				},
				{
					"homePlayerid": form_board3_homePlayerID,
					"awayPlayerid": form_board3_awayPlayerID,
					"homePlayerscore": form_board3_homePlayerScore,
					"awayPlayerscore": form_board3_awayPlayerScore

				},
				{
					"homePlayerid": form_board4_homePlayerID,
					"awayPlayerid": form_board4_awayPlayerID,
					"homePlayerscore": form_board4_homePlayerScore,
					"awayPlayerscore": form_board4_awayPlayerScore

				},
				{
					"homePlayerid": form_board5_homePlayerID,
					"awayPlayerid": form_board5_awayPlayerID,
					"homePlayerscore": form_board5_homePlayerScore,
					"awayPlayerscore": form_board5_awayPlayerScore

				},
				{
					"homePlayerid": form_board6_homePlayerID,
					"awayPlayerid": form_board6_awayPlayerID,
					"homePlayerscore": form_board6_homePlayerScore,
					"awayPlayerscore": form_board6_awayPlayerScore

				}
			]

			badScores = False

			if not badScores:

				try:

					userPlayer = request.user.player

					captainedTeams = Team.objects.filter(captain = userPlayer)
					
					homeOrAway = "H"
					
					for team in captainedTeams:
						if team.name == form_homeTeam:
							usersTeam = team
							homeOrAway = "H"
							break

						if team.name == form_awayTeam:
							usersTeam = team
							homeOrAway = "A"
							break

					newSubmission = Submission.objects.create(team = usersTeam)

					i = 0
					while i < 6:

						if boards[i]["awayPlayerid"] and boards[i]["homePlayerid"]:

							newGame = Game.objects.create(
								boardNumber = i,
								homePlayerID = boards[i]["homePlayerid"],
								awayPlayerID = boards[i]["awayPlayerid"],
								homePlayerScore = boards[i]["homePlayerscore"],
								awayPlayerScore = boards[i]["homePlayerscore"],
								submission = newSubmission
							)
						
						else:

							pass

						i += 1

					fixture = Fixture.objects.get(id = form_selectedFixtureID)

					if homeOrAway == "H":
						fixture.homeSubmission = newSubmission
					else:
						fixture.awaySubmission = newSubmission

					fixture.save()
				
				except Exception as e:

					pageMessage = {
						"type": "ERROR",
						"message": "The results could not be submitted: " + str(e)
					}

				else:

					pageMessage = {
						"type": "SUCCESS",
						"message": "The results were submitted successfully"
					}

		else:

			pageMessage = {
				"type": "ERROR",
				"message": "One or more fields were not completed correctly."
			}

	else:

		resultsSubmissionForm = ResultsSubmissionForm()

		pageMessage = {"type": "BLANK", "message": "NOTHING"}

	fixtureData = {}
	
	if request.user.is_superuser:
	
		for fixture in Fixture.objects.all():
			
			fixtureData[fixture.id] = {
				"date": str(fixture.date),
				"homeTeam": {"name": fixture.homeTeam.name, "club": fixture.homeTeam.club.name},
				"awayTeam": {"name": fixture.awayTeam.name, "club": fixture.awayTeam.club.name},
				"event": fixture.event.name
			}
	else:

		try:
		
			request.user.player
		
		except Player.DoesNotExist:
		
			pass
		
		else:
		
			for fixture in Fixture.objects.all():
				
				if fixture.homeTeam.captain == request.user.player or fixture.awayTeam.captain == request.user.player:
			
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
			"resultsForm": resultsSubmissionForm,
			"pageMessage": json.dumps(pageMessage),
			"fixtureData": json.dumps(fixtureData),
			"playerData": json.dumps(playerData)
		})



# displays tools to keep user data up to date
@login_required(login_url='index')
def userDetails(request):
	
	pageMessage = {"type": "BLANK", "message": "NOTHING"}

	return render(request, "cdclSite/userDetails.html", {"pageMessage": json.dumps(pageMessage)})


# displays tools to manage users and their access
@login_required(login_url='index')
def userManagementToolSettings(request):

	if request.method == "POST":

		userManagementToolsForm = UserManagementToolsForm(request.POST)

		if userManagementToolsForm.is_valid():

				form_selectedUserId = userManagementToolsForm.cleaned_data["selectedUserId"]
				form_activeMode = userManagementToolsForm.cleaned_data["activeMode"]
				form_superuserMode = userManagementToolsForm.cleaned_data["superuserMode"]
				form_officerMode = userManagementToolsForm.cleaned_data["officerMode"]
				form_recordsMode = userManagementToolsForm.cleaned_data["recordsMode"]
				form_treasurerMode = userManagementToolsForm.cleaned_data["treasurerMode"]

				try:

					selectedUser = User.objects.get(id = form_selectedUserId)

				except User.DoesNotExist:

					pageMessage = {
						"type": "ERROR",
						"message": "User could not be found: id = " + str(form_selectedUserId)
					}
				
				else:

					if form_treasurerMode:

						try:

							if selectedUser.userdata.isTreasurer:
							
								selectedUser.userdata.isTreasurer = False
							
							else:
								
								selectedUser.userdata.isTreasurer = True
							
							selectedUser.userdata.save()

						except Exception as e:

							pageMessage = {
								"type": "ERROR",
								"message": "Could not change treasurer status of user: " + str(e)
							}

						else:

							pageMessage = {
								"type": "SUCCESS",
								"message": "Treasurer status changed successfully."
							}

					if form_recordsMode:

						try:

							if selectedUser.userdata.isRecordSecretary:
							
								selectedUser.userdata.isRecordSecretary = False
							
							else:
								
								selectedUser.userdata.isRecordSecretary = True
								
							selectedUser.userdata.save()

						except Exception as e:

							pageMessage = {
								"type": "ERROR",
								"message": "Could not change record secretary status of user: " + str(e)
							}

						else:

							pageMessage = {
								"type": "SUCCESS",
								"message": "Record secretary status changed successfully."
							}



					if form_officerMode:

						try:

							if selectedUser.userdata.isOfficer:
							
								selectedUser.userdata.isOfficer = False
							
							else:
								
								selectedUser.userdata.isOfficer = True

							selectedUser.userdata.save()

						except Exception as e:

							pageMessage = {
								"type": "ERROR",
								"message": "Could not change officer status of user: " + str(e)
							}

						else:

							pageMessage = {
								"type": "SUCCESS",
								"message": "Officer status changed successfully."
							}


					if form_superuserMode:

						try:

							if selectedUser.is_superuser:

								selectedUser.is_superuser = False
							
							else:

								selectedUser.is_superuser = True

							selectedUser.userdata.save()

						except Exception as e:

							pageMessage = {
								"type": "ERROR",
								"message": "Could not change the user's superuser status: " + str(e)
							}

						else:

							pageMessage = {
								"type": "SUCCESS",
								"message": "Superuser status changed successfully."
							}



					if form_activeMode:

						try:
								
							if selectedUser.is_active:

								selectedUser.is_active = False
							
							else:

								selectedUser.is_active = True

							selectedUser.save()

						except Exception as e:

							pageMessage = {
								"type": "ERROR",
								"message": "Could not change the user's enabled status: " + str(e)
							}

						else:

							pageMessage = {
								"type": "SUCCESS",
								"message": "Account activity changed successfully."
							}

		
		else:

			pageMessage = {
				"type": "ERROR",
				"message": "Some or all of the form fields were not correctly completed."
			}

	else:

		userManagementToolsForm = UserManagementToolsForm()

		pageMessage = {"type": "BLANK", "message": "NOTHING"}

	userDataDict = {}

	for user in User.objects.all():

		userDataDict[user.id] = {
			"username": user.username,
			"active": user.is_active,
			"superuser": user.is_superuser
		}

		try:

			currentUserData = user.userdata
		
		except UserData.DoesNotExist:

			userDataDict[user.id]["userData"] = None
		
		else:

			userDataDict[user.id]["userData"] = {
				"isOfficer": currentUserData.isOfficer,
				"isRecordSecretary": currentUserData.isRecordSecretary,
				"isTreasurer": currentUserData.isTreasurer,
				"forenames": currentUserData.forenames,
				"surname": currentUserData.surname,
				"primaryContactNumber":currentUserData.primaryContactNumber,
				"backupContactNumber": currentUserData.backupContactNumber,
				"email": currentUserData.email
			}



		try:

			currentPlayerData = user.player
		
		except Player.DoesNotExist:

			userDataDict[user.id]["playerData"] = None
		
		else:

			userDataDict[user.id]["playerData"] = {
				"forenames": user.player.forenames,
				"surname": user.player.surname,
				"ecfCode": user.player.ecfCode,
				"grading": user.player.grading,
				"club": user.player.club.name
			}

	pprint.pprint(userDataDict)

	return render(
		request,
		"cdclSite/userManagementToolSettings.html",
		{
			"pageMessage": json.dumps(pageMessage),
			"userData": json.dumps(userDataDict),
			"userManagementToolsForm": userManagementToolsForm,
			"users": User.objects.all()
			
		}
	)