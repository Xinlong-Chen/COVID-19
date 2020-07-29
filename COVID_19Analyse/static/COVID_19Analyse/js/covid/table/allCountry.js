$(document).ready(function () {
    $.ajax({
        url: "/data/api/today/",
        type: "POST",
        success: function (data) {
            console.log(data);
            str="";
            $.each(data,function (index,dict) {
                str+="<tr>"+
                    "<td>"+dict.name+"</td>"+
                    "<td>"+dict.continent+"</td>"+
                    "<td>"+dict.confirmAdd+"</td>"+
                    "<td>"+dict.confirm+"</td>"+
                    "<td>"+dict.dead+"</td>"+
                    "<td>"+dict.heal+"</td>";
                if(dict.details==true) {
                    str += "<td><a href='/data/details/" + dict.name + "'>详情</a></a></td>";
                }else {
                    str+="<td></td>"
                }
                str+="</tr>"
            });
            console.log(str);
            $("#countryTableBody").html(str);
            $('#countryTable').dataTable({
                "iDisplayLength": 5,
                "lengthMenu": [[5, 10, 25,50, 100],[5, 10, 25,50, 100]],
                "paging":true,
                "language": {'sSearch': '数据筛选:',
                    "lengthMenu": "每页显示 _MENU_ 项记录",
                    "zeroRecords": "没有符合项件的数据...",
                    "info": "当前页数 _PAGE_ ，共有 _PAGES_页",
                    "infoEmpty": "显示 0 至 0 共 0 项",
                    "infoFiltered": "  (由 _MAX_ 项结果过滤)"
                },
                "order": [[ 3, "desc"]]
            });
            $(document).ready(function () {
                $('#countryTable').DataTable();
            });

        }
    });
});
