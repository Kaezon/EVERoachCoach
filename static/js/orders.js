var orderModal = $('#newOrderModal')
var orderForm =  $('#orderForm');
$( document ).ready(
    orderForm.submit(function() {
        $.ajax({
            type: orderForm.attr('method'),
            url: orderForm.attr('action'),
            data: orderForm.serialize(),
            success: function(data) {
                  orderModal.modal('hide')
                  location.reload()
            },
            error: function(data) {
                $("#orderModalResponse").empty().append('<a href="#" class="close" data-dismiss="alert">&times;</a>')
                $("#orderModalResponse").append(data.responseText)
                $("#orderModalResponse").addClass("alert alert-danger fade in");
            }
        });
        return false;
    }),
    $("modal").each( function() {
        $(this).on('hidden.bs.modal', function () {
            $(this).children(".modalResponse").empty().attr('class','modalResponse')
        })
    })
);