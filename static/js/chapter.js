$(document).ready(function(){
    $(".results").hide();
    $("#frm_new_question").hide();
    $("#addquestion").click(function(){
        $("#frm_new_question").show();
    });
    $("#frm_new_character").hide();
    $("#addcharacter").click(function(){
        $("#frm_new_character").show();
    });
    $("#frm_new_character_reference").hide();
    $("#addcharacterreference").click(function(){
        $("#frm_new_character_reference").show();
    });
    $(".answer_button").click(function(){
        var useranswer = $(this).parent().find("#user_answer").val();
        var correctanswer = $(this).parent().find("#correct_answer").val();
        if(useranswer == correctanswer) {
            $(this).parent().find("#correct").show();
            $(this).parent().find("#incorrect").hide();
        } else {
                $(this).parent().find("#correct").hide();
                $(this).parent().find("#incorrect").show();
        }
    });
    $(".show_refs").click(function(){
        var paras = $(this).parent().find("#paras").val().split(",");
        alert("See paragraphs : " + paras);
        $("p").css("background-color", "white");
        for(i in paras){
            $("#" + paras[i].trim()).css("background-color", "yellow");
        }
    });
});
