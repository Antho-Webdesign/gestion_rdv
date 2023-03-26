from django.db import models
from django.utils.text import slugify


class RendezVous(models.Model):
    nom = models.CharField(max_length=255)
    personne = models.CharField(max_length=255, null=True)

    date = models.DateTimeField()
    description = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    img = models.ImageField(upload_to="images/", default='images/default.png', blank=True, null=True)
    commentaire = models.TextField(max_length=550, null=True)
    finished = models.BooleanField(default=False)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(RendezVous, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'rendez-vous'
        verbose_name_plural = 'rendez-vous'
        ordering = ['date']
