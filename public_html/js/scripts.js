//Funzione che valida le form di inserimento nuovo admin
function validaFormNewAdmin(){
	var User = document.getElementById("Username").value;
	var Pwd = document.getElementById("Password").value;
	var CPwd = document.getElementById("ConfermaPassword").value;
	var check = true;

		//Svuoto gli errori dell'username
	var Form = document.getElementById('user').innerHTML;
		var Form = Form.replace('<span class="error"><span lang="en">Username<\/span> obbligatorio <\/span>', "<!-- errore_username -->");
		document.getElementById('user').innerHTML = Form;

		//Svuoto gli errori della password
	var Form = document.getElementById('pwd').innerHTML;
		var Form = Form.replace('<span class="error"><span lang="en">Password<\/span> obbligatoria <\/span>', "<!-- errore_password -->");
		document.getElementById('pwd').innerHTML = Form;

		//Svuoto gli errori della conferma password
	var Form = document.getElementById('cpwd').innerHTML;
		var Form = Form.replace('<span class="error">Conferma <span lang="en">Password<\/span> obbligatoria <\/span>', "<!-- errore_conferma_password -->");
		document.getElementById('cpwd').innerHTML = Form;

		//Svuoto gli errori della conferma password2
	var Form = document.getElementById('cpwd').innerHTML;
		var Form = Form.replace('<span class="error">Le <span lang="en">Password<\/span> non corrispondono <\/span>', "<!-- errore_conferma_password -->");
		document.getElementById('cpwd').innerHTML = Form;

		//Svuoto gli errori dei caratteri vietati
		var Form = document.getElementById('inizioForm').innerHTML;
		var Form = Form.replace('<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>', "<!-- errore_caratteri -->");
		document.getElementById('inizioForm').innerHTML = Form;

		//Controllo se sono presenti caratteri vietati
	if(User.indexOf("<") >= 0 || User.indexOf(">") >= 0 || User.indexOf(";") >= 0 ||
		 Pwd.indexOf("<") >= 0 || Pwd.indexOf(">") >= 0 || Pwd.indexOf(";") >= 0 ||
	 	 CPwd.indexOf("<") >= 0 || CPwd.indexOf(">") >= 0 || CPwd.indexOf(";") >= 0){
		var Form = document.getElementById('inizioForm').innerHTML;
		var Form = Form.replace("<!-- errore_caratteri -->",'<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>');
		document.getElementById('inizioForm').innerHTML = Form;
		check = false;
	}

		//Controllo se il campo username è definito e lo segnalo
	if(User == "" || User == "undefined"){
		var Form = document.getElementById('user').innerHTML;
		var Form = Form.replace("<!-- errore_username -->",'<span class="error"><span lang="en">Username<\/span> obbligatorio <\/span>');
		document.getElementById('user').innerHTML = Form;
		check = false;
	}
	//Controllo se il campo password è definito e lo segnalo
	if(Pwd == "" || Pwd == "undefined"){
		var Form = document.getElementById('pwd').innerHTML;
		var Form = Form.replace("<!-- errore_password -->",'<span class="error"><span lang="en">Password<\/span> obbligatoria <\/span>');
		document.getElementById('pwd').innerHTML = Form;
		check = false;
	}
	//Controllo se il campo conferma password è definito e lo segnalo
	if(CPwd == "" || CPwd == "undefined"){
		var Form = document.getElementById('cpwd').innerHTML;
		var Form = Form.replace("<!-- errore_conferma_password -->",'<span class="error">Conferma <span lang="en">Password<\/span> obbligatoria <\/span>');
		document.getElementById('cpwd').innerHTML = Form;
		check = false;
	}
	//Controllo se il campo password sia uguale al campo conferma password e lo segnalo
	if(Pwd != CPwd){
		var Form = document.getElementById('cpwd').innerHTML;
		var Form = Form.replace("<!-- errore_conferma_password -->",'<span class="error">Le <span lang="en">Password<\/span> non corrispondono <\/span>');
		document.getElementById('cpwd').innerHTML = Form;
		check = false;
	}
	return check;
}

