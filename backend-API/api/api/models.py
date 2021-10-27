from django.db import models
from datetime import date
from phone_field import PhoneField

class UserDoc(models.Model):

    img = models.ImageField(upload_to='images_uploaded',null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)
    user =models.CharField(max_length=300 )

    def __str__(self):
        return '%s ' % ( self.user )

# class constructionVideo(models.Model):
#     video_id = models.CharField(max_length=30 )
#     video-name = models.CharField(max_length=300 )
#     instructor_last_name = models.CharField(max_length=100,null=True)
#     profile_pic = models.CharField(max_length=400 ,blank=True )
#     email = models.EmailField(null=True , blank=True)
#     phone = PhoneField(blank=True, help_text='Contact phone number')
#     salary = models.DecimalField(max_digits=6, decimal_places=2 , blank=True)
#     commission = models.DecimalField(max_digits=6, decimal_places=2 , blank=True)
#     date_hired = models.DateField()
#     def __str__(self):
#          return "%s " % (self.instructor_first_name)





