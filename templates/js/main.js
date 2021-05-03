var firebaseConfig = {
        apiKey: "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        authDomain: "experiment-663c2.firebaseapp.com",
        databaseURL: "https://experiment-663c2-default-rtdb.firebaseio.com",
        projectId: "experiment-663c2",
        storageBucket: "experiment-663c2.appspot.com",
        messagingSenderId: "378598338807",
        appId: "1:378598338807:web:114229685379655a45a3f2",
        measurementId: "G-E8WX073DSD"
      };
      firebase.initializeApp(firebaseConfig);
      firebase.analytics();
     var messageRef = firebase.database();

    document.getElementById('form').addEventListener('submit', submitForm);

    function submitForm(e){
        e.preventDefault();
        var ip = getInputValue('ip');
        savemessage(ip);
    }

    function getInputValue(id){
       return document.getElementById(id).value;
    }

    function savemessage(ip){
      var newMessage = messageRef.push();
      newMessage.set(
      {
        ip: ip,
      }
      );
    }