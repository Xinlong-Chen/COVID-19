$(document).ready(function () {
    $.ajax({
        url: "/data/api/mainCountry/",
        type: "POST",
        success: function (data) {
            // console.log(data);
            ans = new Map();
            timeList = [];
            cnt = 0;
            $.each(data, function (country, value) {
                cnt++;
                array = [];
                $.each(value, function (elem, num) {
                    if (cnt <= 1) {
                        timeList.push(num.date);
                    }
                    array.push(num.confirm);
                });
                ans.set(country, array);
            });
            try {
                showMainCountryLine("mainCountryChart", timeList, ans);
            }
            catch (e) {

            }
            try {
                showMainCountryTable("MainCountrytableBody", timeList, ans);
            }
            catch (e) {
                
            }
        }
    });
});

function showMainCountryTable(container,time,valueMap) {
    console.log(valueMap);
    table = $("#"+container);
    time=  time.reverse();
    str="";
    a = valueMap.get("意大利").reverse();
    b = valueMap.get("西班牙").reverse();
    c = valueMap.get("德国").reverse();
    d = valueMap.get("英国").reverse();
    e = valueMap.get("法国").reverse();
    f = valueMap.get("美国").reverse();
    console.log(a);
    console.log(b);
    for (i=0;i<49;i+=7){

        args = time[i].split("-");
        tmp = (args[1] + "-" + args[2]);
        str+="<tr>" +
            "<td>"+tmp+"</td>"+
            "<td>"+a[i]+"</td>"+
            "<td>"+b[i]+"</td>"+
            "<td>"+c[i]+"</td>"+
            "<td>"+d[i]+"</td>" +
            "<td>"+e[i]+"</td>"+
            "<td>"+f[i]+"</td>"+
            "</tr>";
    }
    table.html(str);
}
function showMainCountryLine(container, time, valueMap) {
    timeTmp = time.reverse();
    time = [];
    for (i = 0; i < timeTmp.length; i++) {
        args = timeTmp[i].split("-");
        time.push(args[1] + "-" + args[2])
    }
    a = valueMap.get("意大利").reverse();
    b = valueMap.get("巴西").reverse();
    c = valueMap.get("西班牙").reverse();
    d = valueMap.get("德国").reverse();
    e = valueMap.get("英国").reverse();
    f = valueMap.get("法国").reverse();
    g = valueMap.get("美国").reverse();
    h = valueMap.get("俄罗斯").reverse();


    var dom = document.getElementById(container);
    var myChart = echarts.init(dom, 'theme');
    var app = {};
    option = null;
    option = {
        tooltip: {
            trigger: 'axis'
        },
        legend: [{
            data: ['意大利', '巴西', '西班牙', '德国',],
            icon: "roundRect",
            x:'center',
            y:'0%'
        },{
            data: ['英国', '法国', '美国', '俄罗斯',],
            icon: "roundRect",
            x:'center',
            y:'7%'
        }],
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
            boundaryGap: true,
            //x 轴
            data: time,
            axisLabel: {
                interval: 6,
                rotate: 35
            }
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                show: true,
                interval: 'auto',
                formatter: '{value}'
            },
            show: true
        },
        series: [
            {
                name: "意大利",
                type: 'line',
                data: a,
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
                name: '巴西',
                type: 'line',
                data: b,
                itemStyle: {
                    normal: {
                        color: '#ff6f73', //改变折线点的颜色
                        lineStyle: {
                            color: '#ff6f73' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: '西班牙',
                type: 'line',
                data: c,
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
                name: '德国',
                type: 'line',
                data: d,
                itemStyle: {
                    normal: {
                        color: '#ffda42', //改变折线点的颜色
                        lineStyle: {
                            color: '#ffda42' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: '英国',
                type: 'line',
                data: e,
                itemStyle: {
                    normal: {
                        color: '#db63c2', //改变折线点的颜色
                        lineStyle: {
                            color: '#db63c2' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: '法国',
                type: 'line',
                data: f,
                itemStyle: {
                    normal: {
                        color: '#8763f3', //改变折线点的颜色
                        lineStyle: {
                            color: '#8763f3' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: '美国',
                type: 'line',
                data: g,
                itemStyle: {
                    normal: {
                        color: '#5087ff', //改变折线点的颜色
                        lineStyle: {
                            color: '#5087ff' //改变折线颜色
                        }
                    }
                },
            },
            {
                name: '俄罗斯',
                type: 'line',
                data: h,
                itemStyle: {
                    normal: {
                        color: '#47b8ff', //改变折线点的颜色
                        lineStyle: {
                            color: '#47b8ff' //改变折线颜色
                        }
                    }
                },
            }
        ]
    };
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}