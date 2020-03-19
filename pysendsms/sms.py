# sms.py

import smtplib

class SMS():
    """ A class for accesses Gmail SMTP servers.

    Attributes:
    -------------------
        server : smtplib.SMTP() Object
            SMTP object used to facilitate messaging.
        email : str
            Gmail address used for authenticating to Gmail SMTP servers.
        password: str
            Gmail app specific password used for authenticating to Gmail SMTP servers.
        tls : bool
            Wether or not the SMS class should use TLS/SSL for connecting to smtp server
        from_email : str
            Address used to be the from address when your smtp server gives you a username/password credential
        port : int
            Port number that your smtp server requires to connect to
    """

    def __init__(self, username=None, password=None, from_email= None, server='smtp.gmail.com', port=587, tls=True):
        """ The initilizer for SMS class. """

        self.server = smtplib.SMTP(host=server, port=port)
        self.username = username
        self.password = password
        self.tls = tls
        self.from_email = self.username if from_email is None else from_email

        self.connect()

    def connection_alive(self):
        """ A function to validate that number is a string of digits of 10-12 in length.

        Returns:
        -------------------
            bool : bool
                If current instance server responds with a connection, this return true, else false.
        """

        status = None

        try:
            status = self.server.noop()[0]

        except smtplib.SMTPServerDisconnected as e:
            status = e.errno

        finally:
            return True if status == 250 else False

    def connect(self):
        """ A function to initiate conenction and authentication to Gmail servers."""

        if self.tls:
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()

        self.server.login(self.username, self.password)


    def send(self, contacts, message):
        """ A function to send a message to any number of give contact objects.

        Parameters:
        -------------------
            contatcs : Contact() or list(Contact())
                A Contact object or a list of Contact objects to have messages sent to.
            message : str
                The message you want to have sent to given contacts.
        """

        if not self.connection_alive():
            self.connect()

        if type(contacts) != type(list()):
            contacts = [contacts]

        try:
            [self.server.sendmail(from_addr=self.from_email, to_addrs=c.address, msg=message) for c in contacts]
        except Exception as e:
            print(e.__class__.__name__, e)
