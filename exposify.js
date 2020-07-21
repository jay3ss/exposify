// Exposify - by jay3ss
(function() {
    // callback function to remove the warning
    const closeWarning = (e) => {
        const warningElem = document.querySelector('.exposify-warning');
        warningElem.remove();
    }

    // Put a red border around the entire page
    const borderSize = 5;
    document.body.style.border = `${borderSize}px solid red`;

    // set the title
    document.title = `💀EXPOSED💀 - ${document.title}`;

    // add the warning
    let warning = "WARNING: This site is part of a network of ";
    warning += "fake local news sites known to spread propaganda. ";
    const textNode = document.createTextNode(warning);
    const pElement = document.createElement('p');
    const firstElem = document.body.firstElementChild;
    pElement.appendChild(textNode);

    // add a link to the warning
    const infoLink = document.createElement('a');
    const infoURL = "https://www.theatlantic.com/magazine/archive/2020/03/the-2020-disinformation-war/605530/";
    infoLink.href = infoURL;
    infoLink.target = "_blank";
    infoLink.title = "The Billion-Dollar Disinformation Campaign to Reelect the President"
    infoLink.text = "Click here for more info.";
    infoLink.className = "exposify-link";
    
    pElement.appendChild(infoLink);
    pElement.className = 'exposify-warning';

    // add an on-click event listener to remove the warning
    spanElem = document.createElement('span');
    spanElem.textContent = '✖';
    spanElem.className = 'exposify-close'
    spanElem.addEventListener('click', closeWarning);
    pElement.appendChild(spanElem);

    // add the content to the DOM
    document.body.prepend(pElement);
    const firstElemMargintop = Math.floor(pElement.getBoundingClientRect().height);
    firstElem.style.marginTop = `${firstElemMargintop-borderSize-1}px`;
})();

// "&#x274c;"