/**
* Brews
* @namespace crowdBrew.brews.directives
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.brews.directives')
    .directive('brews', brews);

  /**
  * @namespace Brews
  */
  function brews() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf crowdBrew.brews.directives.Brews
    */
    var directive = {
      controller: 'BrewsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        brews: '='
      },
      templateUrl: '/static/templates/brews/brews.html'
    };

    return directive;
  }
})();
