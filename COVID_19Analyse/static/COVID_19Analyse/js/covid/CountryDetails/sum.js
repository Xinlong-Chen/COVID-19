function getsum(country) {
    $.ajax({
        url: "/data/api/sumdetails/",
        type: "GET",
        data:"country="+country,
        success: function (data) {
            // console.log(data);
            $("#nowConfirmAdd").html(change(data.nowConfirmCompare));
            $("#healAdd").html(change(data.healCompare));
            $("#confirmAdd").html(change(data.confirmCompare));
            $("#deadAdd").html(change(data.deadCompare));
            $("#nowConfirm").html(data.nowConfirm);
            $("#confirm").html(data.confirm);
            $("#heal").html(data.heal);
            $("#dead").html(data.dead);
        }
    });
}

function change(value) {
    if (value >= 0) {
        value = "+" + (value);
    }
    return value;
}