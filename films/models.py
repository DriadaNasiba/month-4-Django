from django.db import models


class Film(models.Model):
    GENRE = (
        ('Фантази', 'Фантази'),
        (' Ужасы', 'Ужасы'),
        ( 'Триллер','Триллер')
    )
    image = models.ImageField(upload_to= 'films/', verbose_name= 'загрузите фото')
    title = models.CharField(max_length=100, verbose_name= 'укажите название фильма')
    create_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр',
                              default='Ужасы')
    author = models.CharField(max_length=100, default= 'Иванов Иван')
    description = models.TextField(verbose_name= 'Укажите описание фильма')
    trailer_film = models.URLField(verbose_name='Встаьте ссылку трейлера фильма')

    def _str_(self):
        return self.title
    
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

class Reviews(models.Model):
    films_choice = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100, verbose_name='как вас зовут?')
    text = models.TextField( verbose_name= 'как вам фильм?')   

    def _str_(self):
        return f'{self.films_choice}-{self.user_name}'
    
    class Meta:
        verbose_name = 'коментарий'
        verbose_name_pural = 'коментарии'  

   


