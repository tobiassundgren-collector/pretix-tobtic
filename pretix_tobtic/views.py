from django_scopes import scope
from datetime import date

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
        orgs_with_events = []

        for org in orgs:
            with scope(organizer=Organizer.objects.get(slug = org.slug)):
                today = date.today()
                orgevts = org.events.filter(
                    live=True,
                    is_public=True,
                    date_from__gte=today)
                evts = []
                for evt in orgevts:
                    evt.loadedText = evt.settings.get('frontpage_text')
                    if(evt.settings.get('logo_image') is None):
                        evt.loadedLogo = "../static/tobtic/img/no-arranger-image.png"
                    else:
                        evt.loadedLogo = evt.settings.get('logo_image', as_type=str, default='')[7:]
                    evts.append(evt)   
            org.loadedEvents = evts
            org.loadedText = org.settings.get('frontpage_text')
            if(org.settings.get('organizer_logo_image') is None):
                org.loadedLogo = "../static/tobtic/img/no-arranger-image.png"
            else:
                org.loadedLogo = org.settings.get('organizer_logo_image', as_type=str, default='')[7:]
            if(len(evts)  > 0):
                orgs_with_events.append(org)
        ctx['orgs'] = orgs_with_events
        return ctx