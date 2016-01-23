(function () {
  'use strict';

  angular
    .module('crowdBrew', [
      'thinkster',
      'angularAwesomeSlider',
      'crowdBrew.config',
      'crowdBrew.routes',
      'crowdBrew.registration',
      'crowdBrew.layout',
      'crowdBrew.brews',
      'crowdBrew.tastings',
      'crowdBrew.profiles'
    ]);

  angular
    .module('crowdBrew.config', []);
  angular
    .module('crowdBrew.routes', ['ngRoute']);

    angular
    .module('crowdBrew')
    .run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
