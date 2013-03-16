from wtforms import ValidationError


class Unique(object):
    '''
    Validator that checks field uniqueness
    '''
    def __init__(self, db_session, model, field, message=None):
        self.db_session = db_session
        self.model = model
        self.field = field
        if not message:
                message = "This element already exists"
        self.message = message

    def __call__(self, form, field):
        check =self.db_session.query(self.model).\
            filter(self.field == field.data).first()
        if check:
                raise ValidationError(self.message)


class Exists(object):
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
