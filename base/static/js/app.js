var current = document.getElementById('current').textContent;
var victim = document.getElementById('victim').textContent;

if ( current.length < victim.length ) {
  var spaces = Math.floor((victim.length - current.length)/2);
  current = ' '.repeat(spaces) + current;
} else if ( current.length > victim.length ) {
  var spaces = current.length - victim.length;
  victim = victim + 'x'.repeat(spaces);
}

odoo.default({ el:'.js-odoo', from: current, to: victim, animationDelay: 1000, letterAnimationDelay: 100 });

setTimeout(function(){ 
	$('.wrapper').fadeTo( "slow" , 1);
  $('.message').fadeTo( "slow" , 1);
}, 5000);

for (var i = 0; i < 500; i++) {
	create(i);
}

function create(i) {
  var width = Math.random() * 8;
  var height = width * 0.4;
  var colourIdx = Math.ceil(Math.random() * 3);
  var colour = "red";
  switch(colourIdx) {
    case 1:
      colour = "tech";
      break;
    case 2:
      colour = "design";
      break;
    case 3:
      colour = "product";
      break;
    case 3:
      colour = "marketing";
      break;
    default:
      colour = "culture";
  }

  $('<div class="confetti-'+i+' '+colour+'"></div>').css({
    "width" : width+"px",
    "height" : height+"px",
    "top" : -Math.random()*20+"%",
    "left" : Math.random()*100+"%",
    "opacity" : Math.random()+0.5,
    "transform" : "rotate("+Math.random()*360+"deg)"
  }).appendTo('.wrapper');  
  
  drop(i);
}

function drop(x) {
  $('.confetti-'+x).animate({
    top: "100%",
    left: "+="+Math.random()*15+"%"
  }, Math.random()*3000 + 3000, function() {
    reset(x);
  });
}

function reset(x) {
  $('.confetti-'+x).animate({
    "top" : -Math.random()*20+"%",
    "left" : "-="+Math.random()*15+"%"
  }, 0, function() {
    drop(x);             
  });
}
