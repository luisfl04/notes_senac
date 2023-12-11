from django.db import models

class Note(models.Model):
    
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 60)
    description = models.TextField(max_length = 250)
    done = models.BooleanField(default = False)
    
    
    def make_done(self):
        self.done = True
        self.save()

    def __str__(self):
        return self.description
    