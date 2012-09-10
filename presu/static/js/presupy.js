(function($){

    function parseFloatNoNaN(string){
        result = parseFloat(string);
        if(isNaN(result)){
            result = 0;
        }
        return result;
    }
    /*
     Funcion que recalcula el total de Presupuesto
     antes de Guardarlo para mostrarlo en tiempo real
     */
    function recalcular_totales_presupuesto(){
        baseimponible = 0;
        impuestos = 0;
        total = 0;
        lineas = $('#lineas-group').find('.grp-dynamic-form');

        $(lineas).each(function(i,e){
                if(!$(e).is('.grp-predelete')){
                    cantidad = parseFloatNoNaN($(e).find('.cantidad input').val());
                    precio = parseFloatNoNaN($(e).find('.precio input').val());
                    descuento = parseFloatNoNaN($(e).find('.descuento input').val());
                    impuesto = parseFloatNoNaN($(e).find('.impuesto input').val());
                    baseimponible += cantidad * precio * (1-descuento/100);
                    impuestos += parseFloatNoNaN(cantidad * precio * (1-descuento/100) * (impuesto/100));
                }
        });
        total = baseimponible + impuestos ;
        $('.grp-row.neto .grp-readonly').text(baseimponible);
        $('.grp-row.impuestos .grp-readonly').text(impuestos);
        $('.grp-row.total .grp-readonly').text(total);
    }

    function recalcular_neto_linea_presupuesto(){
        neto = 0;
        lineas = $('#lineas-group').find('.grp-dynamic-form');

        $(lineas).each(function(i,e){
            cantidad = parseFloatNoNaN($(e).find('.cantidad input').val());
            precio = parseFloatNoNaN($(e).find('.precio input').val());
            descuento = parseFloatNoNaN($(e).find('.descuento input').val());
            impuesto = parseFloatNoNaN($(e).find('.impuesto input').val());
            neto = cantidad * precio * (1-descuento/100);
            $(e).find('.neto p.grp-readonly').text(neto);
        });
    }

    /*Esto esta muy feo y es muy ineficiente pero por ahora es lo que ahi......*/
    $(document).ready(function(){
        $('input').keyup(function(){
            recalcular_totales_presupuesto();
            recalcular_neto_linea_presupuesto();
        });

        $('a.grp-delete-handler').bind('click', function() {
            setTimeout(recalcular_totales_presupuesto,0);
            setTimeout(recalcular_neto_linea_presupuesto,0);
        });
    });
})(django.jQuery)