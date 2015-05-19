/**
* IndexController
* @namespace crowdBrew.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Brews', 'Snackbar'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, Authentication, Brews, Snackbar) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.brews = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf crowdBrew.layout.controllers.IndexController
    */
    function activate() {
      console.log('activated');
      Brews.all().then(brewsSuccessFn, brewsErrorFn);

      $scope.$on('brew.created', function (event, brew) {
        vm.brews.unshift(brew);
        console.log(vm.brews);
      });

      $scope.$on('brew.created.error', function () {
        // do nothing
      });


      /**
      * @name brewsSuccessFn
      * @desc Update brews array on view
      */
      function brewsSuccessFn(data, status, headers, config) {
        vm.brews = data.data;
      }


      /**
      * @name brewsErrorFn
      * @desc Show snackbar with error
      */
      function brewsErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
  }
})();
