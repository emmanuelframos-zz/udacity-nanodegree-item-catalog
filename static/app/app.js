var app = angular.module('e-sports', ['ngRoute', 'angular-loading-bar']);

app.controller('AppController', function ($location) {
    var vm = this;  

    vm.user = window.localStorage.user; 

    function init(){              
        if (window.localStorage.auth_token){
            if (window.href){
                $location.path(window.href);
            }else{
                $location.path("/gameList");
            }
        }else{
            $location.path('/signIn');
        }
    }    

    vm.logout = function () {      
        if (window.localStorage.auth_provider == 'facebook'){
            facebookSignOut();
        }
        
        if (window.localStorage.auth_provider == 'google'){
            googleSignOut();          
        }
    }

    init();

});

app.config(function($routeProvider, $httpProvider){
    $httpProvider.interceptors.push('Interceptor');     

    $routeProvider      
        .when("/signIn", {           
            templateUrl : "/static/app/pages/login.html",
        })
        .when("/gameForm", {
            templateUrl : "/static/app/pages/gameForm.html",
        })
        .when("/gameList", {
            templateUrl : "/static/app/pages/gameList.html",
        })
        .when("/gameForm/:game_id", {
            templateUrl : "/static/app/pages/gameForm.html",
        })
        .when("/characterForm", {
            templateUrl : "/static/app/pages/characterForm.html",
        })
        .when("/characterList", {
            templateUrl : "/static/app/pages/characterList.html",
        })
        .when("/characterForm/:character_id", {
            templateUrl : "/static/app/pages/characterForm.html",
        });
});

app.factory('Interceptor', function Interceptor($q) {
  return {
    request: function(config) {
      config.headers["auth_token"] = window.localStorage.auth_token;
      config.headers["auth_provider"] = window.localStorage.auth_provider;
      return config;
    },

    requestError: function(config) {
      return config;
    },

    response: function(res) {
      return res;
    },

    responseError: function(res) {
      window.localStorage.clear();
      window.location.href = "/#/signIn";        
      return $q.reject(res);      
    }
  }
});