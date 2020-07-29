$(document).ready(function () {
    $.ajax({
        url: "/data/api/oversea/",
        type: "POST",
        success: function (data) {
            console.log(data);
            table = $("#OverseaWeektableBody");
            str = "";
            $.each(data,function (index,dict) {
                args = dict.date.split("-");
                dateTmp = args[1] + "-" + args[2];
                str+="<tr><td>"+dateTmp+"</td><td>"+dict.confirm+"</td><td>"+dict.rate*100+"%</td>"
            });
            table.html(str);
        }
    });
});
