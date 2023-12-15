from django.db import models

# Create your models here.
class Eventdetails(models.Model):
    event = models.CharField(max_length=255, blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    event_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.event

    class Meta:
        db_table = 'EventDetails'


class Jobrequisition(models.Model):
    job_position = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.job_position

    class Meta:
        db_table = 'Jobrequisition'


class Persona(models.Model):
    persona = models.CharField(max_length=255, default=1, blank=True, null=True,)

    def __str__(self):
      return self.persona

    class Meta:
        db_table = 'Persona'


class Screeningmode(models.Model):
    screening_mode = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.screening_mode

    class Meta:
        db_table = 'Screeningmode'


class Gender(models.Model):
    gender = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
      return self.gender

    class Meta:
        db_table = 'Gender'

class Maritalstatus(models.Model):
    marital_status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
      return self.marital_status

    class Meta:
        db_table = 'Maritalstatus'

class Employeedirectory(models.Model):
    referred_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.referred_by

    class Meta:
        db_table = 'Employeedirectory'

class City(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.city

    class Meta:
        db_table = 'City'

class Experiencelevel(models.Model):
    experience_level = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.experience_level

    class Meta:
        db_table = 'Experiencelevel'

class Educationlevel(models.Model):
    education_level = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.education_level

    class Meta:
        db_table = 'Educationlevel'

class Reasonforchange(models.Model):
    reason_for_change = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
      return self.reason_for_change

    class Meta:
        db_table = 'Reasonforchange'


class Candidatedirectory(models.Model):
    event = models.ForeignKey(
        "Eventdetails",
        models.DO_NOTHING, 
        db_column="event", 
        blank=False,
        null=True
    )
    job_position = models.ForeignKey(
        "Jobrequisition",
        models.DO_NOTHING,
        db_column="job_position",
        blank=False,
        null=True,
    )
    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=False, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=True)
    email = models.CharField(max_length=50, blank=False, null=True)
    persona = models.ForeignKey(
        "Persona",
        models.DO_NOTHING,
        db_column="persona",
        blank=False,
        null=True,
        default=1,
    )
    role = models.IntegerField(blank=False, null=True)
    screening_mode = models.ForeignKey(
        "Screeningmode",
        models.DO_NOTHING,
        db_column="screening_mode",
        blank=True,
        null=True,
    )
    dob = models.DateField(blank=False, null=True)
    gender = models.ForeignKey(
        "Gender", 
        models.DO_NOTHING, 
        db_column="gender", 
        blank=False, 
        null=True
    )
    marital_status = models.ForeignKey(
        "Maritalstatus",
        models.DO_NOTHING,
        db_column="marital_status",
        blank=False,
        null=True,
    )
    contact_no_primary = models.DecimalField(
        max_digits=10, 
        decimal_places=0, 
        blank=False,
        null=True
    )
    contact_no_alternate = models.DecimalField(
        max_digits=10, 
        decimal_places=0, 
        blank=True, 
        null=True
    )
    referred_by = models.ForeignKey(
        "Employeedirectory",
        models.DO_NOTHING,
        db_column="referred_by",
        blank=True,
        null=True,
    )
    
    referred_by_other = models.CharField(max_length=250, blank=True, null=True)
    address_line = models.CharField(max_length=255, blank=False, null=True)
    city = models.ForeignKey(
        "City", 
        models.DO_NOTHING, 
        db_column="city", 
        blank=False,
        null=True
    )
    pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=False, null=True)
    experience_level = models.ForeignKey(
        "Experiencelevel",
        models.DO_NOTHING,
        db_column="experience_level",
        blank=False,
        null=True,
    )
    education_level = models.ForeignKey(
        "Educationlevel",
        models.DO_NOTHING,
        db_column="education_level",
        blank=False,
        null=True,
    )
    notice_period = models.CharField(max_length=50, blank=False, null=True)
    reason_for_change = models.ForeignKey(
        "Reasonforchange",
        models.DO_NOTHING,
        db_column="reason_for_change",
        blank=False,
        null=True,
    )
    photo_path = models.TextField(blank=True, null=True) 
    resume_path = models.TextField(blank=True, null=True) 
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(default=1)

    def __str__(self):
      return self.first_name

    
    class Meta:
        managed = False
        db_table = "crudapp_candidatedirectory"
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='full_name')
        ]
