function vfun(){
    var uname1 =document.forms["myform"]["uname1"].value;
    var email =document.forms["myform"]["email"].value;
    var upswd1 =document.forms["myform"]["upswd1"].value;
    var upswd2 =document.forms["myform"]["upswd2"].value;

    if(uname1==null || uname1==""){
        document.getElementById("errorbox").innerHTML="Enter the Username";
        
        return false;
    }
    if(email==null || email==""){
        document.getElementById("errorbox").innerHTML="Enter the email";
        return false;
    }
    if(upswd1==null || upswd1==""){
        document.getElementById("errorbox").innerHTML="Enter the Password";
        return false;
    }
    if(upswd2==null || upswd2==""){
        document.getElementById("errorbox").innerHTML="Enter the Password";
        return false;
    }
    if(upswd1 != upswd2){
        document.getElementById("errorbox").innerHTML="Password does not match";
        return false;
    }
    if (uname1 != '' && upswd1 != '' && upswd2 != '' && email != '' && upswd1 == upswd2)


    alert("Register successfull");
                   

  }

  function vfun1(){
      var uname =document.forms["myform1"]["uname"].value;
      var password =document.forms["myform1"]["password"].value;

      if(uname==null || uname==""){
          document.getElementById("errorbox").innerHTML="Enter the Username";
          return false;
      }
      if(password==null || password==""){
          document.getElementById("errorbox").innerHTML="Enter the Password";
          return false;
      }
      if(uname !="" && password !=""){
          alert("Login Successfully");
      }
      
  }



  function addCart(){
      alert("Register Your Account..");
  }
