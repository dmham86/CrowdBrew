/**
* Common Directives
* @namespace crowdBrew.common.directives
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.common.directives',[])
    .directive('spinner', function(){
      return {
        restrict: 'A',
        scope: {
          spinner: '@'
        },
        replace: true,
        transclude: true,
        template: '<div cg-busy="{promise: promise, backdrop: true}"><ng-transclude></ng-transclude></div>',
        controller: ['$scope', function($scope) {
          $scope.promise = null;

          $scope.$on('spinner:start', function(event, spinner) {
            if(spinner.key == $scope.spinner) {
              $scope.promise = spinner.promise;
            }
          })
        }]
      };
    });

})();
