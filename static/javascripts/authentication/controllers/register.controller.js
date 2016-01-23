/**
* Register controller
* @namespace crowdBrew.registration.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.registration.controllers')
    .controller('RegistrationController', RegistrationController);

  RegistrationController.$inject = ['$location', '$scope', 'Registration', 'Authentication'];

  /**
  * @namespace RegistrationController
  */
  function RegistrationController($location, $scope, Registration, Authentication) {
    var vm = this;

    vm.register = register;

    /**
    * @name register
    * @desc Register a new user
    * @memberOf crowdBrew.registration.controllers.RegistrationController
    */
    function register() {
      Registration.register(vm.email, vm.password, vm.username, vm.account_type, vm.brewery_name).then(
          function(data){vm.success = true;},
          function(data){vm.error = data;}
      );
    }

    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf crowdBrew.registration.controllers.RegistrationController
     */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }
  }
})();
