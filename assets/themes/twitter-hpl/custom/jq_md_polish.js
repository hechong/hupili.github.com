$(document).ready(function(){
	$("img").map( function(){
		match = /^style=(.*)$/.exec($(this).attr('alt'));
		if (match){
			styles = match[1].split(";");
			for (var i = 0; i < styles.length; i ++){
				//alert(styles[i]);
				if (styles[i] == "center"){
					$(this).css("display", "block");
					$(this).css("margin-left", "auto");
					$(this).css("margin-right", "auto");
				}
			}
		}
	})
});
