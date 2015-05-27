/**
* Brews
* @namespace crowdBrew.brews.services
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.brews.services')
    .factory('Brews', Brews);

  Brews.$inject = ['$http'];

  /**
  * @namespace Brews
  * @returns {Factory}
  */
  function Brews($http) {
    var Brews = {
      all: all,
      create: create,
      get: get,
      detail: detail
    };

    return Brews;

    ////////////////////

    /**
    * @name all
    * @desc Get all Brews
    * @returns {Promise}
    * @memberOf crowdBrew.brews.services.Brews
    */
    function all() {
      return $http.get('/app/api/v1/brews/');
    }


    /**
    * @name create
    * @desc Create a new Brews
    * @param {string} content The content of the new Brew
    * @returns {Promise}
    * @memberOf crowdBrew.brews.services.Brews
    */
    function create(name, description, style, type, abv) {
      return $http.post('/app/api/v1/brews/', {
        name: name,
        description: description,
        style: style,
        type: type,
        abv: abv
      });
    }

    /**
     * @name get
     * @desc Get the Brews of a given user
     * @param {string} username The username to get Brews for
     * @returns {Promise}
     * @memberOf crowdBrew.brews.services.Brews
     */
    function get(username) {
      return $http.get('/app/api/v1/accounts/' + username + '/brews/');
    }

    /**
     * @name detail
     * @desc Get the Details of a given brew
     * @param {Long} id The id to get details for
     * @returns {Promise}
     * @memberOf crowdBrew.brews.services.Brews
     */
    function detail(id) {
      return $http.get('/app/api/v1/brews/' + id + '/');
    }
  }
})();
