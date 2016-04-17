var orderModal = $('#newOrderModal')
var orderForm =  $('#orderForm');
$( document ).ready(
    orderForm.submit(function() {
        orderModal.find(".modalResponse").first().empty().attr('class','modalResponse');
        $.ajax({
            type: orderForm.attr('method'),
            url: orderForm.attr('action'),
            data: orderForm.serialize(),
            success: function(data) {
                  orderModal.modal('hide');
                  location.reload();
            },
            error: function(data) {
                orderModal.find(".modalResponse").first().empty().append('<a href="#" class="close" data-dismiss="alert">&times;</a>');
                orderModal.find(".modalResponse").first().append(data.responseText);
                orderModal.find(".modalResponse").first().addClass("alert alert-danger fade in");
            }
        });
        return false;
    }),
    $(".modal").each( function() {
        $(this).on('hidden.bs.modal', function () {
            $(this).find(".modalResponse").first().empty().attr('class','modalResponse');
        })
    })
);