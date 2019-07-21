from __future__ import print_function

from django.shortcuts import render,HttpResponse
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# from .settings import MY_KEY


import csv
import datetime
import json
import os
from geopy.geocoders import Nominatim

import httplib2
from apiclient import discovery
from oauth2client.file import Storage
from oauth2client import client
from oauth2client import tools

from dateutil import parser

from .models import *


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def takeEventInfo(request):
    return render(request,'event_info.html')


def createEvent(request):

    eventname = request.POST['eventname'] # u_name is the name of the input tag
    location = request.POST['location']

    startdate = request.POST['startdate']
    enddate = request.POST['enddate']

    starttime = request.POST['starttime']
    endtime = request.POST['endtime']

    description =  request.POST['description']

    sp1 = ["sp1","sp1@gmail","afs"]
    sp2 = ["sp2","sp2@gmail","afswq"]

    sp = [sp1,sp2]
    event = Event.objects.create(eventname=eventname,location=location,startdate=startdate,enddate=enddate,starttime=starttime,endtime=endtime,description=description)
    event.save_speakers(sp)
    event.save()

    print(Event.objects.all())
    return HttpResponse(Event.objects.all())




def addEvent():
    event = {
      'summary': ' Birthday',
      'location': 'San Francisco, CA 94103',
      'description': 'A chance to enjoy birthday party.',
      'start': {
        'date': '2019-10-01',
        'time':'02:00'
        },
      'end': {
        'date': '2019-10-02',
        'time':'02:00'
        },
      'attendees': [
        {'email': 'lpage@example.com'},
        {'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
      'keynoteSpeakers':{
        'sp1':{
            'mail':'sp2@gmail.com',
            'code':'random'
        }
      }
    }
    #   'start': {
    #     'dateTime': '2019-10-01T09:00:00-07:',
    #     'timeZone': 'America/Los_Angeles',
    #     },
    #   'end': {
    #     'dateTime': '2019-10-28T17:00:00-07:00',
    #     'timeZone': 'America/Los_Angeles',
    #     },
    #   'recurrence': [
    #     'RRULE:FREQ=DAILY;COUNT=1'
    #   ],
    #   'attendees': [
    #     {'email': 'lpage@example.com'},
    #     {'email': 'sbrin@example.com'},
    #   ],
    #   'reminders': {
    #     'useDefault': False,
    #     'overrides': [
    #       {'method': 'email', 'minutes': 24 * 60},
    #       {'method': 'popup', 'minutes': 10},
    #     ],
    #   },
    #   'keynoteSpeakers':{
    #     'sp1':{
    #         'mail':'sp1@gmail.com',
    #         'code':'random'
    #     }
    #   }
    # }

    return event


def getCredentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def addEventToCalendar(request):
    creds = getCredentials()
    service = build('calendar', 'v3', credentials=creds)

    newEvent = addEvent()
    event = service.events().insert(calendarId='primary', body=newEvent).execute()
    print('Event created: ' , (event.get('htmlLink')))

    return HttpResponse("event created")


def displayEvents(request):
    creds = getCredentials()
    service = build('calendar', 'v3', credentials=creds)
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    eventResult = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = eventResult.get('items', [])
    print("#######")
    if not events:
        print('No upcoming events found.')


    for event in events:
        print(event['summary'])
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event['summary'])

    events = list({v['summary']:v for v in events}.values()) ##Get unique events only
    return render(request,'ShowCalendarList.html',{'events':events})


def displayWrittenDataInfo(nb_of_records, filename):
    print("[INFO]: {} google calendar events were written to file: {}"
          .format(nb_of_records, filename))

def saveObjectToJson(obj, filename):
    with open(filename, "w") as json_file:
        json.dump(obj, json_file)
    displayWrittenDataInfo(len(obj), filename)

def convertToDatetime(datetime_str):
    return parser.parse(datetime_str)

def saveGCEventsToCSV(gc_events, filename):
    def createCSVRow(event):
        startDatetime = convertToDatetime(
            event.get("start", "").get("dateTime", ""))
        endDatetime = convertToDatetime(
            event.get("end", "").get("dateTime", ""))
        createdDatetime = convertToDatetime(
            event.get("created", "").encode("utf-8"))

        return {"summary": event.get("summary", ""),
                "creator email": event.get("creator", "").get("email", ""),
                "created date": createdDatetime.date(),
                "created time": createdDatetime.time(),
                "start date": startDatetime.date(),
                "start time": startDatetime.time(),
                "end date": endDatetime.date(),
                "end time": endDatetime.time(),
                "nb of attendees": len(event.get("attendees", "")),
                "location": event.get("location", ""),
                "status": event.get("status", ""),
                "description": event.get("description", "").encode("utf-8")}

    headerNames = ["summary", "creator email", "created date", "created time",
                    "start date", "start time", "end date", "end time",
                    "nb of attendees", "location", "status", "description"]

    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, headerNames)
        writer.writeheader()
        for event in gc_events:
            try:
                writer.writerow(createCSVRow(event))
            except UnicodeEncodeError as exc:
                print("[ERROR]: " + str(exc))
    displayWrittenDataInfo(len(gc_events), filename)


def getGCEvents():
    events = []
    page_token = None

    creds = getCredentials()
    gc_service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    while True:
        calendarList= gc_service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime', pageToken=page_token).execute()
        for calendarListEntry in calendarList['items']:
            print(calendarListEntry['summary'])

        events.extend(calendarList["items"])
        page_token = calendarList.get('nextPageToken')
        if not page_token:
            break
    return events

def exportEvents(request):
    all_events = getGCEvents()

    exportFilename = "gc-meetings"
    saveObjectToJson(all_events, exportFilename + ".json")
    saveGCEventsToCSV(all_events, exportFilename + ".csv")
    return render(request,'ShowCalendarList.html',{'events':all_events})

def addressToGeocode():
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode("Mirpur-1,Dhaka")
    print(location.address)
    print((location.latitude, location.longitude))
    geocode = {
        'lat':location.latitude,
        'lng':location.longitude,
    }
    return geocode
#
# def showMap(request):
#     print(MY_KEY)
#     geocode = addressToGeocode()
#     print("geocode", geocode)
#     return render(request,"map.html",{'MY_KEY':MY_KEY, 'lat': geocode['lat'], 'lng':geocode['lng']})
