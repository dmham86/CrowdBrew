/**
* Tasting
* @namespace crowdBrew.tastings.directives
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.tastings.directives')
    .directive('tasting', tasting);

  /**
  * @namespace Tasting
  */
  function tasting() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf crowdBrew.tastings.directives.Tasting
    */
    var directive = {
      restrict: 'E',
      scope: {
        tasting: '='
      },
      templateUrl: '/static/templates/tastings/tasting.html'
    };

    return directive;
  }
})();
