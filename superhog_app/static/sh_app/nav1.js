window.onload = function()
{
    console.log("Hello world");
    let nav = document.getElementById("SH_NAV");
    let var1 = nav.getElementsByTagName("a");

    //let SH_MAIN_CONTENT = document.getElementsByTagName("SH_MAIN_CONTENT");

    function removePreviousActive(){
        let var2 = nav.querySelectorAll("a.active");
        for(let item of var2)
        {
            item.classList.remove("active");
        }
    }

    for(let item of var1)
    {
        item.onclick = function(event) {

            event.preventDefault();

            if(!item.classList.contains("active"))
            {
                removePreviousActive();
                item.classList += "active";

                console.log("Rzaba");
                console.log("Gadzior:"+item.href);
                window.history.pushState({}, null, item.href);
            }

        }
        console.log(item);
    }
}