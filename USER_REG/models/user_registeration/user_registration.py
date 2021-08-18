from USER_REG.extensions.extensions import db
from passlib.apps import custom_app_context as pwd_context


class User_registration(db.Document):
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    confirm_password = db.StringField()

    # def hash_password(self, password):
    #     self.password = pwd_context.encrypt(password)
    #
    # def verify_password(self, password):
    #     return pwd_context.verify(password, self.password)
