/**
* Brew
* @namespace crowdBrew.brews.directives
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.brews.directives')
    .directive('brew', brew);

  /**
  * @namespace Brew
  */
  function brew() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf crowdBrew.brews.directives.Brew
    */
    var directive = {
      restrict: 'E',
      scope: {
        brew: '='
      },
      templateUrl: '/static/templates/brews/brew.html'
    };

    return directive;
  }
})();
