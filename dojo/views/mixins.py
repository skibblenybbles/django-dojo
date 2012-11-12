import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class DojoConfigMixin(object):
    dojo_config = None
    dojo_production = None
    
    dojo_static_path = None
    dojo_static_url = None
    
    dojo_source_path = None
    dojo_production_path = None
    
    dojo_source_url = None
    dojo_production_url = None
    
    def get_dojo_production(self):
        if self.dojo_production is None:
            self.dojo_production = getattr(
                settings,
                "DOJO_PRODUCTION",
                False,
            )
        
        return self.dojo_production
    
    def get_dojo_static_path(self):
        if self.dojo_static_path is None:
            self.dojo_static_path = os.path.normpath(
                getattr(
                    settings,
                    "STATIC_ROOT",
                    "",
                ),
            )
        
        return self.dojo_static_path
    
    def get_dojo_static_url(self):
        if self.dojo_static_url is None:
            self.dojo_static_url = os.path.normpath(
                getattr(
                    settings,
                    "STATIC_URL",
                    "",
                ),
            )
        
        return self.dojo_static_url
    
    def get_dojo_source_path(self):
        if self.dojo_source_path is None:
            self.dojo_source_path = os.path.normpath(
                getattr(
                    settings,
                    "DOJO_SOURCE_PATH",
                    os.path.join(
                        getattr(
                            settings, 
                            "STATIC_ROOT", 
                            "",
                        ),
                        "dojo"
                    ),
                ),
            )
            
        return self.dojo_source_path
    
    def get_dojo_production_path(self):
        if self.dojo_production_path is None:
            self.dojo_production_path = os.path.normpath(
                getattr(
                    settings,
                    "DOJO_PRODUCTION_PATH",
                    os.path.join(
                        self.get_dojo_source_path(),
                        "production",
                    ),
                ),
            )
        
        return self.dojo_production_path
    
    def get_dojo_source_url(self):
        if self.dojo_source_url is None:
            static_path = self.get_dojo_static_path()
            source_path = self.get_dojo_source_path()
            if not source_path.startswith(static_path):
                raise ImproperlyConfigured(
                    u"DojoConfigMixin detected that settings.DOJO_SOURCE_PATH " \
                    u"is not a subdirectory of settings.STATIC_ROOT.",
                )
            self.dojo_source_url = os.path.join(
                self.get_dojo_static_url(),
                source_path[len(static_path) + 1:],
            )
            
        return self.dojo_source_url
    
    def get_dojo_production_url(self):
        if self.dojo_production_url is None:
            static_path = self.get_dojo_static_path()
            production_path = self.get_dojo_production_path()
            if not production_path.startswith(static_path):
                raise ImproperlyConfigured(
                    u"DojoConfigMixin detected that settings.DOJO_PRODUCTION_PATH " \
                    u"is not a subdirectory of settings.STATIC_ROOT.",
                )
            self.dojo_production_url = os.path.join(
                self.get_dojo_static_url(),
                production_path[len(static_path) + 1:],
            )
        
        return self.dojo_production_url
    
    def get_dojo_config(self):
        if self.dojo_config is None:
            self.dojo_config = {
                'url': self.get_dojo_production_url() if \
                    self.get_dojo_production() else \
                    self.get_dojo_source_url(),
            }
            
        return self.dojo_config
    
    def get_dojo_config_data(self):
        return {
            'dojo_config': self.get_dojo_config(),
        }
