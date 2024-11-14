

//  Create the JavaScript File

// static/js/admin/sale.js
document.addEventListener('DOMContentLoaded', function () {
    const productSelect = document.querySelector('select[name="product"]');
    const quantityInput = document.querySelector('input[name="quantity_sold"]');
    const salesTableBody = document.getElementById('sales-table-body');

    productSelect.addEventListener('change', function () {
        const selectedProductId = this.value;
        const selectedProductName = this.options[this.selectedIndex].text;

        // Clear previous rows
        salesTableBody.innerHTML = '';

        if (selectedProductId) {
            const quantity = quantityInput.value || 1; // Default to 1 if no quantity is set

            // Create a new row for the selected product
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${selectedProductName}</td>
                <td>${quantity}</td>
                <td>${quantity * 10} (example price)</td> <!-- Replace with actual price calculation -->
            `;
            salesTableBody.appendChild(row);
        }
    });
});
