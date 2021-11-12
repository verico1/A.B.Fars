from settings.models import Setting

def setting(requet, **kwargs):
    setting = Setting.objects.first()
    ctx = {'setting':setting}
    return ctx