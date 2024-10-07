if ("undefined" === typeof ar_button_titles) {
    aspect_ratio_button_titles = {};
}

aspect_ratio_button_titles["Calc"] = "Show or hide the aspect ratio calculator";
aspect_ratio_button_titles["\u{21c5}"] = "Swap width and height values";
aspect_ratio_button_titles["\u2B07\ufe0f"] = "Get dimensions from txt2img/img2img sliders";
aspect_ratio_button_titles["\u{1f5bc}"] = "Get dimensions from image on current img2img tab";
aspect_ratio_button_titles["Calculate Height"] = "Calculate new height based on source aspect ratio";
aspect_ratio_button_titles["Calculate Width"] = "Calculate new width based on source aspect ratio";
aspect_ratio_button_titles["Apply"] = "Apply calculated width and height to txt2img/img2img sliders";

onUiUpdate(function(){
    gradioApp().querySelectorAll('#txt2img_container_aspect_ratio button, #img2img_container_aspect_ratio button').forEach(function(elem){
	tooltip = aspect_ratio_button_titles[elem.textContent];
	    if(tooltip){
		elem.title = tooltip;
            }
    })
