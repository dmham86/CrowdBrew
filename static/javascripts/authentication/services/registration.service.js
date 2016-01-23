/**
* Registration
* @namespace crowdBrew.registration.services
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.registration.services')
    .factory('Registration', Registration);

  Registration.$inject = ['$cookies', '$http'];

  /**
  * @namespace Registration
  * @returns {Factory}
  */
  function Registration($cookies, $http) {
    /**
    * @name Registration
    * @desc The Factory to be returned
    */
    var Registration = {
      register: register
    };

    return Registration;

    ////////////////////

    /**
    * @name register
    * @desc Try to register a new user
    * @param {string} email The email entered by the user
    * @param {string} password The password entered by the user
    * @param {string} username The username entered by the user
    * @returns {Promise}
    * @memberOf crowdBrew.registration.services.Registration
    */
    function register(email, password, username, account_type, brewery_name) {
      var regPromise = jQuery.Deferred();
      $http.post('app/api/v1/registration/', {
        username: username,
        password: password,
        email: email,
        account_type: account_type,
        brewery_name: brewery_name
      }).then(registerSuccessFn, registerErrorFn);
      return regPromise.promise();

      /**
      * @name registerSuccessFn
      * @desc Return the user object
      */
      function registerSuccessFn(data, status, headers, config) {
        regPromise.resolve(data.data);
      }

      /**
      * @name registerErrorFn
      * @desc Return the failure message
      */
      function registerErrorFn(data, status, headers, config) {
        return regPromise.reject(data.data.message);
      }
    }
  }
})();
