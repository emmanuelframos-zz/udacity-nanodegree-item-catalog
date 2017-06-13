angular.module('e-sports').service('CharacterService', function($http){
    var self = this;

    self.getCharacters = function(){
        return $http.get('http://localhost:5000/character/all');
    }

    self.getCharacter = function(character_id){
        return $http.get('http://localhost:5000/character/' + character_id);
    }

    self.filterCharacters = function(gameId){
        return $http.get('http://localhost:5000/game/'+ gameId +'/character/all');
    }

    self.saveCharacter = function(character){
        return $http.post('http://localhost:5000/character/create', character);
    }

    self.updateCharacter = function(character){
        return $http.put('http://localhost:5000/character/update', character);
    }

    self.deleteCharacter = function(character_id){
        return $http.delete('http://localhost:5000/character/remove/' + character_id);
    }

});