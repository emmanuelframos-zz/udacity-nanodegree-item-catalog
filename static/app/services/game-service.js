angular.module('e-sports').service('GameService', function($http){
    var self = this;

    self.getGames = function(){
        return $http.get('http://localhost:5000/game/all');
    }

    self.getGame = function(game_id){
        return $http.get('http://localhost:5000/game/' + game_id);
    }

    self.saveGame = function(game){
        return $http.post('http://localhost:5000/game/create', game);
    }

    self.updateGame = function(game){
        return $http.put('http://localhost:5000/game/update', game);
    }

    self.deleteGame = function(game_id){
        return $http.delete('http://localhost:5000/game/remove/' + game_id);
    }
});