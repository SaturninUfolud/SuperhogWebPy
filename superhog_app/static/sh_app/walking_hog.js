

function walking_hog() {

    var static_hog = document.getElementById("static_hog");
    if (static_hog.style.display == "none") {
        console.log("Hog is already walking");
        return;
    }
    var hog_posX = 0;
    static_hog.style.display = "none";
    var animated_hog = document.getElementById("walking_hog");
    animated_hog.style.display = null;
    var hog_w1 = window.innerWidth;
    var id = setInterval(frame, 10);
    function frame() {
        if (hog_posX >= window.innerWidth || hog_posX >= hog_w1) {
            clearInterval(id);
            animated_hog.style.display = "none";
            animated_hog.style.left = 0 + "px";
            static_hog.style.display = null;
        }
        else {
            hog_posX += 2;
            animated_hog.style.left = hog_posX + 'px';
        }
    }
}