/**
* NewTastingController
* @namespace crowdBrew.tastings.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.tastings.controllers')
    .controller('NewTastingController', NewTastingController);

  NewTastingController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Tastings'];

  /**
  * @namespace NewTastingController
  */
  function NewTastingController($rootScope, $scope, Authentication, Snackbar, Tastings) {
    var vm = this;
    vm.appearance = "2.5";
    vm.smell = "2.5";
    vm.taste = "2.5";
    vm.mouthfeel = "2.5";
    vm.overall = "2.5";

    $scope.updateBrews = function(typed) {
      vm.newBrews = Tastings.brewSearch(typed);
      vm.newBrews.then(function(data){
        var newBrews = angular.fromJson(data).data;
        $scope.brews = newBrews;//[];
        //for(var i = 0; i < newBrews.length; i++){
          //$scope.brews.push(newBrews[i].name+'<br/><span class-"small">'+newBrews[i].description+'</span>');
        //}
      })
    }

    $scope.setBrew = function(suggestion) {
      vm.brew_id = suggestion;
      vm.brewSelected = true;
    }

    $scope.getBrews = function() {
      return $scope.brews;
    }

    $scope.brews = [];


    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.submit = submit;

    /**
    * @name submit
    * @desc Create a new Tasting
    * @memberOf crowdBrew.tastings.controllers.NewTastingController
    */
    function submit() {

      $scope.closeThisDialog();

      Tastings.create(vm.brew_id, vm.appearance, vm.smell, vm.taste, vm.mouthfeel, vm.overall).then(createTastingSuccessFn, createTastingErrorFn);


      /**
      * @name createTastingSuccessFn
      * @desc Show snackbar with success message
      */
      function createTastingSuccessFn(data, status, headers, config) {
        $rootScope.$broadcast('tasting.created', data.data);
        Snackbar.show('Success! Tasting created.');
      }


      /**
      * @name createTastingErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createTastingErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('tasting.created.error');
        Snackbar.error(data.error);
      }
    }





  }
})();
