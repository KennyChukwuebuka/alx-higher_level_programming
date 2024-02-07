$(document).ready(function() {
    // Function to add new LI element to the list
    $("#add_item").click(function() {
        $("<li>Item</li>").appendTo("ul.my_list");
    });

    // Function to remove the last LI element from the list
    $("#remove_item").click(function() {
        $("ul.my_list li:last-child").remove();
    });

    // Function to clear all LI elements from the list
    $("#clear_list").click(function() {
        $("ul.my_list").empty();
    });
});