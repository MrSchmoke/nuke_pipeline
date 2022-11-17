from mongoengine import *

connect("vfx")

def validate_description(value):
    print("length "+ str(len(value)))
    if len(value) < 5:
        raise ValidationError("Description is too short!")
    elif len(value) > 35:
        raise ValidationError("Description is too long!")


class Users(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    description = StringField(required=True, min_length=5, max_length=35, validation=validate_description)
    artist_type = StringField(required= True, choices=["Compositor", "Lighter", "Modeler", "Rigger", "FX"])
    favorite_movies = ListField(StringField())
    active = BooleanField(default=True)
    email = EmailField(required=True, unique=True)

    @property
    def login(self):
        return (self.first_name[:3] + self.last_name[:3]).lower()


u = Users(first_name="Stu",
      last_name="Soong",
      description="Cool Dude",
      favorite_movies = ["Terminator", "Star Wars"],
      artist_type="Lighter",
      email="soong@mail.com").save()

print(u.login)

print("entry saved in db!")

#search = Users.objects()[0]
#search.active = False
#search.save()