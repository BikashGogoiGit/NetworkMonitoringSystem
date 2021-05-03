def add_new_machine():
    return '''
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form id="form" onsubmit="return false;">
    <input style="position:absolute; top:80%; left:5%; width:40%;" type="text" id="userInput" />
    <input style="position:absolute; top:50%; left:5%; width:40%;" type="submit" onclick="othername();" />
</form>
<script>
    function othername() {
var input = document.getElementById("userInput").value;
alert(input);
}
</script>

</body>
</html>
    '''
    return f"{input}"