//Funzione che valida le form di login
function validaFormLogin(){
	var User = document.getElementById("Username").value;
	var Pwd = document.getElementById("Password").value;
	var check = true;

//Svuoto gli errori dell'username
		var Form = document.getElementById('user').innerHTML;
		var Form = Form.replace(/<span class="error" id="errore1">.*<\/span>/ , "<!-- errore_username -->");
		document.getElementById('user').innerHTML = Form;
//Svuoto gli errori della password
		var Form = document.getElementById('pwd').innerHTML;
		var Form = Form.replace(/<span class="error" id="errore2">.*<\/span>/, "<!-- errore_password -->");
		document.getElementById('pwd').innerHTML = Form;

//Controllo se il campo username è definito e lo segnalo
	if(User == "" || User == "undefined"){
		var Form = document.getElementById('user').innerHTML;
		var Form = Form.replace("<!-- errore_username -->",'<span class="error" id="errore1"><span lang="en">Username<\/span> non inserito <\/span>');
		document.getElementById('user').innerHTML = Form;
		check = false;
	}
//Controllo se il campo password è definito e lo segnalo
	if(Pwd == "" || Pwd == "undefined"){
		var Form = document.getElementById('pwd').innerHTML;
		var Form = Form.replace("<!-- errore_password -->",'<span class="error" id="errore2"><span lang="en">Password<\/span> non inserita <\/span>');
		document.getElementById('pwd').innerHTML = Form;
		check = false;
	}
	return check;
}

//Funzione che valida le form di inserimento nuovo commento
function validaFormNewCommento(){
	var Name = document.getElementById("Nome").value;
	var Mail = document.getElementById("Email").value;
	var Testo = document.getElementById("Testo").value;
	var EmailRegExp = /^[^@]+@+[^\.]+\.+[^\.]+$/;
	var check = true;
//Svuoto gli errori del nome
		var Form = document.getElementById('name').innerHTML;
		var Form = Form.replace('<span class="error">Nome obbligatorio <\/span>', "<!-- errore_nome -->");
		document.getElementById('name').innerHTML = Form;

//Svuoto gli errori della mail
		var Form = document.getElementById('email').innerHTML;
		var Form = Form.replace('<span class="error"><span lang="en">Email<\/span> obbligatoria <\/span>', "<!-- errore_email -->");
		document.getElementById('email').innerHTML = Form;

//Svuoto gli errori della mail
		var Form = document.getElementById('email').innerHTML;
		var Form = Form.replace('<span class="error"><span lang="en">Email<\/span> non valida <\/span>', "<!-- errore_REemail -->");
		document.getElementById('email').innerHTML = Form;

//Svuoto gli errori del testo
		var Form = document.getElementById('testo').innerHTML;
		var Form = Form.replace('<span class="error">Testo obbligatorio <\/span>', "<!-- errore_testo -->");
		document.getElementById('testo').innerHTML = Form;

		//Svuoto gli errori dei caratteri vietati
		var Form = document.getElementById('inizioForm').innerHTML;
		var Form = Form.replace('<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>', "<!-- errore_caratteri -->");
		document.getElementById('inizioForm').innerHTML = Form;

		//Controllo se sono presenti caratteri vietati
	if(Name.indexOf("<") >= 0 || Name.indexOf(">") >= 0 || Name.indexOf(";") >= 0 ||
		 Mail.indexOf("<") >= 0 || Mail.indexOf(">") >= 0 || Mail.indexOf(";") >= 0 ||
	 	 Testo.indexOf("<") >= 0 || Testo.indexOf(">") >= 0 || Testo.indexOf(";") >= 0){
		var Form = document.getElementById('inizioForm').innerHTML;
		var Form = Form.replace("<!-- errore_caratteri -->",'<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>');
		document.getElementById('inizioForm').innerHTML = Form;
		check = false;
	}

	if(Name == "" || Name == "undefined"){
		var Form = document.getElementById('name').innerHTML;
		var Form = Form.replace("<!-- errore_nome -->",'<span class="error">Nome obbligatorio <\/span>');
		document.getElementById('name').innerHTML = Form;
		check = false;
	}
	if(Mail == "" || Mail == "undefined"){
		var Form = document.getElementById('email').innerHTML;
		var Form = Form.replace("<!-- errore_email -->",'<span class="error"><span lang="en">Email<\/span> obbligatoria <\/span>');
		document.getElementById('email').innerHTML = Form;
		check = false;
	}
	else{
		if(!EmailRegExp.test(Mail)){
			var Form = document.getElementById('email').innerHTML;
			var Form = Form.replace("<!-- errore_REemail -->",'<span class="error"><span lang="en">Email<\/span> non valida <\/span>');
			document.getElementById('email').innerHTML = Form;
			check = false;
		}
	}
	if(Testo == "" || Testo == "undefined"){
		var Form = document.getElementById('testo').innerHTML;
		var Form = Form.replace("<!-- errore_testo -->",'<span class="error">Testo obbligatorio <\/span>');
		document.getElementById('testo').innerHTML = Form;
		check = false;
	}
	return check;
}

