from wtforms import ValidationError
from models import User


class UniqueValidator(object):
        '''
        Validator that checks field UniqueValidatorness
        '''
        def __init__(self, db_session, model, field, message=None):
                self.db_session = db_session
                self.model = model
                self.field = field
                if not message:
                        message = "This element already exists"
                self.message = message

        def __call__(self, form, field):
                check = self.db_session.query(self.model).\
                    filter(self.field == field.data).first()
                if check:
                        raise ValidationError(self.message)


class ExistsValidator(object):
        '''
        Validator that checks field existence
        '''

        def __init__(self, db_session, model, field, message=None):
                self.db_session = db_session
                self.model = model
                self.field = field
                if not message:
                        message = "This element not exists"
                self.message = message

        def __call__(self, form, field):

                check = self.db_session.query(self.model).\
                    filter(self.field == field.data).first()
                if not check:
                        raise ValidationError(self.message)


class PasswordValidator(object):
        """
        Validator that checks the password login
        """
        def __init__(self, db_session, message=None):
                self.db_session = db_session
                if not message:
                        message = "Wrong password"
                self.message = message

        def __call__(self, form, password):

                real_password = self.db_session.query(User).\
                    filter(User.name == form.username.data).first()
                if real_password:
                        real_password = real_password.password
                if  real_password != password.data:
                        raise ValidationError(self.message)
