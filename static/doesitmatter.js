var formy=document.getElementById("loggy");

var switcherooR=(e)=>{
  formy.innerHTML="<h4>Register:</h4><form action=\"/register\"><input type=\"text\"  name=\"user\" placeholder=\"username\"><input type=\"text\"  name=\"pass\" placeholder=\"password\"><input type=\"submit\" name=\"regi\" value=\"Register\"></form>";
};

var switcherooL=(e)=>{
  formy.innerHTML="<h4>Login:</h4>  <form action=\"/login\"> <input type=\"text\" name=\"user\" placeholder=\"username\"> <input type=\"text\"  name=\"pass\" placeholder=\"password\">  <input type=\"submit\" name=\"auth\" value=\"Log In\"></form>";
};


var register = document.getElementById("registery");
register.addEventListener('click',switcherooR);

var login = document.getElementById("loginy");
login.addEventListener('click',switcherooL);