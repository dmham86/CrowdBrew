/**
* BrewsController
* @namespace crowdBrew.brews.controllers
*/
(function () {
  'use strict';

  angular
    .module('crowdBrew.brews.controllers')
    .controller('BrewsController', BrewsController);

  BrewsController.$inject = ['$scope'];

  /**
  * @namespace BrewsController
  */
  function BrewsController($scope) {
    var vm = this;

    vm.columns = [];

    activate();


    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf crowdBrew.brews.controllers.BrewsController
    */
    function activate() {
      $scope.$watchCollection(function () { return $scope.brews; }, render);
      $scope.$watch(function () { return $(window).width(); }, render);
    }


    /**
    * @name calculateNumberOfColumns
    * @desc Calculate number of columns based on screen width
    * @returns {Number} The number of columns containing Brews
    * @memberOf crowdBrew.brews.controllers.BrewsControllers
    */
    function calculateNumberOfColumns() {
      var width = $(window).width();

      if (width >= 1200) {
        return 4;
      } else if (width >= 992) {
        return 3;
      } else if (width >= 768) {
        return 2;
      } else {
        return 1;
      }
    }


    /**
    * @name approximateShortestColumn
    * @desc An algorithm for approximating which column is shortest
    * @returns The index of the shortest column
    * @memberOf crowdBrew.brews.controllers.BrewsController
    */
    function approximateShortestColumn() {
      var scores = vm.columns.map(columnMapFn);

      return scores.indexOf(Math.min.apply(this, scores));


      /**
      * @name columnMapFn
      * @desc A map function for scoring column heights
      * @returns The approximately normalized height of a given column
      */
      function columnMapFn(column) {
        var lengths = column.map(function (element) {
          return element.description.length;
        });

        return lengths.reduce(sum, 0) * column.length;
      }


      /**
      * @name sum
      * @desc Sums two numbers
      * @params {Number} m The first number to be summed
      * @params {Number} n The second number to be summed
      * @returns The sum of two numbers
      */
      function sum(m, n) {
        return m + n;
      }
    }


    /**
    * @name render
    * @desc Renders Brews into columns of approximately equal height
    * @param {Array} current The current value of `vm.brews`
    * @param {Array} original The value of `vm.brews` before it was updated
    * @memberOf crowdBrew.brews.controllers.BrewsController
    */
    function render(current, original) {
      if(Object.prototype.toString.call(current) !== "[object Array]") {
        // For some reason render is being called with integers on occasion and ruins everything
        return;
      }
      if (current !== original) {
        vm.columns = [];

        for (var i = 0; i < calculateNumberOfColumns(); ++i) {
          vm.columns.push([]);
        }

        for (var i = 0; i < current.length; ++i) {
          var column = approximateShortestColumn();

          vm.columns[column].push(current[i]);
        }
      }
    }
  }
})();
