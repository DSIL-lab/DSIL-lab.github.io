(function () {
  var img = document.querySelector(".pi-photo");
  if (!img) return;

  var raw = img.getAttribute("data-photo-by-term");
  if (!raw) return;

  var photoByTerm;
  try { photoByTerm = JSON.parse(raw); } catch (e) { return; }

  var term = "";
  try { term = sessionStorage.getItem("dsilActiveTerm") || ""; } catch (e) {}
  if (!term || !photoByTerm[term]) {
    var seasonOrder = { spring: 1, summer: 2, fall: 3, winter: 4 };
    term = Object.keys(photoByTerm).sort(function (a, b) {
      var ma = /^(\d{4})-(spring|summer|fall|winter)$/i.exec(a);
      var mb = /^(\d{4})-(spring|summer|fall|winter)$/i.exec(b);
      if (ma && mb) {
        if (+ma[1] !== +mb[1]) return +mb[1] - +ma[1];
        return seasonOrder[mb[2].toLowerCase()] - seasonOrder[ma[2].toLowerCase()];
      }
      return a < b ? 1 : -1;
    })[0];
    if (!term || !photoByTerm[term]) return;
  }

  var baseUrl = (document.querySelector(".pi-profile") || {}).getAttribute
    ? document.querySelector(".pi-profile").getAttribute("data-base-url") || ""
    : "";
  var path = String(photoByTerm[term]);
  if (!/^(https?:)?\/\//i.test(path) && path.charAt(0) !== "/") path = "/" + path;
  if (baseUrl && !/^(https?:)?\/\//i.test(path) && path.indexOf(baseUrl + "/") !== 0 && path !== baseUrl) {
    var base = baseUrl.charAt(0) === "/" ? baseUrl : "/" + baseUrl;
    if (base.length > 1 && base.charAt(base.length - 1) === "/") base = base.slice(0, -1);
    path = base + path;
  }
  img.src = path;
})();
