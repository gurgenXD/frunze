$(document).ready(function(){
    $('input:radio[name=options]').on('change', function() { 
        $.ajax({
            type: 'GET',
            url: '/products/change/bar_type/',
            data: { offer_id: $(this).data('offer-id') },
            success: function(data) {
                $('#product-price').html(data.product_price);
                $('#in-stock').attr("max", data.in_stock);
                $('#in-stock').val("1");
            }
        });
    });

    $('#add-to-cart').on('click', function() {
        product_id = $('#add-to-cart').data('product-id');
        price = $('#product-price').text();
        quantity = $('#in-stock').val();
        max_q = $('#in-stock').attr('max');
        bar_type = $('input:radio[name=options]:checked').parent().text().trim();

		data = {
            product_id: product_id,
            price: price,
            quantity: quantity,
            max_q: max_q,
            bar_type: bar_type,
        }

        $.ajax({
        	type: 'GET',
        	url: '/orders/add-to-cart/',
        	data: data,
            success: function(data) {
                $('#add-to-cart').addClass('d-none');
                $('#in-cart').removeClass('d-none');
                $('#cart-len').html(data.cart_len);
        	}
        });
    });

    $('.remove-from-cart').on('click', function() {
        product_id = $(this).data('product-id');

        $.ajax({
        	type: 'GET',
        	url: '/orders/remove-from-cart/',
        	data: {product_id: product_id},
            success: function(data) {
                $('.cart-item-' + product_id).addClass('d-none');
                $('.cart-item-' + product_id).removeClass('d-flex');
                $('#cart-len').html(data.cart_len);
        	}
        });
    });

    $('.change-qty').on('click', function() {
        product_id = $(this).parent().data('product-id');
        quantity = $(this).siblings('input').val();

        data = {
            product_id: product_id,
            quantity: quantity,
        }

        $.ajax({
        	type: 'GET',
        	url: '/orders/change-qty/',
        	data: data,
            success: function(data) {
                // $('.cart-item-' + product_id).addClass('d-none');
                $('.price-' + product_id).html(data.cost);
                $('#cart-len').html(data.cart_len);
        	}
        });
    });

    $('#CallBackModal button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        phone = $('#CallBackModalPhone').val();
        csrf_token = $('#CallBackModal form [name="csrfmiddlewaretoken"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            phone: phone,
        }

        $.ajax({
        	type: 'POST',
        	url: $('#CallBackModal form').attr('action'),
        	data: data,
            success: function(data) {
                if (!data.status) {
                    $('#CallBackModal .alert-danger').removeClass('d-none');
                } else {
                    $('#CallBackModal .modal-success').removeClass('d-none');
                    $('#CallBackModal .modal-success').addClass('d-flex');
                }
        	}
        });
    });

    $('#order-form button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        full_name = $('#inputName').val();
        phone = $('#inputPhone').val();
        email = $('#inputEmail').val();
        csrf_token = $('#order-form [name="csrfmiddlewaretoken"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            full_name: full_name,
            phone: phone,
            email: email,
        }

        $.ajax({
        	type: 'POST',
        	url: $('#order-form').attr('action'),
        	data: data,
            success: function(data) {
                if (!data.status) {
                    $('#order-form-alert').removeClass('d-none');
                } else {
                    window.location.replace('/orders/order-done/');
                }
        	}
        });
    });

    $('.search-input').on('keypress',function(e){
        if(e.which == 13) {
            $(this).parent().parent('.search-box').submit();
        }
     });

});