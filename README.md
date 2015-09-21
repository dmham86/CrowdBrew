# CROWD BREW

CrowdBrew is a website for rating and sharing homebrews. All homebrewers that have ever shared their brews with friends and family know that their feedback is not very helpful. "That's good!" or "I really like it!" doesn't help you brew better beer (especially when they're lying). CrowdBrew is designed to draw more useful feedback out of tasters and collect that into useful information about how to improve the brew.

Crowd Brew has a node.js frontend and django rest framework backend

## Required Libraries
#### pip
- Pillow
- djangorestframework
- drf-nested-routers
- django_compressor
- django-gravatar2
- django-registration-redux

#### bower (run bower.json, see *Setup* below)
- angular
- angular-cookies
- angular-route
- angular-animate
- bootstrap
- bootstrap-material-design
- angular-bootstrap
- jquery
- snackbarjs
- ngDialog
- underscore
- ng-slider


## Setup
```sh
## cd to crowdbrew root directory
cp crowdBrew/settings.py.template crowdbrew/settings.py
vi crowdBrew/settings.py
## Configure your settings as necessary ##
cd static
bower install ../bower.json
```

## Running Servers and Tests
```sh
## cd to crowdbrew root directory
### Development Server
python manage.py runserver
### Test Server with prepopulated data
python manage.py testserver authentication/fixtures/authentication_testdata.json crowd_brew/fixtures/crowd_brew_testdata.json
### Unit Tests
python manage.py test
```

## User registration
- For local testing, I would recommend downloading a mock SMTP server. FakeSMTP works great, just download the jar from https://nilhcem.github.io/FakeSMTP/download.html and run.
- Use the SMTP port you configured in settings.py
- Make sure your settings are configured with the correct hostname or IP address (add the hostname to your hosts file)
