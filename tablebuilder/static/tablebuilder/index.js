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


function saveButtonCallback() {
    console.log("Saving!");
}


function renderNewRow() {
    let row = document.createElement("tr");
    for (let i = 0; i < 4; i++) {
        row.appendChild(renderNewCell());
    }

    let saveButton = document.createElement("button");
    saveButton.addEventListener("click", saveButtonCallback);
    saveButton.textContent = "Save";
    row.appendChild(saveButton);
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
