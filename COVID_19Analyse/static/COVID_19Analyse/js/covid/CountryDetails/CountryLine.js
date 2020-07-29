function getdetails(country) {
    // console.log(country);
    $.ajax({
        url: "/data/api/details/",
        type: "GET",
        data:"country="+country,
        success: function (data) {
            // console.log(data);
            confirmList = [];
            addList = [];
            heal = [];
            dead = [];
            dateList = [];
            $.each(data, function (index, dict) {
                confirmList.push(dict.confirm);
                addList.push(dict.confirm_add);
                heal.push(dict.heal);
                dead.push(dict.dead);
                dateList.push(dict.date);
            });
            ansMap = new Map();
            ansMap.set("confirm", confirmList);
            ansMap.set("add", addList);
            ansMap.set("heal", heal);
            ansMap.set("dead", dead);
            ansMap.set("time", dateList);
            showConfirmAddLine("CountryAddLine", ansMap);
            showConfirmHealDeadLine("CountryLine2", ansMap);
        }
    });
}


function showConfirmAddLine(container, ansMap) {
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


function showConfirmHealDeadLine(container, ansMap) {
    timeTmp = ansMap.get("time");
    confirmList = ansMap.get("confirm");
    HealList = ansMap.get("heal");
    deadList = ansMap.get("dead");
    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2])
    }

    time = time.reverse();
    HealList = HealList.reverse();
    confirmList = confirmList.reverse();
    deadList = deadList.reverse();

    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, 'theme');
    var app = {};
    option = null;
    option = {
        tooltip: {
            trigger: 'axis'

        },
        legend: {
            data: ['累计确诊', "累计治愈", "累计死亡"],
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
            {
                name: "累计治愈",
                type: 'line',
                data: HealList,
                itemStyle: {
                    normal: {
                        color: '#2dff85', //改变折线点的颜色
                        lineStyle: {
                            color: '#2dff85' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: "累计死亡",
                type: 'line',
                data: deadList,
                itemStyle: {
                    normal: {
                        color: '#0f0f0f', //改变折线点的颜色
                        lineStyle: {
                            color: '#0f0f0f' //改变折线颜色
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