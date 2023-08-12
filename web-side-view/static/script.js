function showDiv() {
  const div = document.getElementById("chatbot");
  // Check the current display state of the div
  const currentDisplay = div.style.display;
  // Toggle the display property
  div.style.display = currentDisplay === "none" ? "flex" : "none";
}

document.addEventListener("DOMContentLoaded", function() {
  // Scroll the .qnas div to the bottom after the content has loaded
  const qnasDiv = document.getElementById('Top');
  if (qnasDiv) {
    qnasDiv.scrollTop = qnasDiv.scrollHeight;
  }
});
