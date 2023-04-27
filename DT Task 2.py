#creating a nudge object

import datetime

class Nudge:
    def __init__(self, event_id, title, cover_image_url, send_time, description, icon, invitation):
        self.id = None  # Set by the database upon creation
        self.event_id = event_id
        self.title = title
        self.cover_image_url = cover_image_url
        self.send_time = send_time
        self.description = description
        self.icon = icon
        self.invitation = invitation

    def to_dict(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'title': self.title,
            'cover_image_url': self.cover_image_url,
            'send_time': self.send_time.isoformat(),
            'description': self.description,
            'icon': self.icon,
            'invitation': self.invitation
        }

    @classmethod
    def from_dict(cls, nudge_dict):
        nudge = cls(
            event_id=nudge_dict['event_id'],
            title=nudge_dict['title'],
            cover_image_url=nudge_dict['cover_image_url'],
            send_time=datetime.datetime.fromisoformat(nudge_dict['send_time']),
            description=nudge_dict['description'],
            icon=nudge_dict['icon'],
            invitation=nudge_dict['invitation']
        )
        nudge.id = nudge_dict['id']
        return nudge

# To create a new Nudge object, you can simply instantiate the class with the required parameters:

new_nudge = Nudge(event_id='123', title='My Nudge', cover_image_url='https://example.com/image.jpg',
                   send_time=datetime.datetime.now(), description='This is my nudge', icon='heart',
                   invitation='Join me for this event')


# To convert a Nudge object to a dictionary, you can call the to_dict method:

nudge_dict = new_nudge.to_dict()

# create a Nudge object from a dictionary, you can call the from_dict classmethod:

nudge_dict = {'id': 'abc123', 'event_id': '123', 'title': 'My Nudge', 'cover_image_url': 'https://example.com/image.jpg',
              'send_time': '2023-04-27T15:30:00', 'description': 'This is my nudge', 'icon': 'heart',
              'invitation': 'Join me for this event'}
nudge_obj = Nudge.from_dict(nudge_dict)

