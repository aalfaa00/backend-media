from django.db import models
import uuid



class Media(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    service_id = models.CharField(max_length=10)

    User = 'USER'
    Company = 'COMPANY'
    Service = 'SERVICE'

    CHOICES = (
        (User, 'USER'),
        (Company, 'COMPANY'),
        (Service, 'SERVICE')
    )

    service_type = models.CharField(max_length=255, choices=CHOICES)

    def __str__(self):
        return self.service_id