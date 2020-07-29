$(document).ready(function () {
    $.ajax({
        url: "/data/api/trend/",
        type: "POST",
        success: function (data) {
            // console.log(data);
            confirmList = [];
            addList = [];
            healrateList = [];
            deadrateList = [];
            dateList = [];
            nowList = [];
            $.each(data, function (index, dict) {
                confirmList.push(dict.confirm);
                nowList.push(dict.confirm_now);
                addList.push(dict.confirm_add);
                healrateList.push(dict.healrate);
                deadrateList.push(dict.deadrate);
                dateList.push(dict.date);
            });
            ansMap = new Map();
            ansMap.set("confirm", confirmList);
            ansMap.set("add", addList);
            ansMap.set("now", nowList);
            ansMap.set("heal", healrateList);
            ansMap.set("dead", deadrateList);
            ansMap.set("time", dateList);
            showOverseaConfirmAddLine("overseaConfirmAddLine", ansMap);
            showConfirmLine("overseaConfirmLine", ansMap);
            showHealDeadLine("heal-Dead-Rate-Line", ansMap);
        }
    });
});

function showOverseaConfirmAddLine(container, ansMap) {
    timeTmp = ansMap.get("time");
    addList = ansMap.get("add");

    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2])
    }

    time = time.reverse();
    addList = addList.reverse();
    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, 'theme');
    var app = {};
    option = null;
    option = {
        tooltip: {
            trigger: 'axis'

        },
        legend: {
            data: ['新增确诊',],
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
                interval: 15,
                rotate: 35
            }
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                show: true,
                interval: 'auto'
            },
            show: true
        },
        series: [
            {
                name: "新增确诊",
                type: 'line',
                data: addList
            },

        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}

function showConfirmLine(container, ansMap) {
    timeTmp = ansMap.get("time");
    nowList = ansMap.get("now");
    confirmList = ansMap.get("confirm");

    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2])
    }

    time = time.reverse();
    nowList = nowList.reverse();
    confirmList = confirmList.reverse();

    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, 'theme');
    var app = {};
    option = null;
    option = {
        tooltip: {
            trigger: 'axis'

        },
        legend: {
            data: ['现有确诊', "累计确诊"],
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
                interval: 15,
                rotate: 35
            }
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                show: true,
                interval: 'auto'
            },
            show: true
        },
        series: [
            {
                name: "现有确诊",
                type: 'line',
                data: nowList,
                itemStyle: {
                    normal: {
                        color: '#ffa438', //改变折线点的颜色
                        lineStyle: {
                            color: '#ffa438' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: "累计确诊",
                type: 'line',
                data: confirmList,
                itemStyle: {
                    normal: {
                        color: '#a80000', //改变折线点的颜色
                        lineStyle: {
                            color: '#a80000' //改变折线颜色
                        }
                    }
                },
            },
        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}

function showHealDeadLine(container, ansMap) {
    timeTmp = ansMap.get("time");
    heal = ansMap.get("heal");
    dead = ansMap.get("dead");

    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2]);
        heal[i] = Math.floor(heal[i] * 10000 + 0.5) / 100;
        dead[i] = Math.floor(dead[i] * 10000 + 0.5) / 100;
    }

    time = time.reverse();
    heal = heal.reverse();
    dead = dead.reverse();

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
            data: ['治愈率', "病死率"],
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
                interval: 15,
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
                name: "治愈率",
                type: 'line',
                data: heal,
                itemStyle: {
                    normal: {
                        color: '#9de362', //改变折线点的颜色
                        lineStyle: {
                            color: '#9de362' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: "病死率",
                type: 'line',
                data: dead,
                itemStyle: {
                    normal: {
                        color: '#5a5b6a', //改变折线点的颜色
                        lineStyle: {
                            color: '#5a5b6a' //改变折线颜色
                        }
                    }
                },
            },
        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

}