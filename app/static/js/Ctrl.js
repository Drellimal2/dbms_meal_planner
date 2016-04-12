var app = angular.module("MealPlanner",['ngRoute','ui.bootstrap']);

angular.module('MealPlanner').factory('Service',['$http','$q',function($http,$q){
    return{
        getUsers : function(){
            var deferred = $q.defer();
            $http.get('/users')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getRecipes : function(){
            var deferred = $q.defer();
            $http.get('/recipes')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getIngredients : function(){
            var deferred = $q.defer();
            $http.get('/ingredients')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getMeasurments : function(){
            var deferred = $q.defer();
            $http.get('/measurements')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        }
    }
}]);

angular.module('MealPlanner').controller('Ctrl',['$scope',function($scope){

}]);
