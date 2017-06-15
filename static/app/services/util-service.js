angular.module('e-sports').service('UtilService', function(){
    var self = this;

    self.MMDDYYYYtoDate = function(mmddyyyy){
        array = mmddyyyy.split('-');
        return new Date(array[2], array[0], array[1]);
    }

    self.showSnackbar = function(document, text){
        var snackbar = document.getElementById("snackbar")

        snackbar.textContent = text ? text : snackbar.textContent;
        snackbar.className = "show";

        setTimeout(function(){
            snackbar.className = snackbar.className.replace("show", "");
        },  3000);
    }
});