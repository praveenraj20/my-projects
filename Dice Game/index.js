var randomNo1=Math.round(Math.random()*5+1);
var randomImage1="images/dice"+ randomNo1+".png";
document.querySelectorAll("img")[0].setAttribute("src",randomImage1);

var randomNo2=Math.round(Math.random()*5+1);
var randomImage2="images/dice"+randomNo2+".png";
document.querySelectorAll("img")[1].setAttribute("src",randomImage2);

if (randomNo1>randomNo2){
    document.querySelector("h1").innerHTML="🏆 Player 1 wins..!"
}
else if(randomNo1<randomNo2){
    document.querySelector("h1").innerHTML=" Player 2 wins 🏆..!"
}
else{
    document.querySelector("h1").innerHTML="Match Drawn..!"
}