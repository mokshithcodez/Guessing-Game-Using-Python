import winotify
from winotify import Notification

greetings = Notification(app_id="Guessing Game",
                         title="Welcome To Guessing Game",
                         msg="Made By G.Mokshith On Github",
                         duration="short")

greetings.show()