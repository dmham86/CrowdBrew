(function () {
  'use strict';

  angular
    .module('crowdBrew.config')
    .config(config);

  config.$inject = ['$locationProvider', '$provide', '$httpProvider'];

  /**
  * @name config
  * @desc Enable HTML5 routing
  */
  function config($locationProvider, $provide, $httpProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
    registerInterceptor($provide, $httpProvider);
  }

  function registerInterceptor($provide, $httpProvider) {
    // register the interceptor as a service
    $provide.factory('myHttpInterceptor', function($q) {
      return {
        'responseError': function(rejection) {
          if(rejection.status == 401){
            // Redirect to homepage, will clear out auth token
            window.location = "/";
          }
          return $q.reject(rejection);
        }
      };
    });

    $httpProvider.interceptors.push('myHttpInterceptor');
  }
})();
