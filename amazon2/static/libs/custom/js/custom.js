$(document).ready(function(e){
    $('.search-panel .dropdown-menu').find('a').click(function(e) {
    e.preventDefault();
    var param = $(this).attr("href").replace("#","");
    var concept = $(this).text();
    $('.search-panel span#search_concept').text(concept);
    $('.input-group #search_param').val(param);
    });
});

(function($){
	
	/* -------------------------------------------------------- */ 
	/*	//set Global variables
	/* -------------------------------------------------------- */ 
	var cards = $(".card-drop"),
		toggler = cards.find(".toggle"),
		links = cards.find("ul>li>a"),
		li = links.parent('li'),
		count = links.length,
		width = links.outerWidth();

		//set z-Index of drop Items
		links.parent("li").each(function(i){
			$(this).css("z-index" , count - i); //invert the index values
		});

		//set top margins & widths of li elements
		function setClosed(){
			li.each(function(index){
				 $(this).css("top" , index *2)
				 		.css("width" , width - index *2)
				 		.css("margin-left" , (index*2)/2);
			});
			li.addClass('closed');
			toggler.removeClass("active");
		}
		setClosed();

	/* -------------------------------------------------------- */ 
	/*	Toggler Click handler
	/* -------------------------------------------------------- */ 
	toggler.on("mousedown" , function(){
		var $this = $(this); //cache $(this)
		//if the menu is active:
		if($this.is(".active")){
			setClosed();
		}else{
			//if the menu is un-active:
			$this.addClass("active");
			li.removeClass('closed');
			//set top margins
			li.each(function(index){
				 $(this).css("top" , 60 * (index + 1))
				 		.css("width" , "100%")
				 		.css("margin-left" , "0px");
			});
		}
	});

	/* -------------------------------------------------------- */ 
	/*	Links Click handler
	/* -------------------------------------------------------- */ 
	links.on("click" , function(e){
		var $this = $(this),
			label = $this.data("label");
			icon = $this.children("i").attr("class");
			
			li.removeClass('active');
		if($this.parent("li").is("active")){
			$this.parent('li').removeClass("active");
		}else{
			$this.parent("li").addClass("active");
		}
		toggler.children("span").text(label);
		toggler.children("i").removeClass().addClass(icon);
		setClosed();
		e.preventDefault;
	});

})(jQuery);

	/* -------------------------------------------------------- */ 
	/*	Resizing Select
	/* -------------------------------------------------------- */ 

$(document).ready(function() {
	$('#resizing_select').change(function(){
		 $("#width_tmp_option").html($('#resizing_select option:selected').text());
		 $(this).width($("#width_tmp_select").width());  
	});
 });