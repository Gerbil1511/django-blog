from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    This class is used to configure the blog app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
