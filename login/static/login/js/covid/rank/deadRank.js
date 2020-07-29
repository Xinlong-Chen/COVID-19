$(document).ready(function () {
    DeadUp2Down();
});

//大到小
$("a[id='deadDown']").click(function () {
    DeadUp2Down();
});

//小到大
$("a[id='deadUp']").click(function () {
    DeadDown2Up()
});


function DeadDown2Up() {
    $("#flag").val(0);
    DeadAjaxOpt();
}

function DeadUp2Down() {
    $("#flag").val(1);
    DeadAjaxOpt();
}

function DeadAjaxOpt() {
    $.ajax({
        url: "/data/api/deadrank/",
        type: "POST",
        data: $("#hidden_form").serialize(),
        success: function (data) {
            console.log(data);
            countryList = [];
            deadList = [];
            ansMap = new Map();
            $.each(data, function (index, dict) {
                deadList.push(dict.deadrate);
                countryList.push(dict.name);
            });
            ansMap.set("dead", deadList);
            ansMap.set("country", countryList);

            showDeadRank("deadrank-bar", ansMap)
            // console.log(confirmList);
            // console.log(countryList);
        }
    });
}

function showDeadRank(container, ansMap) {

    countryList = ansMap.get("country");
    deadList = ansMap.get("dead");

    countryList = countryList.reverse();
    deadList = deadList.reverse();

    console.log(deadList);
    maxn = Math.max.apply(null, deadList);
    minn = Math.min.apply(null, deadList);

    title = ['score', 'product'];
    data = [title];
    for (i = 0; i < countryList.length; i++) {
        tmp = [];
        deadList[i] = Math.floor(deadList[i] * 10000 + 0.5) / 100;
        tmp.push(deadList[i]);
        tmp.push(countryList[i]);
        data.push(tmp);
    }


    var dom = document.getElementById(container);
    var myChart = echarts.init(dom,"theme");
    var app = {};
    option = null;
    option = {
        tooltip: {
            trigger: 'axis',
            formatter: function (params) {
                var relVal = params[0].name;
                for (var i = 0, l = params.length; i < l; i++) {
                    console.log(params[i]);
                    relVal += " " + params[i].data[0] + '%'
                }
                return relVal;
            }
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        dataset: {
            source: data
        },
        grid: {containLabel: true},
        xAxis: {
            type: 'value',
            axisLabel: {
                show: true,
                interval: 'auto',
                formatter: '{value}%'
            },
            show: true
        },
        yAxis: {type: 'category'},
        visualMap: {
            show: false,
            orient: 'horizontal',
            left: 'center',
            min: minn + 0.001,
            max: maxn + 0.001,
            dimension: 0,
            inRange: {
                color: ['#125ebc', '#8a8c90']
            }
        },
        series: [
            {
                type: 'bar',
                encode: {
                    // Map the "amount" column to X axis.
                    x: 'score',
                    // Map the "product" column to Y axis
                    y: 'product'
                }
            }
        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}