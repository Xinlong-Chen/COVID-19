$(document).ready(function () {
    $.ajax({
        url: "/data/api/continent/",
        type: "POST",
        success: function (data) {
            // console.log(data);
            keyList = [];
            ans = new Map();
            $.each(data, function (key, value) {
                keyList.push(key);
                $.each(value, function (continent, num) {
                    if (!ans.has(continent)) {
                        ans.set(continent, []);
                    }
                    array = ans.get(continent);
                    array.push(num);
                    ans.set(continent, array);
                })
            });
            ans.delete("其他");
            try {
                showBar("continentBar", keyList, ans);
            }
            catch(err) {
            }
            try {
                showLine("continentLine", keyList, ans);
            }
            catch (e) {
            }
        }
    });
});

function showBar(container, time, valueMap) {
    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, "theme");
    var app = {};

    timeTmp = time.slice(0, 3).reverse();
    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2])
    }
    a = valueMap.get("亚洲").slice(0, 3).reverse();
    b = valueMap.get("欧洲").slice(0, 3).reverse();
    c = valueMap.get("北美洲").slice(0, 3).reverse();
    d = valueMap.get("南美洲").slice(0, 3).reverse();
    e = valueMap.get("非洲").slice(0, 3).reverse();
    f = valueMap.get("大洋洲").slice(0, 3).reverse();

    option = null;
    option = {
        angleAxis: {},
        radiusAxis: {
            type: 'category',
            data: time,
            z: 10,
            axisLabel: {
                interval: 0,
                rotate: 25
            }
        },
        tooltip: {
            trigger: 'axis'
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        polar: {},
        series: [{
            type: 'bar',
            data: a,
            coordinateSystem: 'polar',
            name: '亚洲',
            stack: 'a'
        }, {
            type: 'bar',
            data: b,
            coordinateSystem: 'polar',
            name: '欧洲',
            stack: 'a'
        }, {
            type: 'bar',
            data: c,
            coordinateSystem: 'polar',
            name: '北美洲',
            stack: 'a'
        }, {
            type: 'bar',
            data: d,
            coordinateSystem: 'polar',
            name: '南美洲',
            stack: 'a'
        }, {
            type: 'bar',
            data: e,
            coordinateSystem: 'polar',
            name: '非洲',
            stack: 'a'
        }, {
            type: 'bar',
            data: f,
            coordinateSystem: 'polar',
            name: '大洋洲',
            stack: 'a'
        }],
        legend: {
            orient: 'vertical',
            left: '85%',  //图例距离左的距离
            y: 'center',  //图例上下居中
            show: true,
            data: ['亚洲', '欧洲', '北美洲', '南美洲', '非洲', '大洋洲'],
        }
    };

    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}

function showLine(container, time, valueMap) {
    timeTmp = time.reverse();
    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2])
    }
    a = valueMap.get("亚洲").reverse();
    b = valueMap.get("欧洲").reverse();
    c = valueMap.get("北美洲").reverse();
    d = valueMap.get("南美洲").reverse();
    e = valueMap.get("非洲").reverse();
    f = valueMap.get("大洋洲").reverse();

    arate = [];
    brate = [];
    crate = [];
    drate = [];
    erate = [];
    frate = [];
    for (i = 1; i < time.length; i++) {
        arate.push(Math.floor((a[i] - a[i - 1]) / a[i - 1] * 10000 + 0.5) / 100);
        brate.push(Math.floor((b[i] - b[i - 1]) / b[i - 1] * 10000 + 0.5) / 100);
        crate.push(Math.floor((c[i] - c[i - 1]) / c[i - 1] * 10000 + 0.5) / 100);
        drate.push(Math.floor((d[i] - d[i - 1]) / d[i - 1] * 10000 + 0.5) / 100);
        erate.push(Math.floor((e[i] - e[i - 1]) / e[i - 1] * 10000 + 0.5) / 100);
        frate.push(Math.floor((f[i] - f[i - 1]) / f[i - 1] * 10000 + 0.5) / 100);
    }
    time = time.slice(1);

    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, 'theme');
    var app = {};
    option = null;
    option = {
        tooltip: {
            trigger: 'axis',
            formatter: function (params) {
                var relVal = params[0].name;
                for (var i = 0, l = params.length; i < l; i++) {
                    relVal += '<br/>' + params[i].marker + params[i].seriesName + ' : ' + params[i].value + '%'
                }
                return relVal;
            }

        },
        legend: {
            data: ['亚洲', '欧洲', '北美洲', '南美洲', '非洲', '大洋洲'],
            icon: "roundRect",
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            //x 轴
            data: time,
            axisLabel: {
                interval: 0,
                rotate: 35
            }
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                show: true,
                interval: 'auto',
                formatter: '{value}%'
            },
            show: true
        },
        series: [
            {
                name: "亚洲",
                type: 'line',
                data: arate
            },
            {
                name: '欧洲',
                type: 'line',
                data: brate
            },
            {
                name: '北美洲',
                type: 'line',
                data: crate
            },
            {
                name: '南美洲',
                type: 'line',
                data: drate
            },
            {
                name: '非洲',
                type: 'line',
                data: erate
            },
            {
                name: '大洋洲',
                type: 'line',
                data: frate
            }
        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}
