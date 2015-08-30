/**
* Tastings
* @namespace crowdBrew.tastings.directives
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.tastings.directives')
    .directive('tastings', tastings);

  /**
  * @namespace Tastings
  */
  function tastings() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf crowdBrew.tastings.directives.Tastings
    */
    var directive = {
      controller: 'TastingsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        tastings: '='
      },
      templateUrl: '/static/templates/tastings/tastings.html'
    };

    return directive;
  }
})();
