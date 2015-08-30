/**
* ProfileController
* @namespace crowdBrew.profiles.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.profiles.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Brews', 'Profile', 'Snackbar'];

  /**
  * @namespace ProfileController
  */
  function ProfileController($location, $routeParams, Brews, Profile, Snackbar) {
    var vm = this;

    vm.profile = undefined;
    vm.brews = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf crowdBrew.profiles.controllers.ProfileController
    */
    function activate() {
      var username = $routeParams.username;

      Profile.get(username).then(profileSuccessFn, profileErrorFn);
      Brews.get(username).then(brewsSuccessFn, brewsErrorFn);

      /**
      * @name profileSuccessProfile
      * @desc Update `profile` on viewmodel
      */
      function profileSuccessFn(data, status, headers, config) {
        vm.profile = data.data;
      }


      /**
      * @name profileErrorFn
      * @desc Redirect to index and show error Snackbar
      */
      function profileErrorFn(data, status, headers, config) {
        $location.url('/');
        Snackbar.error('That user does not exist.');
      }


      /**
        * @name brewsSucessFn
        * @desc Update `brews` on viewmodel
        */
      function brewsSuccessFn(data, status, headers, config) {
        vm.brews = data.data;
      }


      /**
        * @name brewsErrorFn
        * @desc Show error snackbar
        */
      function brewsErrorFn(data, status, headers, config) {
        Snackbar.error(data.data.error);
      }
    }
  }
})();
