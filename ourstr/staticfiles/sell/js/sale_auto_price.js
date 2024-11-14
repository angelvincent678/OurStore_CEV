

document.addEventListener("DOMContentLoaded", function() {
    // Find the product select field
    const productSelect = document.getElementById("id_product");
    const priceField = document.getElementById("id_product_price");

    // If elements are found, add an event listener
    if (productSelect && priceField) {
        productSelect.addEventListener("change", function() {
            // Get the selected option's text and split to extract the price
            const selectedOption = productSelect.options[productSelect.selectedIndex].text;
            const priceMatch = selectedOption.match(/₹(\d+(\.\d{1,2})?)/);

            if (priceMatch) {
                const price = priceMatch[1];
                priceField.value = price;
            } else {
                priceField.value = "-";
            }
        });
    }
});
