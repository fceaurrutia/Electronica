function cambiarPagina(pag){
    document.getElementById("page").value = pag;
    document.getElementById("filtro").submit(); 
}
function valorSlider(val){
    document.getElementById("x").value=parseInt(val);
    cambiarPagina(1);
}

function validarNumero(e, tel){
	tecla = (document.all) ? e.keyCode : e.which;
	//Tecla de retroceso para borrar, siempre la permite.
	if (tecla==8){
		return true;
	}
	if((tecla!=57 && tecla!=50) && tel.value.length == 0){
		return false;
	}
	if(tecla!=50 && tel.value.length == 1 && tel.value=="2"){
		return false;
	}
	// Patron de entrada, en este caso solo acepta numeros.
	patron =/[0-9]/;
	tecla_final = String.fromCharCode(tecla);
	return patron.test(tecla_final);
}

function validarNombre(e, nombre){
	tecla = (document.all) ? e.keyCode : e.which;

	//Tecla de retroceso para borrar, siempre la permite
	if (tecla==8){
		return true;
	}
	// Patron de entrada, en este caso solo acepta letras.
	patron =/[a-zA-Z áéíóúýÁÉÍÓÚÝ]/;
	tecla_final = String.fromCharCode(tecla);
	return patron.test(tecla_final);
}

function validarCorreo(e) {
	tecla = (document.all) ? e.keyCode : e.which;
	if(tecla == 32){
		return false;
	}else{
		return true;
	}
}

function validarDescuento(e, tel){
	tecla = (document.all) ? e.keyCode : e.which;
	//Tecla de retroceso para borrar, siempre la permite.
	if (tecla==8){
		return true;
	}
	if(tel.value > 100){
		tel.value = 100;
	}
	// Patron de entrada, en este caso solo acepta numeros.
	patron =/[0-9]/;
	tecla_final = String.fromCharCode(tecla);
	return patron.test(tecla_final);
}