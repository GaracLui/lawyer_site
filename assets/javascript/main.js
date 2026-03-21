const mybutton = document.getElementById("btn-back-to-top");

// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener('click', () => {
    window.scrollTo({top: 0, behavior: "smooth", });
})