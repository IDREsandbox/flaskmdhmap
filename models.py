# Import from peewee
from peewee import *

# Connect to the PostgresqlDatabase

db = PostgresqlDatabase('postgres', user='postgres', password='yoh',
													 host='localhost', port=5432)
# Connect to our database.
db.connect()

# class lapd(Model):
# 	# These are all the fields it has
# 	# match up CharField/IntegerField/etc with correct type

# 	fid = CharField(primary_key=True) # primary key = unique id
# 	desc_ = CharField()
# 	slug = CharField()
# 	home_addre = CharField()
# 	sex = CharField()
# 	x = DecimalField(null = True)
# 	y = DecimalField(null = True)
	
# 	class Meta:
# 		# data is coming from schools.db
# 		database = db
# 		# and it's in the table called 'events'
# 		db_table = 'lapd_2016'


class lasd(Model):
	# These are all the fields it has
	# match up CharField/IntegerField/etc with correct type

	booking_nu = CharField(primary_key=True) # primary key = unique id
	sex = CharField()
	race = CharField()
	charge = CharField()
	charge_des = CharField()
	charge_lev = CharField()
	bail = CharField()
	year = CharField()
	longitude = DecimalField(null = True)
	latitude = DecimalField(null = True)
	slug = CharField()
	
	class Meta:
		# data is coming from schools.db
		database = db
		# and it's in the table called 'events'
		db_table = 'lasd_2012_2016'


