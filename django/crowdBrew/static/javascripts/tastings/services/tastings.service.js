/**
* Tastings
* @namespace crowdBrew.tastings.services
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.tastings.services')
    .factory('Tastings', Tastings);

  Tastings.$inject = ['$http'];

  /**
  * @namespace Tastings
  * @returns {Factory}
  */
  function Tastings($http) {
    var Tastings = {
      all: all,
      create: create,
      getForUser: getForUser,
      getForBrew: getForBrew,
      brewSearch: brewSearch
    };

    return Tastings;

    ////////////////////

    /**
    * @name all
    * @desc Get all Tastings
    * @returns {Promise}
    * @memberOf crowdBrew.tastings.services.Tastings
    */
    function all() {
      return $http.get('/app/api/v1/tastings/');
    }


    /**
    * @name create
    * @desc Create a new Tasting
    * @param {string} content The content of the new Brew
    * @returns {Promise}
    * @memberOf crowdBrew.tastings.services.Tastings
    */
    function create(brew_id, appearance, smell, taste, mouthfeel, overall) {
      return $http.post('/app/api/v1/tastings/', {
        brew_id: brew_id,
        appearance: appearance,
        smell: smell,
        taste: taste,
        mouthfeel: mouthfeel,
        overall: overall
      });
    }

    /**
     * @name get
     * @desc Get the Tastings of a given user
     * @param {string} username The username to get Tastings for
     * @returns {Promise}
     * @memberOf crowdBrew.tastings.services.Tastings
     */
    function getForUser(username) {
      return $http.get('/app/api/v1/accounts/' + username + '/tastings/');
    }

    /**
     * @name get
     * @desc Get the Tastings of a given user
     * @param {string} brew The brew to get Tastings for
     * @returns {Promise}
     * @memberOf crowdBrew.tastings.services.Tastings
     */
    function getForBrew(brew) {
      return $http.get('/app/api/v1/brews/' + brew + '/tastings/');
    }

    /**
     * @name brewSearch
     * @desc Find a Brew from sear
     * @param {string} searchText The text used to find a brew
     * @returns {Promise}
     * @memberOf crowdBrew.tastings.services.Tastings
     */
    function brewSearch(searchText) {
      return $http.get('/app/api/v1/brews/?search=' + searchText);
    }
  }
})();
