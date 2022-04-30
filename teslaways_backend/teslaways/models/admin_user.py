from django.db import models
import hashlib, binascii, os
from django import forms

class AdminUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    def create_hashed_password(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        self.password = (salt + pwdhash).decode('ascii')
        return self.password


    def verify_password(self, password):
        salt = self.password[:64]
        stored_password = self.password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }

    
    class Meta:
        verbose_name = "Admin i korisnici"
        verbose_name_plural = verbose_name