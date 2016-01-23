(function () {
  'use strict';

  angular
    .module('crowdBrew.registration', [
      'crowdBrew.registration.controllers',
      'crowdBrew.registration.services'
    ]);

  angular
    .module('crowdBrew.registration.controllers', ['Authentication']);

  angular
    .module('crowdBrew.registration.services', ['ngCookies']);
})();
