from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import InputRequired, AnyOf, URL, ValidationError

state_choices = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

states_list = [
    'AL',
    'AK',
    'AZ',
    'AR',
    'CA',
    'CO',
    'CT',
    'DE',
    'DC',
    'FL',
    'GA',
    'HI',
    'ID',
    'IL',
    'IN',
    'IA',
    'KS',
    'KY',
    'LA',
    'ME',
    'MT',
    'NE',
    'NV',
    'NH',
    'NJ',
    'NM',
    'NY',
    'NC',
    'ND',
    'OH',
    'OK',
    'OR',
    'MD',
    'MA',
    'MI',
    'MN',
    'MS',
    'MO',
    'PA',
    'RI',
    'SC',
    'SD',
    'TN',
    'TX',
    'UT',
    'VT',
    'VA',
    'WA',
    'WV',
    'WI',
    'WY'
]

genre_choices = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Swing', 'Swing'),
    ('Other', 'Other'),
]

genres_list = [
    'Alternative',
    'Blues',
    'Classical',
    'Country',
    'Electronic',
    'Folk',
    'Funk',
    'Hip-Hop',
    'Heavy Metal',
    'Instrumental',
    'Jazz',
    'Musical Theatre',
    'Pop',
    'Punk',
    'R&B',
    'Reggae',
    'Rock n Roll',
    'Soul',
    'Swing',
    'Other'
]


def validate_phone(self, phone):
    us_phone_num = '^([0-9]{3})[-][0-9]{3}[-][0-9]{4}$'
    match = re.search(us_phone_num, phone.value)
    if not match:
        raise ValidationError(
            'Error, phone number must be in format xxx-xxx-xxxx'
        )


class ShowForm(FlaskForm):
    artist_id = StringField(
        'artist_id',
        validators=[InputRequired()]
    )
    venue_id = StringField(
        'venue_id',
        validators=[InputRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[InputRequired()],
        default=datetime.today()
    )


class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[InputRequired()]
    )
    city = StringField(
        'city', validators=[InputRequired()]
    )
    state = SelectField(
        'state',
        validators=[
            InputRequired(),
            AnyOf(states_list)
        ],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[InputRequired()]
    )
    phone = StringField(
        'phone',
        validators=[
            InputRequired(),
            validate_phone
        ]
    )
    image_link = StringField(
        'image_link', validators=[InputRequired()]
    )
    genres = SelectMultipleField(
        'genres',
        validators=[
            InputRequired(),
            AnyOf(genres_list)
        ],
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website = StringField(
        'website', validators=[URL()]
    )
    seeking_talent = BooleanField(
        'seeking_talent'
    )
    seeking_description = StringField(
        'seeking_description'
    )


class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[InputRequired()]
    )
    city = StringField(
        'city', validators=[InputRequired()]
    )
    state = SelectField(
        'state',
        validators=[
            InputRequired(),
            AnyOf(states_list)
        ],
        choices=state_choices
    )
    phone = StringField(
        'phone',
        validators=[
            InputRequired(),
            validate_phone
        ]
    )
    image_link = StringField(
        'image_link', validators=[InputRequired()]
    )
    genres = SelectMultipleField(
        'genres',
        validators=[
            InputRequired(),
            AnyOf(genres_list)
        ],
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website = StringField(
        'website', validators=[URL()]
    )
    seeking_venue = BooleanField(
        'seeking_venue'
    )
    seeking_description = StringField(
        'seeking_description'
    )
