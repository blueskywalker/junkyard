
"use strict";

var app = angular.module("cluster",['ui.bootstrap']);


app.controller('infoCtr', function ($window,$scope,$http) {
   $http.get("/api/cluster").then(function(response) {
        $scope.clusterInfo=response.data;
   });

   $scope.removeItem = function (item) {
        var list = [];
        $.each($scope.clusterInfo,function (k,v) {
            if (v.name != item.name) {
                list.push(v);
            }
        });
        $scope.clusterInfo = list;
   }

   $scope.addItem = function (item) {
        if (item.name.length==0 || item.zookeeper.length==0) {
            alert("Invalid Input");
            return;
        }
        $scope.clusterInfo.push(item);
        $scope.record= {}
   }

   $scope.ok = function() {
        console.log($scope.clusterInfo);
        $http.post("/api/cluster",$scope.clusterInfo).then(function() {
            $window.alert("successfully saved")
        });
   }

   $scope.cancel = function() {
        $window.location.href="/index.html";
   }
});