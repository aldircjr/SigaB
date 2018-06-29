// quando o document estiver ready
$(function() {
    $('.input').hide();
    $.each($("tr"), function(key, val) {
        var qtFilhas = $(this).find('td').length;
        $(this).attr('data-childs', qtFilhas);
        if (qtFilhas == 6) {
            $(this).find('.botao').hide();
        }
    });

  $("input").on('keyup', function (e) {
     if (e.keyCode == 13) {
     let parente = $(this).parent()
     // parente.find('button').click(e)
      }
    });


    $('button').click(function(e){
        let parentId = $(this).parent().attr('id')
        let materiaId = $('#'+parentId+' .materia').attr('data-materia')
        let alunoId = $('#'+parentId+' .aluno').attr('data-aluno')
        let nota = $('#'+parentId+' .input').val();
        let botao = $(this).parent().parent()
        $('#'+parentId+' .input').val('');
        if ($('#'+parentId+' .input').is(":visible")) {
            
            if (nota >= 0 && nota <=10 && (!isNaN(parseFloat(nota)) && isFinite(nota))) {
                let url = $('#urlInserirNota').attr('data-url').slice(0,-5)
                $.get(url+materiaId+'/'+alunoId+'/'+nota+'', function(response) {
                     console.log(response);
                     if (response.status) {
                     let primeiro = $('#'+parentId).parent()
                     let elemento = $('<td class=\"nota\"></tdx>');
                     elemento.insertBefore(primeiro);
                     let linhaDeNotas = botao.parent().find('.nota'); 
                     //configurar para atualizar a table
                     atualizaLinha(materiaId, alunoId, linhaDeNotas);
                     $('#'+parentId+' .input').fadeOut();    
                     }else{
                        alert("Deu Pau");
                     }  
                  });
        }else{
            $('#'+parentId+' .input').fadeOut();
        }
        }else{
                $('#'+parentId+' .input').fadeIn();
                $('#'+parentId+' .input').focus();  
        }



    });

    function atualizaLinha(materiaId, alunoId, listaNotas){
         // let primeiro = $('#'+ondeInserir).parent()
         let url = $('#urlAtualizaNota').attr('data-url').slice(0,-4)
         // let elemento = $('<td class=\"nota\"></tdx>');
         // elemento.insertBefore(primeiro);
         $.get(url+materiaId+'/'+alunoId, function(response) {

             let i = 0;

              $.each(listaNotas, function() { 
                  let nota = response.notas[i].valorNota.toFixed(1)
                  i = i + 1;
                  $(this).text(nota)
                 });
            });
         $.each($("tr"), function(key, val) {
            var qtFilhas = $(this).find('td').length;
            $(this).attr('data-childs', qtFilhas);
            if (qtFilhas == 6) {
            $(this).find('.botao').hide();
        }
    });
}

});