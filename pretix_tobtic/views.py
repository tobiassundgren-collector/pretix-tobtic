from django_scopes import scope

from pretix.base.models import (
    Organizer, Event
)

from django.views.generic import (
    CreateView, DeleteView, ListView, TemplateView, UpdateView,
)

class ShowPageView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        orgs = Organizer.objects.all()
        
        
        for org in orgs:
            
            with scope(organizer=Organizer.objects.get(slug = org.slug)):
                orgevts = org.events.all()
                evts = []
                for evt in orgevts:
                    evt.loadedText = evt.settings.get('frontpage_text')
                    evt.loadedLogo = evt.settings.get('logo_image', as_type=str, default='')[7:]
                    evts.append(evt)   
            org.loadedEvents = evts
            org.loadedText = org.settings.get('frontpage_text')
            if(org.settings.get('organizer_logo_image') is None):
                org.loadedLogo = "tobtic/img/no-arranger-image.png"
            else:
                org.loadedLogo = org.settings.get('organizer_logo_image', as_type=str, default='')[7:]
        ctx['orgs'] = orgs
        return ctx