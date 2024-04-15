function setFooter() {
    var currentYear = new Date().getFullYear();
    var footer = document.getElementsByTagName("footer")[0];

    var authorInfo = document.createElement('p');
    authorInfo.textContent = currentYear + ', by zluuba';

    footer.appendChild(authorInfo);
}

setFooter();
