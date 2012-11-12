from django import template
from classytags.core import Options
from classytags.helpers import InclusionTag
from classytags.arguments import Argument, MultiValueArgument

from ..views import DojoConfigMixin


register = template.Library()


@register.tag
class DojoConfig(DojoConfigMixin, InclusionTag):
    name = "dojo_config"
    template = "dojo/_dojo-config.html"
    options = Options(
        MultiValueArgument("applications", required=False),
    )
    
    def get_context(self, context, applications):
        context.update({
            "applications": applications,
        })
        context.update(self.get_dojo_config_data())
        return context
