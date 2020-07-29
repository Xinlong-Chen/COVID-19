$(document).ready(function () {
    $.ajax({
        url: "/data/api/plc/",
        type: "POST",
        success: function (data) {
            // console.log(data);
            ans = new Map();
            $.each(data, function (country, value) {
                timeList = [];
                array = [];
                $.each(value, function (time, num) {
                    timeList.push(time);
                    array.push(num);
                });
                ans.set(country, array);
            });
            showLCConfirm("plcChartBar", timeList, ans);
        }
    });
});

function showLCConfirm(container, time, ans) {
    timeTmp = time.reverse();
    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2])
    }

    a = ans.get("印度").reverse();
    b = ans.get("印度尼西亚").reverse();
    c = ans.get("巴西").reverse();
    d = ans.get("俄罗斯").reverse();

    arate = [];
    brate = [];
    crate = [];
    drate = [];
    for (i = 1; i < time.length; i++) {
        arate.push(Math.floor((a[i] - a[i - 1]) / a[i - 1] * 10000 + 0.5) / 100);
        brate.push(Math.floor((b[i] - b[i - 1]) / b[i - 1] * 10000 + 0.5) / 100);
        crate.push(Math.floor((c[i] - c[i - 1]) / c[i - 1] * 10000 + 0.5) / 100);
        drate.push(Math.floor((d[i] - d[i - 1]) / d[i - 1] * 10000 + 0.5) / 100);
    }

    time = time.slice(1);

    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, "theme");
    var app = {};
    option = null;
    var posList = [
        'left', 'right', 'top', 'bottom',
        'inside',
        'insideTop', 'insideLeft', 'insideRight', 'insideBottom',
        'insideTopLeft', 'insideTopRight', 'insideBottomLeft', 'insideBottomRight'
    ];

    app.configParameters = {
        rotate: {
            min: -90,
            max: 90
        },
        align: {
            options: {
                left: 'left',
                center: 'center',
                right: 'right'
            }
        },
        verticalAlign: {
            options: {
                top: 'top',
                middle: 'middle',
                bottom: 'bottom'
            }
        },
        position: {
            options: echarts.util.reduce(posList, function (map, pos) {
                map[pos] = pos;
                return map;
            }, {})
        },
        distance: {
            min: 0,
            max: 100
        }
    };

    app.config = {
        rotate: 90,
        align: 'left',
        verticalAlign: 'middle',
        position: 'insideBottom',
        distance: 15,
        onChange: function () {
            var labelOption = {
                normal: {
                    rotate: app.config.rotate,
                    align: app.config.align,
                    verticalAlign: app.config.verticalAlign,
                    position: app.config.position,
                    distance: app.config.distance
                }
            };
            myChart.setOption({
                series: [{
                    label: labelOption
                }, {
                    label: labelOption
                }, {
                    label: labelOption
                }, {
                    label: labelOption
                }]
            });
        }
    };


    var labelOption = {
        show: false,
    };

    option = {
        color: ['#ffce3d', '#ff1d21', '#8663f2', '#9cccff'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            },
            formatter: function (params) {
                var relVal = params[0].name;
                for (var i = 0, l = params.length; i < l; i++) {
                    relVal += '<br/>' + params[i].marker + params[i].seriesName + ' : ' + params[i].value + '%'
                }
                return relVal;
            }

        },
        legend: {
            data: ['印度', '印尼', '巴西', '俄罗斯']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: time,
                axisLabel: {
                    interval: 0,
                    rotate: 35
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                axisLabel: {
                    show: true,
                    interval: 'auto',
                    formatter: '{value}%'
                },
                show: true,
            }
        ],
        series: [
            {
                name: '印度',
                type: 'bar',
                barGap: 0,
                label: labelOption,
                data: arate
            },
            {
                name: '印尼',
                type: 'bar',
                label: labelOption,
                data: brate
            },
            {
                name: '巴西',
                type: 'bar',
                label: labelOption,
                data: crate
            },
            {
                name: '俄罗斯',
                type: 'bar',
                label: labelOption,
                data: drate
            }
        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}