//Funzione che valida le form di inserimento nuovo prodotto/servizio
function validaFormNewProdotto(){
		var Nome = document.getElementById("new_nome").value;
		var Desc = document.getElementById("new_descrizione").value;
		var Prezzo = document.getElementById("new_prezzo").value;
//Svuoto gli errori del nome
		var Form = document.getElementById('l_nome').innerHTML;
		var Form = Form.replace('<span class="error">Nome obbligatorio <\/span>', "<!-- errore_nome -->");
		document.getElementById('l_nome').innerHTML = Form;

//Svuoto gli errori della descrizione
		var Form = document.getElementById('l_descrizione').innerHTML;
		var Form = Form.replace('<span class="error">Descrizione obbligatoria <\/span>', "<!-- errore_descrizione -->");
		document.getElementById('l_descrizione').innerHTML = Form;

//Svuoto gli errori del prezzo
		var Form = document.getElementById('l_prezzo').innerHTML;
		var Form = Form.replace('<span class="error">Prezzo obbligatorio</span>', "<!-- errore_prezzo -->");
		document.getElementById('l_prezzo').innerHTML = Form;
	var check = true;

	//Svuoto gli errori dei caratteri vietati
	var Form = document.getElementById('inizioForm').innerHTML;
	var Form = Form.replace('<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>', "<!-- errore_caratteri -->");
	document.getElementById('inizioForm').innerHTML = Form;

	//Controllo se sono presenti caratteri vietati
	if(Nome.indexOf("<") >= 0 || Nome.indexOf(">") >= 0 || Nome.indexOf(";") >= 0 ||
	 Desc.indexOf("<") >= 0 || Desc.indexOf(">") >= 0 || Desc.indexOf(";") >= 0 ||
	 Prezzo.indexOf("<") >= 0 || Prezzo.indexOf(">") >= 0 || Prezzo.indexOf(";") >= 0){
	var Form = document.getElementById('inizioForm').innerHTML;
	var Form = Form.replace("<!-- errore_caratteri -->",'<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>');
	document.getElementById('inizioForm').innerHTML = Form;
	check = false;
	}


	if(Nome == "" || Nome == "undefined"){
		var Form = document.getElementById('l_nome').innerHTML;
		var Form = Form.replace("<!-- errore_nome -->",'<span class="error">Nome obbligatorio <\/span>');
		document.getElementById('l_nome').innerHTML = Form;
		check = false;
	}
	if(Desc == "" || Desc == "undefined"){
		var Form = document.getElementById('l_descrizione').innerHTML;
		var Form = Form.replace("<!-- errore_descrizione -->",'<span class="error">Descrizione obbligatoria <\/span>');
		document.getElementById('l_descrizione').innerHTML = Form;
		check = false;
	}
	if(Prezzo == "" || Prezzo == "undefined"){
		var Form = document.getElementById('l_prezzo').innerHTML;
		var Form = Form.replace("<!-- errore_prezzo -->",'<span class="error">Prezzo obbligatorio</span>');
		document.getElementById('l_prezzo').innerHTML = Form;
		check = false;
	}
	return check;
}


