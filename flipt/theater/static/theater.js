	var plist = document.getElementById("sidemenu");
	var playArray = plist.getElementsByTagName("a");
	var i = 0;
	var pArray = [];
	while (i < playArray.length){
		if (playArray[i].getAttribute("href") in pArray){
			continue;
		}
		else {
		pArray[i] = playArray[i].getAttribute("href");
		i ++;
		}
	}
	function findPos(link){

		for (i = 0; i < pArray.length; i ++){
			if (pArray[i] == link){
				return i;
			}
		}
	}		
	function setDest(link){
		console.log(link);
		var pos = findPos(link);
		console.log(pos);
		var prev = document.getElementById("previous");
		var next = document.getElementById("next");
		if (pos == 0){
			prev.setAttribute("href", pArray[pos]);
		}
		else{
			prev.setAttribute("href", pArray[pos - 1]);
		}
		if (pos == pArray.length - 1){
			next.setAttribute("href", pArray[pos]);
		}
		else{
			next.setAttribute("href", pArray[pos + 1]);
		}
	}	
        function loadVid(h){
		var vid = document.getElementsByName("coursevid")[0];
		vid.setAttribute("src", h);	
	}	
	