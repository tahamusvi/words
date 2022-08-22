let slider ;
let angleOffset = 0 ;
let unitAngle ;
let lastMousePosition ;
let curMousePosition ;
let deltaMouse ;
let clock ;
let lastFrameTime = NaN ;
let velocity = 0;
let meanPosition = 0 ;
let position = 0;
const springConstant = 80 ;
const sliderMass = 1 ;
const dampingForce = 10 ;
const acceleration = -60 ;
const mouseSensitivity = 0.2 ;
const touchSensitivity = 0.25 ;
const MAX_VELOCITY = 1000 ;


window.onload = () => {
    let cards = [...document.querySelectorAll(".card")];
    slider = document.querySelector(".circular-slider") ;
    distribute(cards);
    window.addEventListener("mousedown",handleMouseDown);
    window.addEventListener("touchstart",handleTouchStart);
    window.addEventListener("touchmove",handleTouchMove);
    window.addEventListener("touchend",handleTouchEnd);
    window.addEventListener("wheel",throttle(handleWheel,300));
};

function handleMouseDown(event){
    cancelAnimation();
    lastMousePosition = event.clientX ;
    curMousePosition = event.clientX ;
    deltaMouse = 0 ;
    window.addEventListener("mousemove",handleMouseMove);
    window.addEventListener("mouseup",handleMouseUp);
}

function handleMouseMove(event){
    curMousePosition = event.clientX ;
    let delta = lastMousePosition - curMousePosition;
    deltaMouse = curMousePosition - lastMousePosition ;
    lastMousePosition = curMousePosition ;
    angleOffset += delta * mouseSensitivity ;
    lastMouseMoveTime = Date.now();
    setAngleOffset(angleOffset);
}

function handleMouseUp(){
    window.removeEventListener("mousemove",handleMouseMove);
    window.removeEventListener("mouseup",handleMouseUp);
    meanPosition = roundToFactor(angleOffset,unitAngle) ;
    velocity = - deltaMouse * 50 * mouseSensitivity ;
    position = angleOffset ;
    clock = requestAnimationFrame(spin);
}

function handleTouchStart(event){
    cancelAnimation();
    lastMousePosition = event.touches[0].clientX ;
    curMousePosition = event.touches[0].clientX ;
    deltaMouse = 0 ;
}

function handleTouchMove(event){
    curMousePosition = event.touches[0].clientX ;
    let delta = lastMousePosition - curMousePosition;
    deltaMouse = curMousePosition - lastMousePosition ;
    lastMousePosition = curMousePosition ;
    angleOffset += delta * touchSensitivity ;
    setAngleOffset(angleOffset);
}

function handleTouchEnd(){
    meanPosition = roundToFactor(angleOffset,unitAngle) ;
    velocity = - deltaMouse * 50 * touchSensitivity ;
    position = angleOffset ;
    clock = requestAnimationFrame(spin);
}

let decayClock = 0;

function throttle(fn, wait) {
    var time = Date.now();
    return function(event) {
      if ((time + wait - Date.now()) < 0) {
        fn(event);
        time = Date.now();
      }
    }
}

function handleWheel(event){
    cancelAnimation();
    velocity += 100 * Math.sign(event.deltaY) ;
    clock = requestAnimationFrame(spin);
}


let roundToFactor = (value,factor) => Math.round(value/factor)*factor ;

function distribute(cards) {
    if(cards.length == 0) 
        return ;
    let angle = Math.PI*2/cards.length ;
    unitAngle = 360 / cards.length ;
    let radius = cards[0].offsetWidth/(2*Math.tan(angle/2)) + 16;
    slider.style.transformOrigin = `center center ${-radius}px` ;
    cards.forEach((card,index)=> {
        let tiltAngle = index*angle ;
        let deltaZ = radius * (1 - Math.cos(tiltAngle));
        let deltaY = radius * Math.sin(tiltAngle) ;
        card.style.transform = `
            translate3d(${deltaY}px,0px,${-deltaZ}px)
            rotateY(${tiltAngle*180/Math.PI}deg)
        ` ;
    });
}

function setAngleOffset(newOffset){
    angleOffset = newOffset ;
    slider.style.transform = `rotateY(${-angleOffset}deg)` ;
}

function snap(currentFrameTime){
    lastFrameTime = lastFrameTime || (currentFrameTime ) ;
    let deltaTime = (currentFrameTime - lastFrameTime)/1000 ;

    let displacement = position - meanPosition ;
    let netForce = - displacement * springConstant - velocity*dampingForce ;
    let acceleration = netForce / sliderMass ;
    velocity += acceleration * deltaTime ;
    position += velocity * deltaTime ;
    angleOffset = position ;
    setAngleOffset(angleOffset);

    lastFrameTime = currentFrameTime ;
    if(Math.abs(acceleration) > 0.1 ){
        clock = requestAnimationFrame(snap);
    } else {
        meanPosition = roundToFactor(angleOffset,unitAngle);
        angleOffset = meanPosition ;
        lastFrameTime = NaN ;
        animating = false ;
    }
}

function cancelAnimation(){
    cancelAnimationFrame(clock);
    lastFrameTime = NaN ;
}

function spin(currentFrameTime){
    lastFrameTime = lastFrameTime || (currentFrameTime ) ;
    let deltaTime = (currentFrameTime - lastFrameTime)/1000 ;

    velocity += Math.sign(velocity) * acceleration * deltaTime ;
    angleOffset += velocity * deltaTime ;
    position = angleOffset ;
    setAngleOffset(angleOffset);

    animating = true ;

    lastFrameTime = currentFrameTime ;
    if(Math.abs(velocity) > 10){
        clock = requestAnimationFrame(spin);
    } else {
        meanPosition = roundToFactor(angleOffset,unitAngle);
        position = angleOffset ;
        lastFrameTime = NaN ;
        clock = requestAnimationFrame(snap);
    }
}

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
    word = document.querySelector(".name");
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