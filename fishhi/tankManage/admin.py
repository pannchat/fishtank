from django.contrib import admin
from .models import Feed
from .models import Fish,Plant,Supplies

from .models import Timeline



admin.site.register(Feed)
admin.site.register(Fish)
admin.site.register(Plant)
admin.site.register(Supplies)
admin.site.register(Timeline)
# Register your models here.
