angular.module('e-sports').controller('CharacterController', function (CharacterService, UtilService, GameService, $location) {
    var vm = this;
    vm.games;
    vm.characters;
    vm.selectedGame;

    function init() {
        vm.getGames();
        vm.getCharacters();
    }

    vm.getGames = function(){
         GameService.getGames().then(function(success){
            vm.games = success.data.games;
         },function(error){
            console.error("Error on get games. " + error.statusText);
            UtilService.showSnackbar(document, error.statusText);
         });
    }

    vm.getCharacters = function () {
        CharacterService.getCharacters().then(function (success) {
            vm.characters = success.data.characters;
        }, function(error) {
            console.error("Error on get characters. " + error.statusText);
            UtilService.showSnackbar(document, error.statusText);
        });
    }

    vm.filterCharacters = function () {
        CharacterService.filterCharacters(vm.selectedGame.id).then(function (success) {
            vm.characters = success.data.characters;
        }, function (error) {
            console.error("Error on filter characters. " + error.statusText);
            UtilService.showSnackbar(document, error.statusText);
        });
    }

    vm.updateCharacter = function(character_id) {
        $location.path('/characterForm/' + character_id);
    }

    vm.clearFilter = function(){
        vm.getCharacters();
        vm.getGames();
    }

    init();

});