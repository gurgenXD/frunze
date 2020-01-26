(function($) {
    $(document).ready(function(){
        $('#id_category').on('change', function() { 
            $.ajax({
            	type: 'GET',
            	url: '/load/subcategory/',
            	data: { category_id: $(this).val() },
            	success: function(data) {
                    data = data.subcategories;
                    $('#id_subcategory').empty();
                    $('#id_subcategory').append('<option value>---------</option>');
                    for(var i = 0; i < data.length; i++){
                        $('#id_subcategory').append('<option value="' + data[i][0] + '">' + data[i][1] + '</option>');
                    }
                }
            });
        });
    });
})(django.jQuery);