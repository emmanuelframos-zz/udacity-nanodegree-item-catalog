angular.module('e-sports').controller('CharacterEditController', ['CharacterService', 'GameService', 'UtilService', '$location','$routeParams',
function (CharacterService, GameService, UtilService, $location, $routeParams) {
    var vm = this;
    vm.games;
    vm.character;
    vm.isEdit;

    function init() {
       vm.getGames();

       var character_id = $routeParams.character_id;

       if (character_id){
            vm.getCharacter(character_id);
            vm.isEdit = true;
        }
    }

    vm.getGames = function(){
         GameService.getGames().then(function(success){
            vm.games = success.data.games;
         },function(error){
            console.error("Error on get games. " + error.statusText);
         });
    }

    vm.saveCharacter = function () {
        if (vm.isEdit){
           CharacterService.updateCharacter(vm.character).then(function (success) {
                vm.sendToCharacterList();
           }, function(error) {
                console.error("Error on update character. " + error.statusText);
           });
        }else{
           CharacterService.saveCharacter(vm.character).then(function (success) {
                vm.sendToCharacterList();
           }, function(error) {
                console.error("Error on save character. " + error.statusText);
           });
        }
    }

    vm.cancel = function () {
        vm.sendToCharacterList();
    }

    vm.deleteCharacter = function () {
        CharacterService.deleteCharacter(vm.character.id).then(function (success) {
            vm.sendToCharacterList();
        }, function (error) {
            console.error("Error on remove character. " + error.statusText);
        });
    }

    vm.getCharacter = function (character_id) {
        CharacterService.getCharacter(character_id).then(function (success) {
            vm.character = success.data;
            vm.character.release_date = UtilService.MMDDYYYYtoDate(vm.character.release_date);
        }, function (error) {
            console.error("Error on get character. " + error.statusText);
        });
    }

    vm.sendToCharacterList = function(){
        $location.path('/characterList');
    }

    init();

}]);