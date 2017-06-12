angular.module('e-sports').controller('GameEditController', ['GameService', 'UtilService', '$location', '$routeParams', function (GameService, UtilService, $location, $routeParams) {
    var vm = this;
    vm.game;
    vm.isEdit;

    function init() {
        var game_id = $routeParams.game_id;

        if (game_id){
            vm.getGame(game_id);
            vm.isEdit = true;
        }
    }

    vm.saveGame = function () {
       var file = document.getElementById('game-file').files[0],
       reader = new FileReader();

       reader.onloadend = function(e) {
      var data = e.target.result;
      //send your binary data via $http or $resource or do anything else with it
    }

       reader.readAsBinaryString(file);

        if (vm.isEdit){
            GameService.updateGame(vm.game).then(function (success) {
                $location.path('/');
            }, function (error) {
                console.error("Error on update game. " + error.statusText);
            });
        }else{
            GameService.saveGame(vm.game).then(function (success) {
                $location.path('/');
            }, function (error) {
                console.error("Error on save game. " + error.statusText);
            });
        }
    }

    vm.getGame = function (game_id) {
        GameService.getGame(game_id).then(function (success) {
            vm.game = success.data;
            vm.game.release_date = UtilService.MMDDYYYYtoDate(vm.game.release_date);
        }, function (error) {
            console.error("Error on get game. " + error.statusText);
        });
    }

    vm.deleteGame = function () {
        GameService.deleteGame(vm.game.id).then(function (success) {
            $location.path('/');
        }, function (error) {
            console.error("Error on remove game. " + error.statusText);
        });
    }

    vm.cancel = function(){
        $location.path('/');
    }

    init();

}]);