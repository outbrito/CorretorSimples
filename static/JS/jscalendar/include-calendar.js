var inputs = document.getElementsByTagName('input');
for (i=0; i<inputs.length; i++) {
    var inp = inputs[i];
    
    if (inp.getAttribute('type') == 'text' && inp.className.match(/vDateField/)) {
        	
        // Shortcut links (calendar icon and "Today" link)
        var shortcuts_span = document.createElement('span');
        inp.parentNode.insertBefore(shortcuts_span, inp.nextSibling);
        var cal_link = document.createElement('input');
        cal_link.setAttribute('type', 'button');
		cal_link.setAttribute('style', 'background:url(/site_media/IMG/calendar.gif) no-repeat');
		cal_link.setAttribute('id', 'lancador'+i);
        shortcuts_span.appendChild(document.createTextNode('\240'));
        shortcuts_span.appendChild(document.createTextNode('\240|\240'));
        shortcuts_span.appendChild(cal_link);
		
		Calendar.setup({
	        inputField     :    inp.getAttribute('id'),     // id do campo de texto
	        ifFormat       :    "%d/%m/%Y",       			// formato da data
	        button         :    "lancador"+i   				// id do botão que lançará o calendário
	    });
	}
}