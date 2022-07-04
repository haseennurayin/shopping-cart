<html>
<head>
<title> Verification of valid Password </title>
</head>
<script>
function verifyPassword() {
  var pw = document.getElementById("pswd").value;

  if(pw == "") {
     document.getElementById("message").innerHTML = "**Fill the password please!";
     return false;
  }

  if(pw.length < 8) {
     document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";
     return false;
  }

  if(pw.length > 15) {
     document.getElementById("message").innerHTML = "**Password length must not exceed 15 characters";
     return false;
  } else {
     alert("Password is correct");
  }
}
</script>

<body>
<center>
<h1 style="color:green">Javatpoint</h1>
<h3> Verify valid password Example </h3>

<form onsubmit ="return verifyPassword()">

<td> Enter Password </td>
<input type = "password" id = "pswd" value = ""> 
<span id = "message" style="color:red"> </span> <br><br>


<input type = "submit" value = "Submit">


<button type = "reset" value = "Reset" >Reset</button>
</form>
</center>
</body>
</html>
