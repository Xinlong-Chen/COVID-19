$(document).ready(function () {
    HealUp2Down();
});

//大到小
$("a[id='healDown']").click(function () {
    HealUp2Down();
});

//小到大
$("a[id='healUp']").click(function () {
    HealDown2Up()
});


function HealDown2Up() {
    $("#flag").val(0);
    healAjaxOpt();
}

function HealUp2Down() {
    $("#flag").val(1);
    healAjaxOpt();
}

function healAjaxOpt() {
    $.ajax({
        url: "/data/api/healrank/",
        type: "POST",
        data: $("#hidden_form").serialize(),
        success: function (data) {
            console.log(data);
            countryList = [];
            healList = [];
            ansMap = new Map();
            $.each(data, function (index, dict) {
                healList.push(dict.healrate);
                countryList.push(dict.name);
            });
            ansMap.set("heal", healList);
            ansMap.set("country", countryList);

            showHealRank("healrank-bar", ansMap)
            // console.log(confirmList);
            // console.log(countryList);
        }
    });

}

function showHealRank(container, ansMap) {

    countryList = ansMap.get("country");
    healList = ansMap.get("heal");

    countryList = countryList.reverse();
    healList = healList.reverse();

    maxn = Math.max.apply(null, healList);
    minn = Math.min.apply(null, healList);

    title = ['score', 'product'];
    data = [title];
    for (i = 0; i < countryList.length; i++) {
        tmp = [];
        healList[i] = Math.floor(healList[i] * 10000 + 0.5) / 100;
        tmp.push(healList[i]);
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
            min: minn,
            max: maxn,
            dimension: 0,
            inRange: {
                color: ['#31de00', '#00952c']
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