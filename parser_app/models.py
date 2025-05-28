from django.db import models

class Parser_Rezka(models.Model):
    title =models.TextField(max_length=200)

    def _str_(self):
      return self.title
        
    
    
