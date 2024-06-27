from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings

cipher_suite = Fernet(settings.ENCRYPTION_KEY)


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Password(models.Model):
    service_name = models.OneToOneField(
        Service, on_delete=models.CASCADE, related_name="password"
    )
    encrypted_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.encrypted_password.startswith("gAAAAA"):
            self.encrypted_password = cipher_suite.encrypt(
                self.encrypted_password.encode()
            ).decode()
        super(Password, self).save(*args, **kwargs)

    def get_decrypted_password(self):
        return cipher_suite.decrypt(self.encrypted_password.encode()).decode()

    def __str__(self):
        return str(self.service_name)
