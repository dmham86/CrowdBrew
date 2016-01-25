/**
* Profile
* @namespace crowdBrew.common.services
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.common.services', [])
    .factory('SpinnerService', SpinnerService);

  SpinnerService.$inject = ['$rootScope'];

  /**
  * @namespace SpinnerService
  * Want to keep it decoupled in case I choose to change it up
  */
  function SpinnerService($rootScope) {
    /**
    * @name Profile
    * @desc The factory to be returned
    * @memberOf crowdBrew.profiles.services.Profile
    */
    var Spinner = {
      spin: spin
    };

    return Spinner;

    function spin(promise, key) {
      if(key == undefined) {
        key = 'mainSpinner';
      }
      $rootScope.$broadcast('spinner:start', {key: key, promise: promise});
    }
  }
})();
