from django.db import models
from django.utils.timezone import now


class User(models.Model):
    firstName = models.TextField("first_name")
    lastName = models.TextField("last_name")
    username = models.TextField("user_name")
    email = models.EmailField(max_length=254)
    phone = models.TextField()
    image = models.TextField(null=True)
    password = models.TextField()
    isActive = models.BooleanField("is_active", default=True)
    isDeleted = models.BooleanField("is_deleted", default=False)
    createdAt = models.DateField("created_at", auto_now_add=True)
    updatedAt = models.DateField("updated_at", auto_now=True)
    lastActiveOn = models.DateTimeField("last_active_on", default=now)

    def __str__(self):
        fullName = self.firstName + " " + self.lastName
        return fullName

    class Meta:
        ordering = ['firstName']
        

class UserAccessTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    accessToken = models.TextField("access_token")
    expiresAt = models.DateTimeField("expires_at")

    createdAt = models.DateTimeField("created_at", auto_now_add=True)
    updatedAt = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        verbose_name = "User Access Token"
        verbose_name_plural = "User Access Tokens"


class UserPasswordResetTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resetToken = models.TextField("reset_token")
    expiresAt = models.DateField("expires_at")
    
    createdAt = models.DateField("created_at", auto_now_add=True)
    updatedAt = models.DateField("updated_at", auto_now=True)