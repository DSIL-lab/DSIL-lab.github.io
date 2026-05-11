document.addEventListener("DOMContentLoaded", function() {
  var cards = document.querySelectorAll(".news-item-click");

  for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener("click", function(e) {
      if (e.target.closest("a")) return;
      var url = this.getAttribute("data-url");
      if (url) window.location.href = url;
    });

    cards[i].addEventListener("keydown", function(e) {
      if (e.key === "Enter") {
        e.preventDefault();
        var url = this.getAttribute("data-url");
        if (url) window.location.href = url;
      }
    });
  }
});
