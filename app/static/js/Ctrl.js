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
        getMeasurements : function(){
            var deferred = $q.defer();
            $http.get('/measurements')
            .success(function(data){
                deferred.resolve(data);
            })
            .error(function(err){
                deferred.reject(err);
            });
            return deferred.promise;
        },
        getRestrictions : function(){
            var deferred = $q.defer();
            $http.get('/restrictions')
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

angular.module('MealPlanner').controller('IngredientCtrl',['$scope','Service',function($scope,Service){
    // Service.getIngredients().then(function(ingredients){
    //     $scope.ingredients = ingredients;
    // });
    // console.log($scope.ingredients);
    Service.getMeasurements().then(function(measurements){
        console.log(measurements);
        $scope.measurements = measurements;
    });

    $scope.fields = [{'id':'field1'}]
    $scope.addNewField = function(){
        var newField = $scope.fields.length+1;
        $scope.fields.push({'id':'field'+newField});
    };
    $scope.removelastField = function(){
        var selectField = $scope.fields.length-1;
        $scope.fields.splice(selectField);
    };
}]);

angular.module('MealPlanner').controller('RecipesCtrl',['$scope','Service',function($scope,Service){
    Service.getRecipes().then(function(recipes){
        $scope.recipes = recipes;
    })
}]);