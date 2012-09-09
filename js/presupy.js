var updateInlineLabel = function(row) {
    alert('hola mundo');
};
django.jQuery(function($){

    var updateInlineLabel = function(row) {
        alert('hola mundo 2');
    };

    /*
     Funcion que recalcula el total de Presupuesto
     antes de Guardarlo para mostrarlo en tiempo real
     */
    function recalcular_totales_presupuesto(){
        total = 0;
        baseimponible = 0;
        impuestos = 0;
        $('.dynamic-lineas').each(function(index,linea){
            id = $(linea).attr('id');
            cantidad = parseFloat($(linea).find('#id_'+id+'-cantidad').first().val());
            precio = parseFloat($(linea).find('#id_'+id+'-precio').val());
            descuento = parseFloat($(linea).find('#id_'+id+'-descuento').val());
            impuesto = parseFloat($(linea).find('#id_'+id+'-impuesto').val());
            neto = (cantidad*(precio * (1-descuento/100)));
            impuestos += neto * impuesto/100;
            baseimponible += neto;
            total += neto * (1+impuesto/100);
        })
        total = Math.round(total*10000)/10000;
        total = total.toString();
        total = total.replace('.',',');
        $('.field-total div p').first().text(total);

        baseimponible = Math.round(baseimponible*10000)/10000;
        baseimponible = baseimponible.toString();
        baseimponible = baseimponible.replace('.',',');
        $('.field-neto div p').first().text(baseimponible);

        impuestos = Math.round(impuestos*10000)/10000;
        impuestos = impuestos.toString();
        impuestos = impuestos.replace('.',',');
        $('.field-impuestos div p').first().text(impuestos);
    }
    /*Recalcular el Total al cambiar datos*/
    $('.field-cantidad,.field-precio,.field-descuento,.field-impuesto').keyup(recalcular_totales_presupuesto);

    /*Esto esta muy feo y es muy ineficiente pero por ahora es lo que ahi......*/
    setInterval(recalcular_totales_presupuesto,1000);
})