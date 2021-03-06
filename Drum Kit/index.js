
// function for button-press

var noOfDrumButtons=document.querySelectorAll(".drum").length;

for (i=0; i<noOfDrumButtons; i++){
    document.querySelectorAll(".drum")[i].addEventListener("click",function(){
       var buttonInnerHtml = this.innerHTML;
       makeSound(buttonInnerHtml);
       buttonAnimation(buttonInnerHtml);
    });

}
// function for keyboard-press

document.addEventListener("keypress",function(event){
    makeSound(event.key);
    buttonAnimation(event.key);
});


function makeSound(key){
    switch (key) {
        case "p":
           var tom1= new Audio("sounds/tom-1.mp3");
           tom1.play();
           break;
        case "r":
           var tom2= new Audio("sounds/tom-2.mp3");
           tom2.play();
           break;
        case "a":
           var tom3= new Audio("sounds/tom-3.mp3");
           tom3.play();
           break;
        case "v":
           var tom4= new Audio("sounds/tom-4.mp3");
           tom4.play();
           break;   
        case "e":
           var crash= new Audio("sounds/crash.mp3");
           crash.play();
           break;  
        case "i":
           var kick= new Audio("sounds/kick-bass.mp3");
           kick.play();
           break; 
        case "n":
           var snare= new Audio("sounds/snare.mp3");
           snare.play();
           break; 

    
        default:
            break;
    }
}
        function buttonAnimation(currentkey){
           var activeButton=document.querySelector("."+currentkey);
           activeButton.classList.add("pressed");

           setTimeout(function(){
              activeButton.classList.remove("pressed");
           },100)

        }