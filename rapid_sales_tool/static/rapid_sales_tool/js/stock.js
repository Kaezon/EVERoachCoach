var addItemModal = $('#newItemModal');
var addStockModal = $('#addStockModal')
var itemForm =  $('#addItemForm');
var stockForm = $('#addStockForm');
$( document ).ready(
    addItemModal.submit(function() {
        addItemModal.find(".modalResponse").first().empty().attr('class','modalResponse');
        $.ajax({
            type: itemForm.attr('method'),
            url: itemForm.attr('action'),
            data: itemForm.serialize(),
            success: function(data) {
                  addItemModal.modal('hide');
                  location.reload();
            },
            error: function(data) {
                addItemModal.find(".modalResponse").first().empty().append('<a href="#" class="close" data-dismiss="alert">&times;</a>');
                addItemModal.find(".modalResponse").first().append(data.responseText);
                addItemModal.find(".modalResponse").first().addClass("alert alert-danger fade in");
            }
        });
        return false;
    }),
    stockForm.submit(function() {
        addStockModal.find(".modalResponse").first().empty().attr('class','modalResponse');
        $.ajax({
            type: stockForm.attr('method'),
            url: stockForm.attr('action'),
            data: stockForm.serialize(),
            success: function(data) {
                  addStockModal.modal('hide');
                  location.reload();
            },
            error: function(data) {
                addStockModal.find(".modalResponse").first().empty().append('<a href="#" class="close" data-dismiss="alert">&times;</a>');
                addStockModal.find(".modalResponse").first().append(data.responseText);
                addStockModal.find(".modalResponse").first().addClass("alert alert-danger fade in");
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