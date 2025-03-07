from django.db import models
from django.contrib.auth.models import AbstractUser,User
import re
from django.core.exceptions import ValidationError


def validatePhone(value):
    regex = r'^[0]{1}[7]{1}[01245678]{1}[0-9]{7}$'

    if not re.match(regex, value):
        raise ValidationError("Phone number is not valid, use this format (0710000000)")


# Create your models here.

#--------------------- customize default user model ------------------------#
 
class User(AbstractUser):
    phone = models.CharField(max_length=15, validators=[validatePhone])
    address = models.TextField(blank=True, null=True)
    userPic = models.ImageField(blank=True, null=True, default='images/propic.jpeg', upload_to='images')


#------------------- Association Model -----------------------#

class Association(models.Model):
    AssociationName = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    profilePic = models.ImageField(blank=True, null=True, default='images/logo1', upload_to='associatePic')
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_associations")

    def __str__(self):
        return self.AssociationName
    

#----------------------- Members Model --------------------------#

class AssociationMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memberships")
    association = models.ForeignKey(Association, on_delete=models.CASCADE, related_name="members")
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, default="member")
    adminAccept = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.association}"
    

    class Meta:
        unique_together = ('user', 'association')  # Prevent duplicate membership

