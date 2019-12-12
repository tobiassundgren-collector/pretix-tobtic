from django.utils.translation import ugettext_lazy
try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    name = 'pretix_tobtic'
    verbose_name = 'TobTic site'

    class PretixPluginMeta:
        name = ugettext_lazy('TobTic site')
        author = 'Tobias Sundgren'
        description = ugettext_lazy('Short description')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_tobtic.PluginApp'
