from django.db import models


class dna(models.Model):

    dna_seq = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.dna_seq
