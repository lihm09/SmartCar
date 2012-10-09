import datetime
from settings import *

def siteinfo(request):
    info={'site_name':SITE_NAME,
          'competition_name':COMPETITION_NAME,
          'year':datetime.datetime.now().year,
          'org':ORG}
    return info