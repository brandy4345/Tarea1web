// Get the modal
let modal1 = document.getElementById("modal1");
var modal2 = document.getElementById("modal2");
let modal3 = document.getElementById("modal3");
let modal4 = document.getElementById("modal4");
let modal5 = document.getElementById("modal5");

// Get the image and insert it inside the modal - use its "alt" text as a caption
let img1 = document.getElementById("pepino");
let img2 = document.getElementById("manzana");
let img3 = document.getElementById("apio");
let img4 = document.getElementById("platano");
let img5 = document.getElementById("sandia");

let modalImg1 = document.getElementById("img01");
let modalImg2 = document.getElementById("img02");
let modalImg3 = document.getElementById("img03");
let modalImg4 = document.getElementById("img04");
let modalImg5 = document.getElementById("img05");

img1.onclick = function(){
  modal1.style.display = "block";
  modalImg1.src = this.src;
}
img2.onclick = function(){
    modal2.style.display = "block";
    modalImg2.src = this.src;
}
img3.onclick = function(){
    modal3.style.display = "block";
    modalImg3.src = this.src;
}
img4.onclick = function(){
    modal4.style.display = "block";
    modalImg4.src = this.src;
}
img5.onclick = function(){
    modal5.style.display = "block";
    modalImg5.src = this.src;
}

// Get the <span> element that closes the modal
let span1 = document.getElementsByClassName("close")[0];
let span2 = document.getElementsByClassName("close")[1];
let span3 = document.getElementsByClassName("close")[2];
let span4 = document.getElementsByClassName("close")[3];
let span5 = document.getElementsByClassName("close")[4];

// When the user clicks on <span> (x), close the modal

// No me funciona pero segun deberia funcionar asi que lo dejo 
span1.onclick = function() { 
  modal1.style.display = "none";
}
span2.onclick = function() { 
    modal2.style.display = "none";
}
span3.onclick = function() { 
    modal3.style.display = "none";
}
span4.onclick = function() { 
    modal4.style.display = "none";
}
span5.onclick = function() { 
    modal5.style.display = "none";
}
