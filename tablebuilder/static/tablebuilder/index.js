/**
 * Code to execute when the HTML is loaded. Called at the bottom of this file.
 */
function onload() {
    let addButton = document.getElementById("add-button");
    addButton.addEventListener("click", addButtonCallback);
}


function addButtonCallback() {
    let tbody = document.querySelector("#table tbody");
    let row = renderNewRow();

    let addButton = document.getElementById("add-button");
    let addButtonRow = addButton.parentNode.parentNode;

    tbody.insertBefore(row, addButtonRow);
}


function saveButtonCallback(event) {
    let row = event.target.parentNode.parentNode;

    for (let input of row.querySelectorAll("input")) {
        let text = input.value.trim();
        input.parentNode.appendChild(document.createTextNode(text));
        input.remove();
    }

    let editButton = document.createElement("button");
    editButton.addEventListener("click", editButtonCallback);
    editButton.textContent = "Edit";
    event.target.parentNode.appendChild(editButton);
    event.target.remove();
}


function editButtonCallback(event) {
    console.log("Editing");
    console.log(event.target);
}


function renderNewRow() {
    let row = document.createElement("tr");
    for (let i = 0; i < 4; i++) {
        row.appendChild(renderNewCell());
    }

    let saveButton = document.createElement("button");
    saveButton.addEventListener("click", saveButtonCallback);
    saveButton.textContent = "Save";
    let saveButtonCell = document.createElement("td");
    saveButtonCell.appendChild(saveButton);
    row.appendChild(saveButtonCell);
    return row;
}


function renderNewCell() {
    let input = document.createElement("input");
    input.setAttribute("type", "text");
    let cell = document.createElement("td");
    cell.appendChild(input);
    return cell;
}


onload();
