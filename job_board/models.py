from django.db import models

# Create your models here.
# model => python class
# model represents a table in the db
# attributes are the fields

class JobPosting(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	company = models.CharField(max_length=100)
	salary = models.IntegerField()
	is_active = models.BooleanField(default=False)

# makemigrations
## -> creates intructions telling django how the db have changed

# migrate
# -> Applies the above changes


# CRUD Operations
# Create
# Read
# Update
# Delete


# model manager -> objects
# JobPosting.objects.all()
# JobPosting.objects.get(id=1)

