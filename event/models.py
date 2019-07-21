from django.db import models
import json




class Event(models.Model):
    eventname = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    startdate = models.CharField(max_length=50) #Test
    enddate = models.CharField(max_length=50) #Test
    starttime = models.CharField(max_length=50) #Test
    endtime = models.CharField(max_length=50) #Test
    description = models.CharField(max_length=150)
    speakers = models.CharField(max_length=200)
    
    def save_speakers(self, x):
        self.speakers = json.dumps(x)

    def get_speakers(self):
        return json.loads(self.speakers)


	# locationInMap =
	# attendeesCount =
    # coverPhoto =
    # response =
	# hasApprovalForPosts =
	# maximumNumberOfAttendees,
	# ticketPrice =
    # eventAdmins =
	# speakerList =

 #    class Meta:
	# 	permissions = (
	# 		('add_ev', 'Add event'),
	# 		('del_ev','Delete event'),
	# 		('edit_ev','Edit event'),
	# 	)
	# def __str__(self):
	# 	return self.eventname


# event title , starting date, end date, location, location_in_map, event description, attendees count, response ( going / declined / following ) , event short summary, event cover photo. hasApprovalForPosts(true/false), event admins, maximumNumberOfAttendees, Ticket Price, keynote speakers, speakerList with name,
