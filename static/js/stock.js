var addItemModal = $('#newItemModal');
var addStockModal = $('#addStockModal')
var itemForm =  $('#addItemForm');
var stockForm = $('#addStockForm');
$( document ).ready(
    itemForm.submit(function() {
        $.ajax({
            type: itemForm.attr('method'),
            url: itemForm.attr('action'),
            data: itemForm.serialize(),
            success: function(data) {
                  addItemModal.modal('hide')
                  location.reload()
            },
            error: function(data) {
                itemForm.children(".modalResponse").empty().append('<a href="#" class="close" data-dismiss="alert">&times;</a>')
                itemForm.children(".modalResponse").append(data.responseText)
                itemForm.children(".modalResponse").addClass("alert alert-danger fade in");
            }
        });
        return false;
    }),
    stockForm.submit(function() {
        $.ajax({
            type: stockForm.attr('method'),
            url: stockForm.attr('action'),
            data: stockForm.serialize(),
            success: function(data) {
                  addStockModal.modal('hide')
                  location.reload()
            },
            error: function(data) {
                stockForm.children(".modalResponse").empty().append('<a href="#" class="close" data-dismiss="alert">&times;</a>')
                stockForm.children(".modalResponse").append(data.responseText)
                stockForm.children(".modalResponse").addClass("alert alert-danger fade in");
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