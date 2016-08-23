"use strick";

var app = angular.module("KafkaChart", ['ui.grid']);


function makeDBName(cluster) {
    return 'kafka_' + cluster;
}

function parseQuery(search) {
    var args = search.substring(1).split('&');
    var argsParsed = {};
    var i, arg, kvp, key, value;
    for (i=0; i < args.length; i++) {
        arg = args[i];
        if (-1 === arg.indexOf('=')) {
            argsParsed[decodeURIComponent(arg).trim()] = true;
        }
        else {
            kvp = arg.split('=');
            key = decodeURIComponent(kvp[0]).trim();
            value = decodeURIComponent(kvp[1]).trim();
            argsParsed[key] = value;
        }
    }
    return argsParsed;
}

function perf(delta,time) {
    var num = (delta/(time/1000)).toFixed(2);
    return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
}

app.controller("source",function($scope,$window) {
    $scope.params= parseQuery($window.location.search);

    $scope.cluster = $scope.params.cluster;
    $scope.group = $scope.params.group;
    $scope.topic = $scope.params.topic;
});

app.controller("data",function($scope,$http) {
    var ranges = [ { text : "15 min", value : 900 },
                   { text : "30 min", value : 1800 },
                   { text : "1 hour", value : 3600 },
                   { text : "3 hours", value : 10800 },
                   { text : "6 hours", value : 21600 },
                   { text : "12 hours", value : 43200 },
                   { text : " 1 day", value: 86400 },
                   { text : " 3 days", value: 259200 },
                   { text : " 1 week", value: 604800 }
                 ];

    $scope.ranges = ranges;
    $scope.period= $scope.ranges[0].value;


    $scope.draw = function() {
        $('#container').highcharts({
            chart: {
                type:'spline'
            }
            , title: {
                text: 'KAFKA OFFSET'
            }
            , xAxis: [{
                type: 'datetime'
            }]
            , yAxis:[ {
                title: {
                    text: 'message size'
                },

            },{
                gridLineWidth: 0,
                title: {
                    text: 'lag'
                },
                opposite : true
            }],

            plotOptions: {
                spline: {
                    marker: {
                        enabled: false
                    }
                }
            },
            series: [
                {
                    name: 'logsize'
                    , data: $scope.logsize

                }
                , {
                    name: 'offset',
                    data: $scope.offset

                }, {
                    name: 'lag'
                    , data: $scope.lag
                    , yAxis : 1

                }]
        });
    }

    $scope.change = function() {

        var url = "/api/timeseries?cluster="+ $scope.cluster +
            "&group=" + $scope.group + "&topic=" + $scope.topic +
            "&period=" + $scope.period;

        $http.get(url).then(function(response){

            $scope.offsetData = response.data;
            $scope.gridOptions = {  data: 'offsetData'};

            logsize=[];
            offset=[];
            lag=[];

            response.data.forEach(function(r) {
                logsize.push([r.timestamp * 1000,Number(r.logsize)]);
                offset.push([r.timestamp * 1000,Number(r.offset)]);
                lag.push([r.timestamp * 1000,Number(r.lag)]);
            });
            $scope.logsize=logsize;
            $scope.offset=offset;
            $scope.lag=lag;

            var deltaTime = logsize[logsize.length-1][0]-logsize[0][0];
            var deltaMessage = logsize[logsize.length-1][1]-logsize[0][1];

            $scope.producer = perf(deltaMessage,deltaTime);

            deltaTime = offset[logsize.length-1][0]-offset[0][0];
            deltaMessage = offset[logsize.length-1][1]-offset[0][1];
            $scope.consumer = perf(deltaMessage,deltaTime);

            $scope.draw();
        });

    }

    $scope.change();
});
