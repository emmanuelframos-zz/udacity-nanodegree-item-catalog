angular.module('e-sports').controller('GameEditController', function (GameService, UtilService, $location, $routeParams) {
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
        if (vm.fieldsAreValid()){
            if (vm.isEdit){
                GameService.updateGame(vm.game).then(function (success) {
                    vm.sendToGameList();
                }, function (error) {
                    console.error("Error on update game. " + error.statusText);
                });
            }else{
                GameService.saveGame(vm.game).then(function (success) {
                    vm.sendToGameList();
                }, function (error) {
                    console.error("Error on save game. " + error.statusText);
                });
            }
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
            vm.sendToGameList();
        }, function (error) {
            console.error("Error on remove game. " + error.statusText);
        });
    }

    vm.cancel = function(){
        vm.sendToGameList();
    }

    vm.sendToGameList = function(){
        $location.path('/gameList');
    }

    vm.fieldsAreValid = function(){
        if (!vm.game || !vm.game.name || !vm.game.release_date || !vm.game.description){
            var snackbar = document.getElementById("snackbar")
            snackbar.className = "show";
            setTimeout(function(){
                snackbar.className = snackbar.className.replace("show", "");
            }, 3000);
            return false;
        }
        return true;
    }

    init();

});