from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False)

def create_or_update_user_profile( sender, instance, created, **kwargs ):
    """create the user profile 

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
        created (_type_): _description_
    """
    UserProfile.objects.create(user=instance)
