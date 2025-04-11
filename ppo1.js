	window.addEventListener('load', removeLoader);
	window.addEventListener('contentmenu', ()=> {return false;});
loadTxt();
	function removeLoader() {
		var loader = document.querySelector('.loader');
		loader.classList.add('hidden');
			// var txt = document.querySelector('.loader_txt').textContent="Let's Go";
	}
	function loadTxt() {
		var loading_txt = document.querySelector('.loader_inner_txt');
		setTimeout(()=> {
			loading_txt.textContent="Background";
		},2000);
		setTimeout(()=> {
			loading_txt.textContent="Buttons";
		},4000);
		setTimeout(()=> {
			loading_txt.textContent="Blocks";
		},6000);
		setTimeout(()=> {
			loading_txt.textContent="Characters";
		},8000);
		setTimeout(()=> {
			loadTxt();
		},10000);
	}