from django.contrib.auth.models import User
from django.db import models


def profile_image_directory_path(instance: "Profile", filename: str) -> str:
    return "myauth/profile_{pk}/images/{filename}".format(
        pk=instance.user.pk,
        filename=filename
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, upload_to=profile_image_directory_path)


class ProfileAvatar(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=profile_image_directory_path)
