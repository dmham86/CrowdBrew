(function () {
  'use strict';

  angular
    .module('crowdBrew.brews', [
      'crowdBrew.brews.controllers',
      'crowdBrew.brews.directives',
      'crowdBrew.brews.services'
    ]);

  angular
    .module('crowdBrew.brews.controllers', []);

  angular
    .module('crowdBrew.brews.directives', ['ngDialog']);

  angular
    .module('crowdBrew.brews.services', []);
})();
