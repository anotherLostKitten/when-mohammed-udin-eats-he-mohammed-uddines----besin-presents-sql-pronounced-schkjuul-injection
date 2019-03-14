var formy=document.getElementById("loggy");
var register = document.getElementById("registery");
var login = document.getElementById("loginry");

var switcherooR=(e)=>{
	formy.innerHTML="<h4>Register:</h4><br><form action=\"/registerr\" method=\"POST\"><input type=\"text\" class=\"intxt\"  name=\"user\" placeholder=\"Username\"><br><br><input class=\"intxt\" type=\"text\"  name=\"pass\" placeholder=\"Password\"><br><br><input type=\"submit\" name=\"regi\" value=\"Register\" class=\"btn btn-primary\"></form>";
	register.className = "btn btn-light";
	login.className = "btn btn-info";
};

var switcherooL=(e)=>{
	formy.innerHTML="<h4>Login:</h4><br><form action=\"/schkjuul\" method=\"POST\"> <input class=\"intxt\" type=\"text\" name=\"user\" placeholder=\"Username\"><br><br><input class=\"intxt\"  type=\"text\"  name=\"pass\" placeholder=\"Password\"><br><br><input type=\"submit\" name=\"auth\" value=\"Log In\" class=\"btn btn-primary\"></form>";
	register.className = "btn btn-info";
	login.className = "btn btn-light";
};


register.addEventListener('click',switcherooR);

login.addEventListener('click',switcherooL);
