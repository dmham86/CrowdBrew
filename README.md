CROWD BREW

A website for rating and sharing homebrews. All homebrewers that have ever shared their brews with friends and family know that their feedback is not very helpful. "That's good!" or "I really like it!" doesn't help you brew better beer. CrowdBrew is designed to draw more useful feedback out of tasters and collect that into useful information about how to improve the brew.

required
pip
- Pillow
- djangorestframework
- drf-nested-routers
- django_compressor
- django-gravatar2
- django-registration-redux

bower
- angular
- angular-cookies
- angular-route
- bootstrap
- bootstrap-material-design
- jquery
- snackbarjs
- ngDialog
- underscore
- ng-slider
- allmighty-autocomplete
- ngAutocomplete


Setup
- Copy django/crowdBrew/crowdBrew/settings.py.template to settings.py in the same folder.
- Configure settings for your database and any other settings necessary
- cd to django/crowdBrew/static and run "bower install ../bower.json"
