(function () {
  'use strict';

  angular
    .module('crowdBrew.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/', {
      controller: 'IndexController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/layout/index.html'
    }).when('/register', {
      controller: 'RegistrationController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/registration/register.html'
    }).when('/user/:username', {
      controller: 'ProfileController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/profiles/profile.html'
    }).when('/user/:username/settings', {
      controller: 'ProfileSettingsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/profiles/settings.html'
    }).when('/brew/:id', {
      controller: 'BrewDetailController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/brews/brew-detail.html'
    }).otherwise('/');
  }
})();
