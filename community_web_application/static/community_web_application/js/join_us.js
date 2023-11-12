var char = 0;
var login_div = document.getElementsByClassName("login-div")[0]
var sign_up_div = document.getElementsByClassName("sign-up-div")[0]
function toggle(){
    if(char == 0){
        login_div.style.display = 'none';
        sign_up_div.style.display='flex';
        char = 1;
    }else{
        login_div.style.display = 'flex';
        sign_up_div.style.display='none';
        char = 0;
    }
}