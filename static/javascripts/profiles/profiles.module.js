(function () {
  'use strict';

  angular
    .module('crowdBrew.profiles', [
      'crowdBrew.profiles.controllers',
      'crowdBrew.profiles.services'
    ])
    .filter('size', function() {
      var reg = /(\?|&)s=[0-9]+/;
      // Adds s={size} parameter to string and replaces existing
      return function(input, size) {
        input = input || '';
        if(input.match(reg)) { // Already has a s parameter
          return input.replace(reg, '$1s='+size);
        }
        else if(input.match(/\?/)) { // Has parameters, but no s
          return input + '&s='+size;
        }
        else { // no url parameters
          return input + '?s='+size;
        }
      };
    });

  angular
    .module('crowdBrew.profiles.controllers', []);

  angular
    .module('crowdBrew.profiles.services', []);
})();
