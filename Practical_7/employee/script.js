document.getElementById("myForm").addEventListener("submit", function(e) {

    e.preventDefault();

    let id = document.getElementById("id").value;
    let name = document.getElementById("name").value;
    let role = document.getElementById("role").value;
    let salary = document.getElementById("salary").value;

    let table = document.getElementById("table");

    let row = table.insertRow();

    row.insertCell(0).innerText = id;
    row.insertCell(1).innerText = name;
    row.insertCell(2).innerText = role;
    row.insertCell(3).innerText = salary;

    document.getElementById("myForm").reset();

});