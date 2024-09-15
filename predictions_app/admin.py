from django.contrib import admin
from .models import Laliga_Matches

# Register your models here.


admin.site.register(Laliga_Matches)


"""class LaLigaMatchAdmin(admin.ModelAdmin):
    list_display = ('Season', 'Date', 'Hometeam', 'Awayteam', 'Fthg', 'Ftag', 'Ftr', 'Hthg', 'Htag', 'Htr')
    list_filter = ('Season', 'Hometeam', 'Awayteam', 'Ftr')
    search_fields = ('Hometeam', 'Awayteam', 'Season') """
