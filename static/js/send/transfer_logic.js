// This class will contain variables and methods to handle selected qnotes for transfer and updating the view accordingly

/*
{
    "serial": "123456789",
    "amount": 10,
}
*/
let selected = [];

function addSerial(serial) {
    selected.push(serial);
}


function deleteSerial(serial) {
    for (let i = 0; i < selected.length; i++) {
        if (selected[i].serial == serial) {
            selected.splice(i, 1);
        }
    }
}

function getSerial(serial) {
    for (let i = 0; i < selected.length; i++) {
        if (selected[i].serial == serial) {
            return selected[i];
        }
    }
    return null;
}

function clearSelected() {
    selected = [];
}

function getSelected() {
    return selected;
}

// Frontend logic for the transfer page

function clearView() {
    $('#selected-amount').html('<h2>No banknotes selected</h2>');
    $('#selected-serials').html('');
}

function calculateTotal() {
    let total = 0;
    for (let i = 0; i < selected.length; i++) {
        // convert to int
        total += parseInt(selected[i].amount);
    }
    return total;
}

function templateItem(serial, amount) {
    // List item 
    // R<Amount> <Serial>
    // Add a jquery click event to remove the serial from the selected list
    return `
        <li class="list-group-item d-flex justify-content-between align-items-center">
            R${amount} ${serial}
            <div class="badge badge-danger badge-pill" id="remove-${serial}">
            <span>X</span>
            </div>
        </li>
    `;
}

function updateView() {
    $('#selected-amount').html(`<h2>Selected Amount: R ${calculateTotal()}</h2>`);
    $('#selected-serials').html('');
    for (let i = 0; i < selected.length; i++) {
        $('#selected-serials').append(templateItem(selected[i].serial, selected[i].amount));
        $(`#remove-${selected[i].serial}`).click(function () {
            deleteSerial(selected[i].serial);
            updateView();
        });
    }
}




