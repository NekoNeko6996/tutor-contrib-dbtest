from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import PluginURLs, ProjectType

class DbuiConfig(AppConfig):
    name = "tutorcontrib.dbtest.djangoapps.dbui"
    label = "dbui"
    verbose_name = "DB Test UI"

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                "namespace": "dbui",
                "regex": r"^",          # mount ở root
                "relative_path": "urls", # file urls.py cùng thư mục
            },
            ProjectType.CMS: {
                "namespace": "dbui",
                "regex": r"^",
                "relative_path": "urls",
            },
        },
    }
