$(document).ready(function () {
    $.ajax({
        url: "/data/api/confirmrank/",
        type: "POST",
        success: function (data) {
            countryList = [];
            confirmList = [];
            ansMap = new Map();
            $.each(data, function (index, dict) {
                confirmList.push(dict.confirm_add);
                countryList.push(dict.name);
            });
            ansMap.set("confirm", confirmList);
            ansMap.set("country", countryList);

            showAddRank("confirmRankBar", ansMap);

        }
    });
});


function showAddRank(container, ansMap) {

    countryList = ansMap.get("country");
    confirmList = ansMap.get("confirm");

    countryList = countryList.reverse();
    confirmList = confirmList.reverse();

    maxn = Math.max.apply(null, confirmList);
    minn = Math.min.apply(null, confirmList);

    title = ['score', 'product'];
    data = [title];
    for (i = 0; i < countryList.length; i++) {
        tmp = [];
        tmp.push(confirmList[i]);
        tmp.push(countryList[i]);
        data.push(tmp);
    }


    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, "theme");
    var app = {};
    option = null;
    option = {
        tooltip: {
            trigger: 'axis',
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
            name: '',
            axisLabel: {
                interval: 6,
                rotate: 35
            }
        },
        yAxis: {type: 'category'},
        visualMap: {
            show: false,
            orient: 'horizontal',
            left: 'center',
            min: minn - 100,
            max: maxn + 100,
            dimension: 0,
            inRange: {
                color: ['#D7DA8B', '#E15457']
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