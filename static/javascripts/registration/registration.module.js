(function () {
  'use strict';

  angular
    .module('crowdBrew.registration', [
      'crowdBrew.registration.controllers',
      'crowdBrew.registration.services',
      'crowdBrew.common',
      'cgBusy'
    ]);

  angular
    .module('crowdBrew.registration.controllers', ['thinkster']);

  angular
    .module('crowdBrew.registration.services', ['ngCookies']);
})();
