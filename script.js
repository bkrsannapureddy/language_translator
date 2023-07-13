const fromText = document.querySelector(".from-text"),
toText = document.querySelector(".to-text"),
exchageIcon = document.querySelector(".exchange"),
selectTag = document.querySelectorAll("select"),
icons = document.querySelectorAll(".row i");
translateBtn = document.querySelector("button");

selectTag.forEach((tag, id) => {
    for (let country_code in countries) {
        let selected = id == 0 ? country_code == "fi" ? "selected" : "" : country_code == "hi" ? "selected" : "";
        let option = `<option ${selected} value="${country_code}">${countries[country_code]}</option>`;
        tag.insertAdjacentHTML("beforeend", option);
    }
});


    
fromText.addEventListener("keyup", () => {
    if(!fromText.value) {
        toText.value = "";
    }
});

translateBtn.addEventListener("click", () => {
    let text = fromText.value.trim(),
    translateFrom = selectTag[0].value,
    translateTo = selectTag[1].value;
    if(!text) return;
    toText.setAttribute("placeholder", "Translating...");
    let apiUrl = `https://translation.googleapis.com/language/translate/v2?key=API_KEY&q=${text}&source=${translateFrom}&target=${translateTo}`;
    fetch(apiUrl).then(res => res.json()).then(data => {
        toText.value = data.data.translations[0].translatedText;
        toText.setAttribute("placeholder", "Translation");
    }).catch(error => {
        console.error(error);
        toText.setAttribute("placeholder", "Error occurred");
    });
});

icons.forEach(icon => {
    icon.addEventListener("click", ({target}) => {
        if(!fromText.value || !toText.value) return;
        if(target.classList.contains("fa-copy")) {
            if(target.id == "to") {
                navigator.clipboard.writeText(toText.value);
            } 
        } else {
            let text;
            let languageCode;
            if (target.id == "from") {
                text = fromText.value;
                languageCode = selectTag[0].value;
            } else {
                text = toText.value;
                languageCode = selectTag[1].value;
            }
            
            // Call the function to play speech using Google Cloud Text-to-Speech API
            playSpeech(text, languageCode);
        }
    });
});

function playSpeech(text, languageCode) {
    // Construct the API request URL
    const apiUrl = `https://texttospeech.googleapis.com/v1/text:synthesize?key=YOUR_API_KEY`;
    
    // Set up the request parameters
    const request = {
        input: { text: text },
        voice: { languageCode: languageCode, ssmlGender: "FEMALE" },
        audioConfig: { audioEncoding: "MP3" }
    };

    // Send a POST request to the API
    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(request)
    })
        .then(response => response.json())
        .then(data => {
            // Extract the audio content from the API response
            const audioContent = data.audioContent;
            
            // Convert the base64-encoded audio content to binary format
            const audioData = atob(audioContent);
            const arrayBuffer = new ArrayBuffer(audioData.length);
            const view = new Uint8Array(arrayBuffer);
            for (let i = 0; i < audioData.length; i++) {
                view[i] = audioData.charCodeAt(i);
            }
            
            // Create a Blob object from the binary audio data
            const blob = new Blob([arrayBuffer], { type: "audio/mp3" });
            
            // Create an audio element and play the speech
            const audioElement = new Audio();
            audioElement.src = URL.createObjectURL(blob);
            audioElement.play();
        })
        .catch(error => {
            console.error(error);
        });
}
