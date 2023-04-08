from mongoengine import connect, Document, StringField, BooleanField

connect(host='mongodb+srv://userweb10:567234@pyweb.e9uvnnc.mongodb.net/?retryWrites=true&w=majority')


class Client(Document):
    fullname = StringField(required=True)
    email = StringField()
    phone = StringField()
    address = StringField()
    sent_message = BooleanField()
    best_method = StringField()
