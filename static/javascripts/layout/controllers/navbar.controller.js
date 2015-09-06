/**
* NavbarController
* @namespace thinkster.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.layout.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace NavbarController
  */
  function NavbarController($scope, Authentication) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();

    vm.logout = logout;
    vm.syncAuth = syncAuth;


    /**
    * @name logout
    * @desc Log the user out
    * @memberOf thinkster.layout.controllers.NavbarController
    */
    function logout() {
      Authentication.logout();
    }

    function syncAuth(username) {
      if (!!username && Authentication.isAuthenticated()) {
        var account = Authentication.getAuthenticatedAccount();
        if(account.username != username) {
          Authentication.unauthenticate();
        }
      }
      else {
        Authentication.unauthenticate();
      }
    }
  }
})();
