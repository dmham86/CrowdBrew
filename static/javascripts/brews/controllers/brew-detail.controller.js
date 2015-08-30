/**
* BrewDetailController
* @namespace crowdBrew.brews.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.brews.controllers')
    .controller('BrewDetailController', BrewDetailController);

  BrewDetailController.$inject = ['$location', '$routeParams', 'Brews', 'Snackbar'];

  /**
  * @namespace BrewDetailController
  */
  function BrewDetailController($location, $routeParams, Brews, Snackbar) {
    var vm = this;

    vm.brew = undefined;

    activate();


    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf crowdBrew.brews.controllers.BrewDetailController
    */
    function activate() {
      var id = $routeParams.id;

      Brews.detail(id).then(brewDetailSuccessFn, brewDetailErrorFn);
    }

    /**
      * @name brewDetailSucessFn
      * @desc Update `brew` on viewmodel
      */
    function brewDetailSuccessFn(data, status, headers, config) {
      vm.brew = data.data;
    }

    /**
    * @name brewDetailErrorFn
    * @desc Redirect to index and show error Snackbar
    */
    function brewDetailErrorFn(data, status, headers, config) {
      $location.url('/');
      Snackbar.error('That brew does not exist.');
    }

  }
})();
