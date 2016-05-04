

var app = angular.module("kafka",['ngAnimate', 'ui.bootstrap']);
app.controller("clusterCtr",function($scope,$http){
    $http.get("get_clusters.php").then(function(response) {
        $scope.clusters = response.data.
        filter(function(d){return d.Database.startsWith('kafka_');}).
        map(function(d) { return d.Database.substring(6);});

    });
});

app.controller("groupCtr",function($scope,$http) {
    var url = "get_groups.php?cluster=" + $scope.cluster;
    $http.get(url).then(function(response){
        var values = $.map(response.data,function(k){ return k[Object.keys(k)]; });
        $scope.groups = values;
    });
});

app.controller("topicCtr",function($scope,$http) {
    var url = "get_offsets.php?cluster=" + $scope.cluster +"&group="+$scope.group+"&period=2";
    $http.get(url).then(function(response) {
        $scope.records = response.data;
        $scope.topics = jQuery.unique($scope.records.map(function(r){return r.topic;}));
    });
});
