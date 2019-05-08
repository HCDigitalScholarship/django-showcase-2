"use strict";


const TABLE_COLUMNS = 5;

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
    saveRow(row, true);
}


function cancelButtonCallback(event) {
    let row = event.target.parentNode.parentNode;
    saveRow(row, false);
}


function saveRow(row, useInputText) {
    for (let input of row.querySelectorAll(".content-cell input")) {
        let text = useInputText ? input.value.trim()
                                : input.getAttribute("data-original");
        input.parentNode.appendChild(document.createTextNode(text));
        input.remove();
    }

    let editButton = document.createElement("button");
    editButton.classList.add("edit-button");
    editButton.addEventListener("click", editButtonCallback);
    editButton.textContent = "Edit";

    let removeButton = document.createElement("button");
    removeButton.classList.add("remove-button");
    removeButton.addEventListener("click", removeButtonCallback);
    removeButton.textContent = "Remove";

    let buttonCell = row.querySelector(".button-cell");
    buttonCell.innerHTML = "";
    buttonCell.appendChild(editButton);
    buttonCell.appendChild(removeButton);
}


function editButtonCallback(event) {
    let row = event.target.parentNode.parentNode;

    for (let cell of row.querySelectorAll(".content-cell")) {
        let text = cell.textContent;
        cell.textContent = "";

        let input = document.createElement("input");
        input.setAttribute("type", "text");
        input.setAttribute("data-original", text);
        input.value = text;
        cell.appendChild(input);
    }

    let saveButton = document.createElement("button");
    saveButton.classList.add("save-button");
    saveButton.addEventListener("click", saveButtonCallback);
    saveButton.textContent = "Save";

    let cancelButton = document.createElement("button");
    cancelButton.classList.add("cancel-button");
    cancelButton.addEventListener("click", cancelButtonCallback);
    cancelButton.textContent = "Cancel";

    let buttonCell = row.querySelector(".button-cell");
    buttonCell.innerHTML = "";
    buttonCell.appendChild(saveButton);
    buttonCell.appendChild(cancelButton);
}


function removeButtonCallback(event) {
    let row = event.target.parentNode.parentNode;
    row.remove();
}


function renderNewRow() {
    let row = document.createElement("tr");
    for (let i = 0; i < TABLE_COLUMNS - 1; i++) {
        row.appendChild(renderNewCell());
    }

    let saveButton = document.createElement("button");
    saveButton.classList.add("save-button");
    saveButton.addEventListener("click", saveButtonCallback);
    saveButton.textContent = "Save";

    let saveButtonCell = document.createElement("td");
    saveButtonCell.classList.add("button-cell");
    saveButtonCell.appendChild(saveButton);
    row.appendChild(saveButtonCell);

    return row;
}


function renderNewCell() {
    let input = document.createElement("input");
    input.setAttribute("type", "text");
    let cell = document.createElement("td");
    cell.classList.add("content-cell");
    cell.appendChild(input);
    return cell;
}


onload();
