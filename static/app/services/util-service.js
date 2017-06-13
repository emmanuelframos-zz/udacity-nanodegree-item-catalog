angular.module('e-sports').service('UtilService', function(){
    var self = this;

    self.MMDDYYYYtoDate = function(mmddyyyy){
        array = mmddyyyy.split('-');
        return new Date(array[2], array[0], array[1]);
    }

});