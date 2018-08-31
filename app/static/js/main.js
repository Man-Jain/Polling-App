a=1;
$(document).ready(function(){
    $("#add-option-g1").click(function(){
        $("fieldset").append("<div id='field-"+a+"' class='form-group'><label>Poll Choice</label> <input class='form-control' placeholder='Choice' type='text' name='choice-"+a+"' required> </div>");
        a++;
    });
    $("#remove-option-g1").click(function(){
        $("#field-"+a).remove();
        a--;
    });
});

$(function(){
    $('#btn-group1').click(function(){
        $.ajax({
            url: '/group1',
            data: $('#form-group1').serialize(),
            type: 'POST',
            success: function(response){
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
        $(function(){$("#alert-g1").show();});
    });
});

$(function(){
    $('#poll-submit-btn').click(function(){
        $.ajax({
            url: '/vote',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
        $(function(){$("#alert-g1").show();});
    });
});