
$(document).ready(function () {

    var table = $('#feature-req-table').DataTable({
        "ajax": {
            "url": "/api/feature-requests",
            "dataSrc": function (json) {
                var return_data = new Array();
                for (var i = 0; i< json.length; i++) {
                     return_data.push([
                        json[i].id,
                        json[i].title,
                        json[i].description,
                        json[i].client,
                        json[i].priority,
                        json[i].product_area,
                        moment(json[i].target_date).format('MMM Do YYYY'),
                        '<span><a class="btn btn-warning btn-xs" href="/feature-requests/edit/' + json[i].id  + '"><i class="fa fa-pencil"></i></a></span> ' +
                        '<span><a class="btn btn-danger btn-xs deleteLink" data-payload="'+ json[i].id+'"><i class="fa fa-trash"></i></a></span>'
                    ])
              }
              return return_data;
            }
        }
    });

    $(document).on('click', '.deleteLink', function () {

        var id = $(this).data("payload");

        $.ajax({
            type: 'DELETE',
            dataType: "text/plain",
            url: 'api/feature-requests/' + id,
            success: function (data, status) {
                $("#deleteAlertMesage>span").text(id)
                $("#deleteAlertMesage").show();
                table.ajax.reload();
            }
        })
    })

    $("#deleteAlertMesage").hide();


    var form = $( "#addFeatureRequestForm");
    form.validate();

    $('.date-picker').datepicker({
        format: 'yyyy-mm-dd',
        startDate: '1d'
    });

    $("#addClient").hide();
    $("#addProductArea").hide();
    $("#addStatusMessage").hide();

    form.submit(function(e) {
        e.preventDefault();
        if(form.valid()) {

            var formData = $('form').serialize();

            $("#addFeatureRequestForm :input").prop("disabled", true);
            $.ajax({
                type : 'POST',
                url : '/api/feature-requests',
                data  : formData,
                dataType : 'json',
                encode : true,
                success : function (data) {
                    $("#addFeatureRequestForm :input").prop("disabled", false);
                    $("#addFeatureRequestForm :input").val("")
                    $("#FqId").text(data.id);
                    $("#addStatusMessage").show();
                    setTimeout(function () {
                        window.location = "/";
                    }, 3000)
                }
            })
        }
    })


    $("#showClientInbut").change(function () {
        var isAddClientChecked = $('#showClientInbut').is(':checked');

       if (isAddClientChecked) {
            $("#showClient").hide();
            $("#showClient :input").val("");
            $("#addClient").show();
       }
       else {
            $("#showClient").show();
            $("#addClient").hide();
            $("#addClient :input").val("");
       }
    })

    $("#showProductAreaInbut").change(function () {
        var isAddPAChecked = $('#showProductAreaInbut').is(':checked');

       if (isAddPAChecked) {
            $("#showProductArea").hide();
            $("#showProductArea :input").val("");
            $("#addProductArea").show();
       }
       else {
            $("#showProductArea").show();
            $("#addProductArea").hide();
            $("#addProductArea :input").val("");
       }
    })

    var dateValue = $("#editTargetDate").val();
    dateValue = moment(dateValue).format('YYYY-MM-DD');

    $("#editTargetDate").val(dateValue);

    var updateForm = $("#updateFeatureRequestForm");
    updateForm.validate();

    updateForm.submit(function(e) {
        e.preventDefault();
        if(updateForm.valid()) {

            var formData = $("form").serialize();
            var id = $('form').data("id");

            $("#updateFeatureRequestForm :input").prop("disabled", true);
            $.ajax({
                type : 'PUT',
                url : '/api/feature-requests/' + id,
                data  : formData,
                dataType : 'json',
                encode : true,
                success : function (data) {
                    $("#updateFeatureRequestForm :input").prop("disabled", false);
                    $("#FqId").text(data.id);
                    $("#addStatusMessage").show();
                }
            })
        }
    })
});