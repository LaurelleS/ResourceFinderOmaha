from django.apps import AppConfig



class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):

        from django.db.utils import OperationalError
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        
        try:
            # create group for orgs and regular users
            finders_group, _ = Group.objects.get_or_create(name='Finders')
            posters_group, _ = Group.objects.get_or_create(name='Organizations')

            # create permissions for Event
            users_ct = ContentType.objects.get(app_label='events', model='event')
            can_add_event = Permission.objects.get(codename='add_event', content_type=users_ct)
            can_delete_event = Permission.objects.get(codename='delete_event', content_type=users_ct)
            can_change_event = Permission.objects.get(codename='change_event', content_type=users_ct)
            can_view_event = Permission.objects.get(codename='view_event', content_type=users_ct)
            
            # set permisions for groups
            posters_group.permissions.add(can_add_event, can_delete_event, can_change_event, can_view_event)
            finders_group.permissions.add(can_view_event)
            
        except OperationalError:
            pass
