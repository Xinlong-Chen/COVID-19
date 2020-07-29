$("a[name='continentData']").bind("click", function () {
    $("#datatype").val("continent");
    var input1 = $('<input>');
    input1.attr('type', 'hidden');
    input1.attr('name', 'datatype');
    input1.attr('value', $("#datatype").val());
    var input2 = $('<input>');
    input2.attr('type', 'hidden');
    input2.attr('name', 'country');
    input2.attr('value', $("#country").val());
    $.ajax({
        url: "/data/download/",
        type: "POST",
        data: $("#hidden_form").serialize(),
        success: function (response, status, request) {
            var disp = request.getResponseHeader('Content-Disposition');
            if (disp && disp.search('attachment') != -1) { //判断是否为文件
                var form = $('<form action="/data/download/" method="post"></form>');
                $('body').append(form);
                form.append(input1);
                form.append(input2);
                form.submit();
            }
        }
    })
});