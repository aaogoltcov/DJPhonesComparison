from django.db import models


class Phone(models.Model):
    os_choices = [
        ('IOS', 'IOS'),
        ('Android', 'Android'),
    ]
    ram_choices = [
        (2, 2),
        (4, 4),
        (8, 8),
        (16, 16),
        (32, 32),
        (62, 64),
        (124, 124),
    ]
    boolean_choices = [
        (True, 'Есть'),
        (False, '-'),
    ]
    id = models.AutoField(primary_key=True)
    phone_model = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    os = models.TextField(max_length=10, choices=os_choices)
    ram = models.DecimalField(max_digits=3, decimal_places=0)
    pixel_per_inch = models.DecimalField(max_digits=6, decimal_places=0)
    dual_camera = models.BooleanField(default=False, choices=boolean_choices)
    cpu = models.TextField(max_length=50)
    screen_resolution = models.TextField(max_length=30)
    fm_radio = models.BooleanField(default=False, choices=boolean_choices)

    def __str__(self):
        return self.phone_model, self.os, self.cpu, self.screen_resolution, self.dual_camera, self.fm_radio


class PhoneAddInfo(models.Model):
    id = models.AutoField(primary_key=True)
    phone_model = models.ForeignKey(Phone, null=True, on_delete=models.CASCADE)
    add_info = models.TextField(max_length=50)

    def __str__(self):
        return self.add_info
