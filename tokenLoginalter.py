import requests, lxml.html
s = requests.session()

### Here, we're getting the login page and then grabbing hidden form
### fields.  We're probably also getting several session cookies too.
 login = s.get('https://www.yelp.com/login')
 login_html = lxml.html.fromstring(login.text)
 hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
 form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
print(form)
{'csrftok': '9e34ca7e492a0dda743369433e78ccf10c1e68bbb1f453cbb80ce6eaeeebe928', 
 'context': ''}
 
### Now that we have the hidden form fields, let's add in our 
### username and password.
form['email'] = # Enter an email here.  Not mine.
form['password'] = # I'm definitely not telling you my password.
response = s.post('https://www.yelp.com/login', data=form)

### How can we tell that we logged in?  Well, these worked for me:
response.url
'https://www.yelp.com/cleveland'
'Stephen' in response.text
True
