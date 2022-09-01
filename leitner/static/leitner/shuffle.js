(()=>{
var word ;
var orignal;
var text="";
const rotationGap = 4;
var clock2 ;
var j;
var l;
var c;
var p;

window.addEventListener("load",() => {
    word = document.querySelector(".mean");
    orignal = `itsGoodBits`;
    l=orignal.length;
    j=c=p=0;
    clock2 = setInterval(shuffle,30);
});

function shuffle(){
    if(p-->0) return;
    text="";
    for(var k=0;k<j;k++) text += orignal[k];
    for(var k=j;k<j+4 && k<l;k++){
        text += String.fromCharCode(
            (Math.random()>0.5)?
            (Math.floor(Math.random()*26) + 65):
            (Math.floor(Math.random()*26) + 97)
        );
    }
    c++;
    if(c==rotationGap){
        c=0;
        j += 1;
    }
    word.innerText = text ;
    if(j>=l+1){
        j=0;
        c=0;
        p=100;
    }
}
})();
