/**
* NewBrewController
* @namespace crowdBrew.brews.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.brews.controllers')
    .controller('NewBrewController', NewBrewController);

  NewBrewController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Brews'];

  /**
  * @namespace NewBrewController
  */
  function NewBrewController($rootScope, $scope, Authentication, Snackbar, Brews) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.submit = submit;

    /**
    * @name submit
    * @desc Create a new Brew
    * @memberOf crowdBrew.brews.controllers.NewBrewController
    */
    function submit() {

      $scope.closeThisDialog();

      Brews.create(vm.name, vm.description, vm.style, vm.type, vm.abv).then(createBrewSuccessFn, createBrewErrorFn);


      /**
      * @name createBrewSuccessFn
      * @desc Show snackbar with success message
      */
      function createBrewSuccessFn(data, status, headers, config) {
        $rootScope.$broadcast('brew.created', data.data);
        Snackbar.show('Success! Brew created.');
      }


      /**
      * @name createBrewErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createBrewErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('brew.created.error');
        Snackbar.error(data.error);
      }
    }
  }
})();
