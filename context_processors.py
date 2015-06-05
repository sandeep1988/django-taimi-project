from django.utils.translation import ugettext as _
def client_info(request):
	import client
	c = {}
	c['name'] = _(client.NAME)
	c['address'] = client.ADDRESS
	c['city'] = client.CITY
	c['province'] = client.PROVINCE
	c['country'] = client.COUNTRY
	c['phone'] = client.PHONE
	c['postal_code'] = client.POSTAL_CODE
	c['fax'] = client.FAX
	c['email'] = client.EMAIL
	return {'client': c}

def myurl( request ):
  return { 'myurlx': request.get_full_path() }