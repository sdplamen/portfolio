document.addEventListener('DOMContentLoaded', function() {
    const images = [
        'https://staging-jubilee.flickr.com/65535/54629506863_771d2cabae_o.jpg',
        'https://staging-jubilee.flickr.com/65535/54620822916_ef4200bb39_o.jpg',
        'https://staging-jubilee.flickr.com/65535/54572746712_c62e0f99d0_o.jpg',
        'https://staging-jubilee.flickr.com/65535/54539767076_e08f3b6436_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54541186370_74d59eac19_b.jpg',
		'https://staging-jubilee.flickr.com/65535/54605030534_d7e8c08f60_b.jpg',
		'https://staging-jubilee.flickr.com/65535/54601561423_bc9c902ec9_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54597893398_c1d6b05dac_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54599039501_56204236aa_b.jpg',
		'https://staging-jubilee.flickr.com/65535/54549662373_3cfe7ca1d8_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54589793883_e69baaa649_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54582061417_cfe8d2dc1f_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54534179307_f1b672c6dd_b.jpg',
		'https://staging-jubilee.flickr.com/65535/54532896717_417bc8006f_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54522049567_dd1c9d8ca7_o.jpg',
		'https://staging-jubilee.flickr.com/65535/54497123454_591802d903_b.jpg',
    ];

    let currentImageIndex = 0;
    const body = document.body;

    function changeBackground() {
        body.style.backgroundImage = `url('${images[currentImageIndex]}')`;
        currentImageIndex = (currentImageIndex + 1) % images.length; // Cycle through images
    }

    // Set the initial background image
    changeBackground();

    // Change background every 5 seconds (5000 milliseconds)
    setInterval(changeBackground, 5000);
});

// header scrolling effect
$(window).on('scroll', function(){
	if($(window).scrollTop()){
      $('header').addClass('nav-show');
		  
	} 
	else{
		$('header').removeClass('nav-show');
	}
	   
})

//hamburger
const navSlide = () => {
	 const hamburger = document.querySelector(".hamburger");
	 const navbar = document.querySelector(".nav-bar");
	 const navLinks = document.querySelectorAll(".nav-bar li");

     hamburger.onclick = () => {
		
	 navbar.classList.toggle("nav-active");
		 
      //Animation links
	 navLinks.forEach((link, index) => {
		if (link.style.animation) {
			link.style.animation = "";
		} else {
			link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7+1}s`;
		   }
		});
	  //hamburger animation
	 hamburger.classList.toggle("toggle");
    }
	 
	}

window.onload = () => navSlide();