//Funzione che valida le form di modifica nuovo prodotto/servizio
function validaFormEditProdotto(){
		var Nome = document.getElementById("edit_nome").value;
		var Desc = document.getElementById("edit_descrizione").value;
		var Prezzo = document.getElementById("edit_prezzo").value;
//Svuoto gli errori del nome
		var Form = document.getElementById('l_edit_nome').innerHTML;
		var Form = Form.replace('<span class="error">Nome obbligatorio <\/span>', "<!-- errore_nome -->");
		document.getElementById('l_edit_nome').innerHTML = Form;

//Svuoto gli errori della descrizione
		var Form = document.getElementById('l_edit_descrizione').innerHTML;
		var Form = Form.replace('<span class="error">Descrizione obbligatoria <\/span>', "<!-- errore_descrizione -->");
		document.getElementById('l_edit_descrizione').innerHTML = Form;

//Svuoto gli errori del prezzo
		var Form = document.getElementById('l_edit_prezzo').innerHTML;
		var Form = Form.replace('<span class="error">Prezzo obbligatorio <\/span>', "<!-- errore_prezzo -->");
		document.getElementById('l_edit_prezzo').innerHTML = Form;
	var check = true;

	//Svuoto gli errori dei caratteri vietati
	var Form = document.getElementById('inizioEditForm').innerHTML;
	var Form = Form.replace('<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>', "<!-- errore_caratteri -->");
	document.getElementById('inizioEditForm').innerHTML = Form;

	//Controllo se sono presenti caratteri vietati
	if(Nome.indexOf("<") >= 0 || Nome.indexOf(">") >= 0 || Nome.indexOf(";") >= 0 ||
	 Desc.indexOf("<") >= 0 || Desc.indexOf(">") >= 0 || Desc.indexOf(";") >= 0 ||
	 Prezzo.indexOf("<") >= 0 || Prezzo.indexOf(">") >= 0 || Prezzo.indexOf(";") >= 0){
	var Form = document.getElementById('inizioEditForm').innerHTML;
	var Form = Form.replace("<!-- errore_caratteri -->",'<span class="error">Non sono ammessi i caratteri "&gt;", "&lt;" ed ";"<\/span>');
	document.getElementById('inizioEditForm').innerHTML = Form;
	check = false;
	}


	if(Nome == "" || Nome == "undefined"){
		var Form = document.getElementById('l_edit_nome').innerHTML;
		var Form = Form.replace("<!-- errore_nome -->",'<span class="error">Nome obbligatorio <\/span>');
		document.getElementById('l_edit_nome').innerHTML = Form;
		check = false;
	}
	if(Desc == "" || Desc == "undefined"){
		var Form = document.getElementById('l_edit_descrizione').innerHTML;
		var Form = Form.replace("<!-- errore_descrizione -->",'<span class="error">Descrizione obbligatoria <\/span>');
		document.getElementById('l_edit_descrizione').innerHTML = Form;
		check = false;
	}
	if(Prezzo == "" || Prezzo == "undefined"){
		var Form = document.getElementById('l_edit_prezzo').innerHTML;
		var Form = Form.replace("<!-- errore_prezzo -->",'<span class="error">Prezzo obbligatorio <\/span>');
		document.getElementById('l_edit_prezzo').innerHTML = Form;
		check = false;
	}
	return check;
}

//
// Le seguenti funzioni fanno uso di JQuery.
//

// Ricerca nella pagina dei servizi
function CercaServizio(){
	//prende il valore (lovercase per rendere case insensitive)
	var query= $("#ricerca").val().toLowerCase();
	//azzera precedenti ricerche
	$("li").filter(".servizio").css("display","inline")
	//nasconde i servizi che non contengono la parola cercata
	if (query != null){
		$("li").filter(".servizio").filter(function(){
			return (this.innerHTML.toLowerCase().indexOf(query)== -1);
		}).css("display", "none");
	}
	$('html, body').animate({
        scrollTop: $("#lista_servizi").offset().top
    }, 200);
	return false;
}

// Azzera una ricerca nella pagina dei servizi
function AzzeraFiltri(){
	var query= $("#ricerca").val("");
	//mostra tutti i servizi
	$("li").filter(".servizio").css("display","inline")
}

// Solo se js è attivo viene mostrato il form per la ricerca
$(document).ready(function(){
	$("#sezionericerca").html('<h3>Ricerca tra i Servizi <span class="reader">(necessita di Javascript)</span></h3>' +
	'<form action="#lista_servizi"><p><input type="text" id="ricerca" tabindex="1"/></p>' +
	'<p><input class="pulsante" type="button" id="bottoneazzera" value="Azzera filtri" onclick="AzzeraFiltri()" tabindex="3"/>' +
	'<input class="pulsante" type="submit" id="bottonericerca" value="Cerca!" onclick="return CercaServizio()" tabindex="2"/></p></form>'
	);
});
