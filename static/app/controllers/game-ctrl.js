angular.module('e-sports').controller('GameController', function (GameService, $location) {
    var vm = this;
    vm.games;

    function init() {
        vm.getGames();
    }

    vm.getGames = function () {
        GameService.getGames().then(function (success) {
            vm.games = success.data.games;
        }, function (error) {
            console.error("Error on get games. " + error.statusText);
        });
    }

    vm.updateGame = function(game_id){
        $location.path('/gameForm/' + game_id);
    }

    init();
});