import random
import time
from mongoengine import *

connect("vfx")

##FIRST TEST

# def validate_description(value):
#     print("length "+ str(len(value)))
#     if len(value) < 5:
#         raise ValidationError("Description is too short!")
#     elif len(value) > 35:
#         raise ValidationError("Description is too long!")

# class Users(Document):
#     first_name = StringField(required=True)
#     last_name = StringField(required=True)
#     description = StringField(required=True, min_length=5, max_length=35, validation=validate_description)
#     artist_type = StringField(required= True, choices=["Compositor", "Lighter", "Modeler", "Rigger", "FX"])
#     favorite_movies = ListField(StringField())
#     active = BooleanField(default=True)
#     email = EmailField(required=True, unique=True)

#     @property
#     def login(self):
#         return (self.first_name[:3] + self.last_name[:3]).lower()

# u = Users(first_name="Stu",
#       last_name="Soong",
#       description="Cool Dude",
#       favorite_movies = ["Terminator", "Star Wars"],
#       artist_type="Lighter",
#       email="soong@mail.com").save()

# print(u.login)

# print("entry saved in db!")

#search = Users.objects()[0]
#search.active = False
#search.save()




##SEARCH 
# class User(Document):
#     first_name = StringField(required=True)
#     last_name =  StringField(required=True)
#     gender =     StringField(choices=["Female", "Male", "Non-Binary"])
#     age =        IntField()
#     married =    BooleanField()

#     meta = {
#         "ordering": ["first_name", "last_name"],
#         "indexes":  ["first_name"] #caches the first name in the db for faster search output
#     }

#     def __str__(self):
#         return "<User Object>: %s %s, age: %s" %(self.first_name, self.last_name, self.age)

# user_search = User.objects().average("age")
# user_search = User.objects().order_by("-age")
# user_search = User.objects()[0:10]
# user_search = User.objects(age=22, first_name="Richard").get()

# user_search = User.objects(age__gte=20) #gte -> greater than equal
# user_search = User.objects(age__lte=20) #te -> lower than equal
# user_search = User.objects(first_name__contains="nn")
# user_search = User.objects(first_name__not__contains="nn") 
# user_search = User.objects(age__gt="20", age__lt="24", married = False) 

# for u in user_search:
#     print(u)
# print(user_search)




#LOAD DEMODATA IN DB
# def generate_users():
#     txt_file = open("users.txt", "r")

#     for line in txt_file:
#         strip_line = line.strip()
#         name_list = strip_line.split("\t")
#         #declare user object
#         users = User()
#         users.first_name = name_list[0]
#         users.last_name = name_list[1]
#         users.gender = name_list[2]
#         users.age = name_list[3]
#         name_list[4]
#         users.married = name_list[4] == 'Married'
#         users.save()

# generate_users()
# class Project(Document):
#     name = StringField()
#     client_name = StringField()

# project = Project(name = "My test project", client_name = "Lion").save()

# class Shot(Document):
#     name = StringField()
#     project = ReferenceField("Project")

# for i in range(10):
#     shot = Shot(name=str(i).zfill(4))
#     shot.project = project
#     shot.save()

# search = Shot.objects()

# project = Project.objects().first()
# project.name = "new name"
# project.save()
# for shot in Shot.objects():
#     print(shot.project.name)




##FILTER USERS AND PROJECTS IN DB
# class User(Document):
#     name = StringField()

# class Project(Document):
#     name = StringField()
#     active = BooleanField()

# class Shot(Document):
#     name = StringField()
#     assigned_user = ReferenceField("User")
#     project = ReferenceField("Project")

# user_list = ["Martin", "Fabian", "Oliver"]
# project_list = ["Project1", "Project2", "Project3", "Project4", "Project5"]

# for u in user_list:
#     User(name=u).save()

# for p in project_list:
#     project = Project(name=p)
#     project.active = bool(random.choice([0,1]))
#     project.save()

#     users = User.objects()
#     for i in range(50):
#         shot = Shot(name= str(i).zfill(3))
#         shot.project = project
#         shot.assigned_user = random.choice(users)
#         shot.save()

# user = User.objects(name="Fabian").get()
# project = Project.objects(active=True)

# shots = Shot.objects(assigned_user=user, project__in=project) #in -> look in projectlist

# for i in shots:
#     print(i.assigned_user.name, i.project.active, i.project.name)




##REFERENCING AND DELETING
# class User(Document):
#     name = StringField()

# class Project(Document):
#     name = StringField()
#     creator = ReferenceField("User")

# class Sequence(Document):
#     name = StringField()
#     project = ReferenceField("Project" reverse_delete_rule=CASCADE)

# class Shot(Document):
#     name = StringField()
#     sequence = ReferenceField("Sequence")

#     @property
#     def project(self):
#         return self.sequence.project

#     @property
#     def user_name(self):
#         return self.project.creator.name

# user = User(name = "Martin").save()
# project = Project(name = "Test Project", creator = user).save()
# sequence = Sequence(name="seq_001", project = project).save()
# shot = Shot(name = "001", sequence = sequence).save()

# shot = Shot.objects().first()
# print(shot.user_name)

# search = Shot.objects(name = "001")
# search.delete()

##Delete
# project = Project.objects().first()
# project.delete()




##INHERITANCE
# class Shot(Document):
#     name = StringField()
#     width = IntField()
#     height = IntField()

#     meta = {
#         "allow_inheritance": True
#     }

# class StereoShot(Shot):
#     is_conversion = BooleanField()
    
# shot = Shot(name="test_shots").save()
# stereo_shot = StereoShot(name="Test", is_conversion=True).save()




##DYNAMIC DOCS
# class Shot(DynamicDocument):
#     name = StringField()

# # Shot(name="test").save()
# shot = Shot.objects().first()

# # shot.first_frame = 1
# # shot.save()

# shot = Shot(name="test2", last_frame = 100, aspect_ration = 2).save()




##TIMESAVING COMMANDS
class Test(Document):
    name = StringField()

before = time.time()

l = list()

for i in range(20000):
    t = Test(name = "test")
    l.append(t)

Test.objects.insert(l)
print(time.time() - before)
#before using list: 5.349799156188965 seconds
#after using list: 1.0051321983337402 seconds

