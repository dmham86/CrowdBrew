(function () {
  'use strict';

  angular
    .module('crowdBrew.tastings', [
      'crowdBrew.tastings.controllers',
      'crowdBrew.tastings.directives',
      'crowdBrew.tastings.services',
      'ui.bootstrap'
    ]);

  angular
    .module('crowdBrew.tastings.controllers', []);

  angular
    .module('crowdBrew.tastings.directives', ['ngDialog']);

  angular
    .module('crowdBrew.tastings.services', []);
})();
