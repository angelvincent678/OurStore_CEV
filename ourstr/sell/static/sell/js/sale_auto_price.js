document.addEventListener("DOMContentLoaded", function() {
    const productSelect = document.getElementById("id_product");
    const priceField = document.getElementById("id_product_price");
    const bulkPriceField = document.getElementById("id_bulk_price");

    if (productSelect && priceField && bulkPriceField) {
        const productPrices = JSON.parse(productSelect.getAttribute("data-product-prices"));
        const productBulkPrices = JSON.parse(productSelect.getAttribute("data-product-bulk-prices"));

        productSelect.addEventListener("change", function() {
            const productId = productSelect.value;

            if (productId && productPrices[productId] !== undefined) {
                priceField.value = productPrices[productId];
                bulkPriceField.value = productBulkPrices[productId];
            } else {
                priceField.value = "-";
                bulkPriceField.value = "-";
            }
        });
    }
});
