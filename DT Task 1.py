#Get an event by its unique id:

import requests

event_id = 'your_event_id'
response = requests.get(f'https://event-management-api.com/events/{event_id}')
if response.status_code == 200:
    event = response.json()
    print(event)
else:
    print(f'Error fetching event with id {event_id}')


#Get an event by its recency & paginate results by page number and limit of events per page:

import requests

page_number = 2
events_per_page = 10
response = requests.get(f'https://event-management-api.com/events?page={page_number}&limit={events_per_page}&sort=date')
if response.status_code == 200:
    events = response.json()
    print(events)
else:
    print(f'Error fetching events for page {page_number}')

#Create an event and return the Id of the event i.e. created:

import requests

new_event = {
    'name': 'New Event',
    'description': 'A new event created using the API',
    'date': '2023-05-01'
}
response = requests.post('https://event-management-api.com/events', json=new_event)
if response.status_code == 201:
    created_event_id = response.json()['id']
    print(f'Event created with id {created_event_id}')
else:
    print('Error creating new event')


#Delete an event based on its Unique Id:
    
import requests

event_id = 'your_event_id'
response = requests.delete(f'https://event-management-api.com/events/{event_id}')
if response.status_code == 204:
    print(f'Event with id {event_id} deleted successfully')
else:
    print(f'Error deleting event with id {event_id}')
