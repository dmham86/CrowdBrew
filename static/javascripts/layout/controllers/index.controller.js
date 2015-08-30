/**
* IndexController
* @namespace crowdBrew.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Brews', 'Snackbar'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, Authentication, Brews, Snackbar) {
    var vm = this, selectingAction = false, actionTimeout;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.brews = [];

    vm.isSelectingAction = isSelectingAction;
    vm.setSelectingAction = setSelectingAction;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf crowdBrew.layout.controllers.IndexController
    */
    function activate() {
      Brews.all().then(brewsSuccessFn, brewsErrorFn);

      $scope.$on('brew.created', function (event, brew) {
        vm.brews.unshift(brew);
      });

      $scope.$on('brew.created.error', function () {
        // do nothing
      });


      /**
      * @name brewsSuccessFn
      * @desc Update brews array on view
      */
      function brewsSuccessFn(data, status, headers, config) {
        vm.brews = data.data;
      }


      /**
      * @name brewsErrorFn
      * @desc Show snackbar with error
      */
      function brewsErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }

    /**
     * @name isSelectingAction
     * @desc Returns true if user is currently selecting an action from the menu
     * @return User is selecting action
     * @memberOf crowdBrew.layout.controllers.IndexController
     */
    function isSelectingAction() {
      return selectingAction;
    }

    /**
     * @name setSelectingAction
     * @desc Set user is selecing action. Debounced on false
     * @memberOf crowdBrew.layout.controllers.IndexController
     */
    function setSelectingAction(selecting) {
      if(selecting!=true) {
        clearTimeout(actionTimeout);
        actionTimeout = setTimeout(function() { selectingAction = false; }, 400)
      }
      else {
        clearTimeout(actionTimeout);
        selectingAction = true;
      }

    }
  }
})();
