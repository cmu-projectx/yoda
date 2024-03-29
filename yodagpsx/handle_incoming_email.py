import logging, email, urllib
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class MessageHandlerException(Exception):
    """The general exception object thrown by MessageHandler"""
    def __init__(self, msg):
        self.msg = msg
		
class WebHook(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        body = list(mail_message.bodies(content_type='text/plain'))[0]
        logging.info("Body of message: " + body[1].decode())
        
        url = "http://thawing-retreat-8701.herokuapp.com/messages.json"
        form_fields = {
            "sender": mail_message.sender,
            "subject": mail_message.subject,
            "to": mail_message.to,
            "date": mail_message.date,
            "body": body[1].decode()
        }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(url=url,
                        payload=form_data,
                        method=urlfetch.POST,
                        headers={'Content-Type': 'application/x-www-form-urlencoded'})
        logging.info(result.status_code)
        logging.info(result.content)
		
application = webapp.WSGIApplication([('/_ah/mail/.+', WebHook)],
                                     debug=True)
			
def main():
    run_wsgi_app(application)
    
if __name__ == '__main__':
    main()
