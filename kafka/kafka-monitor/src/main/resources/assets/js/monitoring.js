


var app = angular.module("kafka",['ngAnimate', 'ui.bootstrap']);

app.controller("clusterCtr",function($scope,$http,$uibModal){
    $http.get("/api/cluster").then(function(response) {
        $scope.clusters = response.data.map(function(d){return d.name;})
    });
});

app.controller('ModalInstanceCtrl', function ($scope, $uibModalInstance, items) {

    $scope.items = items;
    $scope.selected = {
        item: $scope.items[0]
    };

    $scope.ok = function () {
        $uibModalInstance.close($scope.selected.item);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };
});

app.controller("groupCtr",function($scope,$http) {
    var url = "/api/consumer?cluster=" + $scope.cluster;
    $http.get(url).then(function(response){
        $scope.groups = response.data;
    });
});

app.controller("topicCtr",function($scope,$http) {
    var url = "/api/status?cluster=" + $scope.cluster +"&group="+$scope.group;
    $http.get(url).then(function(response) {
        console.log(response.data);
        $scope.records = response.data;
        $scope.topics = jQuery.unique($scope.records.map(function(r){return r.topic;}));
    });
});
