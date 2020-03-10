from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, \
    SubmitField, PasswordField, FloatField, FileField
from wtforms.validators import DataRequired, Length, Email, Regexp, Optional
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    body = PageDownField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[DataRequired()])
    submit = SubmitField('Submit')


class OpPlanningForm(FlaskForm):
    # def init_formdata(self, form):
    #     coronal_component_C = 5.6
    #     form.process_formdata([coronal_component_C])
    #     return True
    coronal_component_C = FloatField('Enter coronal component C', validators=[DataRequired()])
    sagittal_component_S = FloatField('Enter sagittal component S', validators=[DataRequired()])
    torsion_component_T = FloatField('Enter torsion component T', validators=[DataRequired()])
    # filename = FileField('Store the results in:', validators=[Optional()])
    # coronal_component_C.data = 5.6
    # coronal_component_C = FloatField('Enter coronal component C', value=5.5, validators=[DataRequired()])
    # sagittal_component_S = FloatField('Enter sagittal component S', value=-7.2, validators=[DataRequired()])
    # torsion_component_T = FloatField('Enter torsion component T', value=23.8, validators=[DataRequired()])
    submit = SubmitField('Submit')
