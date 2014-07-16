'use strict';

/* Users Admin controller v6 */
angular.module('bombolone.controllers.usersAdmin', [])
.controller('UsersAdminCtrl', [
  "$scope", 
  "$resource", 
  "$rootScope", 
  "api",
  function($scope, $resource, $rootScope, api) {
    var upload;
    if (path.match(/^\/admin\/users\/new\/?$/i) || path.match(/^\/admin\/users\/([^\/]+)\/?$/i)) {
      upload = {
        module: "avatars",
        frame_class: "upload_target",
        action: "/upload_avatar/",
        action_iframe: "/upload_avatar_iframe/",
        action_base: "{{ url_for('users.update', _id=_id) }}"
      };
    }

    $scope.tab_menu = {
      selected: "account"
    };

    if (path.match(/^\/admin\/users\/?$/i)) {
      var params = {};
      $rootScope.admin_module = "users";
      $scope.sort_table = "-created";
      api.usersList.get(params, function(resource) {
        $rootScope.items_list = resource.users;
      });
    }
  }
]);
