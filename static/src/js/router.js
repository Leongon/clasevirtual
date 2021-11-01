class indexView{
    constructor(){
            window.addEventListener("hashchange",e=>onRouteChange(e));
    }
    onRouteChange(e){
        console.log(e);
    }
}

new indexView();