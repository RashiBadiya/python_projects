<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Math Time</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background-color: #333;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  #calculator {
    background-color: #222;
    border: 3px solid #444;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }
  input[type="text"] {
    width: 200px;
    height: 40px;
    font-size: 20px;
    margin-bottom: 10px;
    border: none;
    border-radius: 5px;
    padding: 5px;
    background-color: #444;
    color: #fff;
  }
  input[type="button"] {
    width: 50px;
    height: 50px;
    font-size: 20px;
    margin: 5px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    background-color: #666;
    color: #fff;
  }
  .row {
    display: flex;
    justify-content: center;
  }
</style>
</head>
<body>
  <div id="calculator">
    <input type="text" id="display" disabled><br>
    <div class="row">
      <input type="button" value="1" onclick="addToDisplay('1')">
      <input type="button" value="2" onclick="addToDisplay('2')">
      <input type="button" value="3" onclick="addToDisplay('3')">
      <input type="button" class="operator" value="+" onclick="addToDisplay('+')">
    </div>
    <div class="row">
      <input type="button" value="4" onclick="addToDisplay('4')">
      <input type="button" value="5" onclick="addToDisplay('5')">
      <input type="button" value="6" onclick="addToDisplay('6')">
      <input type="button" class="operator" value="-" onclick="addToDisplay('-')">
    </div>
    <div class="row">
      <input type="button" value="7" onclick="addToDisplay('7')">
      <input type="button" value="8" onclick="addToDisplay('8')">
      <input type="button" value="9" onclick="addToDisplay('9')">
      <input type="button" class="operator" value="*" onclick="addToDisplay('*')">
    </div>
    <div class="row">
      <input type="button" value="C" onclick="clearDisplay()">
      <input type="button" value="0" onclick="addToDisplay('0')">
      <input type="button" class="operator" value="/" onclick="addToDisplay('/')">
      <input type="button" value="=" onclick="calculate()">
    </div>
  </div>

  <script>
    function addToDisplay(value) {
      document.getElementById('display').value += value;
    }
    
    function clearDisplay() {
      document.getElementById('display').value = '';
    }
    
    function calculate() {
      try {
        var result = eval(document.getElementById('display').value);
        document.getElementById('display').value = result;
      } catch (error) {
        document.getElementById('display').value = 'Error';
      }
    }
  </script>
</body>
</html>
